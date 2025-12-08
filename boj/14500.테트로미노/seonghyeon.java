import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Tetromino {
    static int answer = Integer.MIN_VALUE;
    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    static int n, m;
    static boolean[][] visited;
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(bf.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = true;
                dfs(i, j, 1, board[i][j]);
                visited[i][j] = false;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                checkTShape(i, j);
            }
        }

        System.out.println(answer);
    }

    public static void dfs(int x, int y, int depth, int sum) {
        if (depth == 4) {
            answer = Math.max(answer, sum);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (visited[nx][ny]) continue;

            visited[nx][ny] = true;
            dfs(nx, ny, depth + 1, sum + board[nx][ny]);
            visited[nx][ny] = false;
        }
    }

    public static void checkTShape(int x, int y) {
        int sum = board[x][y];

        int wings = 0;
        int minWing = Integer.MAX_VALUE;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            wings++;
            sum += board[nx][ny];
            minWing = Math.min(minWing, board[nx][ny]);
        }

        if (wings >= 3) {
            if (wings == 4) {
                sum -= minWing;
            }
            answer = Math.max(answer, sum);
        }
    }
}