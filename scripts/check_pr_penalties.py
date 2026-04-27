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


def github_request(url: str) -> Any:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN is required.")

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "algorithm-study-pr-penalty-checker",
    }
    req = request.Request(url, headers=headers)

    try:
        with request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed: {exc.code} {body}") from exc


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
        page_items = github_request(url)

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
    submitted_members: list[Member],
    missed_members: list[Member],
) -> str:
    lines = [
        "# PR 벌주 현황",
        "",
        f"- 최근 점검 구간: `{start.strftime('%Y-%m-%d %H:%M %Z')} ~ {end.strftime('%Y-%m-%d %H:%M %Z')}`",
        f"- 제출자: {', '.join(member.name for member in submitted_members) if submitted_members else '없음'}",
        f"- 미제출자: {', '.join(member.name for member in missed_members) if missed_members else '없음'}",
        "",
        "| 이름 | GitHub | 벌주 |",
        "| --- | --- | ---: |",
    ]

    sorted_members = sorted(
        board["members"].items(),
        key=lambda item: (-item[1]["penalties"], item[1]["name"]),
    )
    for github_login, info in sorted_members:
        lines.append(f"| {info['name']} | `{github_login}` | {info['penalties']} |")

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


def main() -> int:
    config = load_json(CONFIG_PATH)
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not repo:
        raise RuntimeError("GITHUB_REPOSITORY is required.")

    members = [Member(github=item["github"], name=item["name"]) for item in config["members"]]
    member_by_login = {member.github.lower(): member for member in members}

    start, end, period_id = get_cutoff_window(config)
    board = load_penalty_board(members)

    for history_item in board["history"]:
        if history_item["period_end"] == period_id:
            print(f"Period {period_id} was already processed. Skipping duplicate penalty update.")
            markdown = build_markdown(board, start, end, [], [])
            PENALTY_MD_PATH.write_text(markdown, encoding="utf-8")
            return 0

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

    board["history"].append(
        {
            "period_end": period_id,
            "submitted": [member.name for member in submitted_members],
            "missed": [member.name for member in missed_members],
        }
    )

    save_json(PENALTY_JSON_PATH, board)
    markdown = build_markdown(board, start, end, submitted_members, missed_members)
    PENALTY_MD_PATH.write_text(markdown, encoding="utf-8")

    submitted_text = ", ".join(member.name for member in submitted_members) if submitted_members else "없음"
    missed_text = ", ".join(member.name for member in missed_members) if missed_members else "없음"
    message = (
        f"[알고리즘 스터디 PR 체크]\n"
        f"- 점검 구간: {start.strftime('%Y-%m-%d %H:%M %Z')} ~ {end.strftime('%Y-%m-%d %H:%M %Z')}\n"
        f"- 제출자: {submitted_text}\n"
        f"- 미제출자: {missed_text}"
    )

    send_webhook(os.environ.get("SLACK_WEBHOOK_URL", ""), message)
    send_webhook(os.environ.get("DISCORD_WEBHOOK_URL", ""), message)

    print(message)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
