import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] wineList = new int[n+1];
        for (int i = 1; i <= n; i++) {
            wineList[i] = sc.nextInt();
        }

        int[] dp = new int[n+1];
        dp[1] = wineList[1];
        if (n >= 2) dp[2] = wineList[1] + wineList[2];

        for (int i = 3; i <= n; i++) {
            dp[i] = Math.max(dp[i-1],
                    Math.max(dp[i-2] + wineList[i],
                            dp[i-3] + wineList[i-1] + wineList[i]));
        }

        System.out.println(dp[n]);
    }
}