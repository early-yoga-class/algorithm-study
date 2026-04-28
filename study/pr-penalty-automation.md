# PR 벌주 자동화

매주 월요일 `09:00 (KST)`에 GitHub Actions가 실행되어 지난 1주 동안의 PR 제출 여부를 확인합니다.

## 동작 방식

1. `.github/workflows/pr-penalty-check.yml` 이 매주 월요일 `00:00 UTC`에 실행됩니다.
2. `scripts/check_pr_penalties.py` 가 `지난 월요일 09:00 ~ 이번 월요일 09:00 (KST)` 사이의 PR을 조회합니다.
3. `.github/pr-penalty-config.json` 에 등록된 멤버 중 PR이 없는 사람에게 벌주를 `+1` 합니다.
4. 결과를 `study/penalties.json`, `study/penalties.md` 에 저장하고 커밋합니다.
5. 제출로 인정된 PR 중 열려 있고 `main` 대상인 PR은 자동 머지를 시도합니다.
6. 설정된 웹훅이 있으면 Slack/Discord로 결과를 보냅니다.

## 설정할 것

### 1. 멤버 목록 수정

`.github/pr-penalty-config.json` 의 `members` 배열을 실제 GitHub 아이디 기준으로 맞춰 주세요.

### 2. GitHub Secrets 추가

Repository `Settings > Secrets and variables > Actions` 에 아래 값을 넣어 주세요.

- `SLACK_WEBHOOK_URL`
- `DISCORD_WEBHOOK_URL`

둘 중 하나만 써도 됩니다. 비워두면 해당 알림은 건너뜁니다.

### 3. 조건 조정

`.github/pr-penalty-config.json` 에서 아래 값을 바꿀 수 있습니다.

- `auto_merge_enabled`: `false` 로 바꾸면 자동 머지를 끔
- `auto_merge_method`: `merge`, `squash`, `rebase` 중 선택
- `auto_merge_base_branch`: 자동 머지 대상 base 브랜치
- `count_drafts`: `false` 로 바꾸면 draft PR은 제출로 인정하지 않음
- `required_labels`: 예를 들어 `["알고리즘"]` 으로 넣으면 해당 라벨이 있는 PR만 인정
- `cutoff_hour`: 마감 시각 조정

## 수동 실행

Actions 탭에서 `PR Penalty Check` 워크플로우를 `Run workflow` 로 수동 실행할 수 있습니다.

같은 주차에 다시 실행해도 `history` 를 보고 중복 벌주를 올리지 않습니다.
