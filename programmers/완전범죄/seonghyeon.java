import java.util.*;

class Solution {
    public int solution(int[][] info, int n, int m) {
        long sumA = 0;
        for (int[] x : info) sumA += x[0];

        int cap = m - 1;
        int best = 0;

        if (cap >= 0) {
            int[] dp = new int[cap + 1];
            Arrays.fill(dp, -1);
            dp[0] = 0;

            for (int[] x : info) {
                int a = x[0], b = x[1];

                for (int w = cap; w >= b; --w) {
                    if (dp[w - b] != -1) {
                        dp[w] = Math.max(dp[w], dp[w - b] + a);
                    }
                }
            }
            for (int w = 0; w <= cap; ++w) best = Math.max(best, dp[w]);
        }

        long ansA = sumA - best;
        return ansA < n ? (int) ansA : -1;
    }
}