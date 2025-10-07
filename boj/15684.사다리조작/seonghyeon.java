import java.util.Scanner;

public class Main {
    static boolean[][] ladder;
    static int n,m,h;
    static int answer = 4;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        h = sc.nextInt();

        ladder = new boolean[h + 1][n + 1];

        if (m == 0) {
            System.out.println(0);
            return;
        }

        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            ladder[a][b] = true;
        }

        dfs(0, 1, 1);

        System.out.println(answer == 4 ? -1 : answer);
    }

    static void dfs(int count, int x, int y) {
        if (count >= answer) return;

        if (checkAll()) {
            answer = count;
            return;
        }

        if (count == 3) return;

        for (int i = x; i <= h; i++) {
            for (int j = (i == x ? y : 1); j < n; j++) {

                if (ladder[i][j]) continue;
                if (j > 1 && ladder[i][j - 1]) continue;
                if (j < n - 1 && ladder[i][j + 1]) continue;

                ladder[i][j] = true;
                dfs(count + 1, i, j + 2);
                ladder[i][j] = false;
            }
        }
    }

    static boolean checkAll(){
        for(int i=1;i<=n;i++){
            if(!play(i)) return false;
        }
        return true;
    }

    static boolean play(int start){
        int now = start;
        for(int i = 1; i <= h; i++){
            if (now < n && ladder[i][now]) {
                now++;
            } else if (now > 1 && ladder[i][now - 1]) {
                now--;
            }
        }
        return now == start;
    }
}
