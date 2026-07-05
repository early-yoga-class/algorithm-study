import java.util.*;

class Solution {
    static final int INF = Integer.MAX_VALUE / 2;
    static final int OFFSET = 10;   // 온도 -10~40 → 0~50
    static final int MAX_T = 50;

    public int solution(int temperature, int t1, int t2, int a, int b, int[] onboard) {
        int n = onboard.length;
        int out = temperature + OFFSET;
        int lo = t1 + OFFSET, hi = t2 + OFFSET;

        int[][] dp = new int[n][MAX_T + 1];
        for (int[] row : dp) Arrays.fill(row, INF);
        dp[0][out] = 0; // 0분 실내온도 = 실외온도

        for (int i = 0; i < n - 1; i++) {
            for (int t = 0; t <= MAX_T; t++) {
                if (dp[i][t] >= INF) continue;
                int cur = dp[i][t];

                // 1) OFF: 실외온도 방향으로 1도 (비용 0)
                relax(dp, i + 1, t + Integer.signum(out - t), cur, onboard[i + 1], lo, hi);

                // 2) ON, 희망온도 == 실내온도: 유지 (비용 b)
                relax(dp, i + 1, t, cur + b, onboard[i + 1], lo, hi);

                // 3) ON, 희망온도 != 실내온도: ±1 (비용 a)
                if (t + 1 <= MAX_T) relax(dp, i + 1, t + 1, cur + a, onboard[i + 1], lo, hi);
                if (t - 1 >= 0)     relax(dp, i + 1, t - 1, cur + a, onboard[i + 1], lo, hi);
            }
        }

        int answer = INF;
        for (int t = 0; t <= MAX_T; t++) answer = Math.min(answer, dp[n - 1][t]);
        return answer;
    }

    private void relax(int[][] dp, int time, int temp, int cost, int boarding, int lo, int hi) {
        if (boarding == 1 && (temp < lo || temp > hi)) return; // 탑승 중 쾌적 범위 필수
        if (cost < dp[time][temp]) dp[time][temp] = cost;
    }
}
