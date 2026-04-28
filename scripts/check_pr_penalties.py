from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from urllib import error, parse, request
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / ".github" / "pr-penalty-config.json"
PENALTY_JSON_PATH = ROOT / "study" / "penalties.json"
PENALTY_MD_PATH = ROOT / "study" / "penalties.md"
GITHUB_API_BASE = "https://api.github.com"


@dataclass
class Member:
    github: str
    name: str


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)
        file.write("\n")


def github_request(method: str, url: str, payload: dict[str, Any] | None = None) -> Any:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required.")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "algorithm-study-pr-penalty-checker",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = request.Request(url, headers=headers, data=data, method=method)

    try:
        with request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else {}
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed: {exc.code} {body}") from exc


def github_request_safe(method: str, url: str, payload: dict[str, Any] | None = None) -> tuple[bool, Any]:
    try:
        return True, github_request(method, url, payload)
    except RuntimeError as exc:
        return False, str(exc)


def get_cutoff_window(config: dict[str, Any]) -> tuple[datetime, datetime, str]:
    tz = ZoneInfo(config["timezone"])
    now = datetime.now(tz)
    cutoff_weekday = int(config["cutoff_weekday"])
    cutoff_hour = int(config["cutoff_hour"])

    cutoff = now.replace(hour=cutoff_hour, minute=0, second=0, microsecond=0)
    cutoff -= timedelta(days=(cutoff.weekday() - cutoff_weekday) % 7)
    if now < cutoff:
        cutoff -= timedelta(days=7)

    start = cutoff - timedelta(days=7)
    period_id = cutoff.strftime("%Y-%m-%d %H:%M %Z")
    return start, cutoff, period_id


def parse_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def fetch_prs_for_window(
    repo: str,
    start: datetime,
    end: datetime,
    count_drafts: bool,
    required_labels: set[str],
) -> list[dict[str, Any]]:
    pulls: list[dict[str, Any]] = []
    page = 1

    while True:
        query = parse.urlencode(
            {
                "state": "all",
                "sort": "created",
                "direction": "desc",
                "per_page": 100,
                "page": page,
            }
        )
        url = f"{GITHUB_API_BASE}/repos/{repo}/pulls?{query}"
        page_items = github_request("GET", url)

        if not page_items:
            break

        reached_older_items = False
        for pr in page_items:
            created_at = parse_datetime(pr["created_at"]).astimezone(start.tzinfo)

            if created_at < start:
                reached_older_items = True
                continue

            if created_at >= end:
                continue

            if not count_drafts and pr.get("draft"):
                continue

            pr_labels = {label["name"] for label in pr.get("labels", [])}
            if required_labels and required_labels.isdisjoint(pr_labels):
                continue

            pulls.append(pr)

        if reached_older_items:
            break

        page += 1

    return pulls


def load_penalty_board(members: list[Member]) -> dict[str, Any]:
    if PENALTY_JSON_PATH.exists():
        board = load_json(PENALTY_JSON_PATH)
    else:
        board = {"members": {}, "history": []}

    board.setdefault("members", {})
    board.setdefault("history", [])

    for member in members:
        board["members"].setdefault(
            member.github,
            {
                "name": member.name,
                "penalties": 0,
                "missed_periods": [],
            },
        )
        board["members"][member.github]["name"] = member.name

    return board


def build_markdown(
    board: dict[str, Any],
    start: datetime,
    end: datetime,
    submitted_names: list[str],
    missed_names: list[str],
) -> str:
    max_penalties = max((member["penalties"] for member in board["members"].values()), default=0)
    lines = [
        "# PR 벌주 현황",
        "",
        f"- 최근 점검 구간: `{start.strftime('%Y-%m-%d %H:%M %Z')} ~ {end.strftime('%Y-%m-%d %H:%M %Z')}`",
        f"- 제출자: {', '.join(submitted_names) if submitted_names else '없음'}",
        f"- 미제출자: {', '.join(missed_names) if missed_names else '없음'}",
        "",
        "| 이름 | GitHub | 벌주 |",
        "| --- | --- | ---: |",
    ]

    sorted_members = sorted(
        board["members"].items(),
        key=lambda item: (-item[1]["penalties"], item[1]["name"]),
    )
    for github_login, info in sorted_members:
        crown = "👑 " if max_penalties > 0 and info["penalties"] == max_penalties else ""
        lines.append(f"| {crown}{info['name']} | `{github_login}` | {info['penalties']} |")

    lines.extend(["", "## 기록", ""])

    history = sorted(board["history"], key=lambda item: item["period_end"], reverse=True)
    if not history:
        lines.append("- 아직 기록이 없습니다.")
    else:
        for item in history:
            lines.append(
                f"- `{item['period_end']}` 제출: {', '.join(item['submitted']) if item['submitted'] else '없음'} / "
                f"미제출: {', '.join(item['missed']) if item['missed'] else '없음'}"
            )

    lines.append("")
    return "\n".join(lines)


def send_webhook(url: str, content: str) -> None:
    if not url:
        return

    data = json.dumps({"content": content}).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "User-Agent": "algorithm-study-pr-penalty-checker"},
    )
    try:
        with request.urlopen(req):
            return
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"Webhook failed: {exc.code} {body}", file=sys.stderr)


def build_penalty_totals_text(board: dict[str, Any]) -> str:
    sorted_members = sorted(
        board["members"].values(),
        key=lambda item: (-item["penalties"], item["name"]),
    )
    max_penalties = max((member["penalties"] for member in sorted_members), default=0)
    parts = []
    for member in sorted_members:
        crown = "👑 " if max_penalties > 0 and member["penalties"] == max_penalties else ""
        parts.append(f"{crown}{member['name']} {member['penalties']}")
    return ", ".join(parts)


def get_history_entry(board: dict[str, Any], period_id: str) -> dict[str, Any] | None:
    for history_item in board["history"]:
        if history_item["period_end"] == period_id:
            return history_item
    return None


def filter_merge_candidates(
    prs: list[dict[str, Any]],
    member_logins: set[str],
    target_base_branch: str,
) -> list[dict[str, Any]]:
    candidates = []
    for pr in prs:
        user_login = pr.get("user", {}).get("login", "").lower()
        if user_login not in member_logins:
            continue
        if pr.get("state") != "open":
            continue
        if pr.get("draft"):
            continue
        if pr.get("base", {}).get("ref") != target_base_branch:
            continue
        candidates.append(pr)
    return candidates


def format_pr_reference(pr: dict[str, Any], member_by_login: dict[str, Member]) -> str:
    login = pr.get("user", {}).get("login", "")
    member = member_by_login.get(login.lower())
    display_name = member.name if member else login
    return f"#{pr['number']} {display_name}"


def merge_pull_requests(
    repo: str,
    prs: list[dict[str, Any]],
    merge_method: str,
    member_by_login: dict[str, Member],
) -> tuple[list[str], list[str]]:
    merged: list[str] = []
    failed: list[str] = []

    for pr in prs:
        merge_url = f"{GITHUB_API_BASE}/repos/{repo}/pulls/{pr['number']}/merge"
        payload = {
            "merge_method": merge_method,
            "commit_title": f"{pr['title']} (auto-merged by PR bot)",
        }
        ok, result = github_request_safe("PUT", merge_url, payload)
        pr_ref = format_pr_reference(pr, member_by_login)
        if ok and result.get("merged"):
            merged.append(pr_ref)
        else:
            reason = result.get("message", "merge failed") if isinstance(result, dict) else str(result)
            failed.append(f"{pr_ref} ({reason})")

    return merged, failed


def main() -> int:
    config = load_json(CONFIG_PATH)
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        raise RuntimeError("GITHUB_REPOSITORY is required.")

    members = [Member(github=item["github"], name=item["name"]) for item in config["members"]]
    member_by_login = {member.github.lower(): member for member in members}

    start, end, period_id = get_cutoff_window(config)
    board = load_penalty_board(members)
    existing_history = get_history_entry(board, period_id)

    prs = fetch_prs_for_window(
        repo=repo,
        start=start,
        end=end,
        count_drafts=bool(config.get("count_drafts", True)),
        required_labels=set(config.get("required_labels", [])),
    )

    submitted_logins = {
        pr["user"]["login"].lower()
        for pr in prs
        if pr.get("user", {}).get("login", "").lower() in member_by_login
    }

    if existing_history:
        print(f"Period {period_id} was already processed. Skipping duplicate penalty update.")
        submitted_names = existing_history.get("submitted", [])
        missed_names = existing_history.get("missed", [])
    else:
        submitted_members = sorted(
            (member_by_login[login] for login in submitted_logins),
            key=lambda member: member.name,
        )
        missed_members = sorted(
            (member for member in members if member.github.lower() not in submitted_logins),
            key=lambda member: member.name,
        )

        for member in missed_members:
            board["members"][member.github]["penalties"] += 1
            board["members"][member.github]["missed_periods"].append(period_id)

        submitted_names = [member.name for member in submitted_members]
        missed_names = [member.name for member in missed_members]

        board["history"].append(
            {
                "period_end": period_id,
                "submitted": submitted_names,
                "missed": missed_names,
            }
        )

    merge_candidates = filter_merge_candidates(
        prs=prs,
        member_logins=set(member_by_login),
        target_base_branch=config.get("auto_merge_base_branch", "main"),
    )
    merged_prs: list[str] = []
    failed_merges: list[str] = []

    if config.get("auto_merge_enabled", True) and merge_candidates:
        merged_prs, failed_merges = merge_pull_requests(
            repo=repo,
            prs=merge_candidates,
            merge_method=config.get("auto_merge_method", "squash"),
            member_by_login=member_by_login,
        )

    save_json(PENALTY_JSON_PATH, board)
    markdown = build_markdown(board, start, end, submitted_names, missed_names)
    PENALTY_MD_PATH.write_text(markdown, encoding="utf-8")

    submitted_text = ", ".join(submitted_names) if submitted_names else "없음"
    missed_text = ", ".join(missed_names) if missed_names else "없음"
    total_penalties_text = build_penalty_totals_text(board)
    merged_text = ", ".join(merged_prs) if merged_prs else "없음"
    failed_merge_text = ", ".join(failed_merges) if failed_merges else "없음"
    message = (
        f"[알고리즘 스터디 PR 체크]\n"
        f"- 점검 구간: {start.strftime('%Y-%m-%d %H:%M %Z')} ~ {end.strftime('%Y-%m-%d %H:%M %Z')}\n"
        f"- 제출자: {submitted_text}\n"
        f"- 미제출자: {missed_text}\n"
        f"- 총 벌주: {total_penalties_text}\n"
        f"- 자동 머지 성공: {merged_text}\n"
        f"- 자동 머지 실패: {failed_merge_text}"
    )

    send_webhook(os.environ.get("SLACK_WEBHOOK_URL", ""), message)
    send_webhook(os.environ.get("DISCORD_WEBHOOK_URL", ""), message)

    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
