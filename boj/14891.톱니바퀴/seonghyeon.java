import java.io.*;
import java.util.*;

public class Main {
    static final int T = 4;
    static boolean[] visited;
    static int[][] gears = new int[T][8];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < T; i++) {
            String line = br.readLine().trim();
            for (int j = 0; j < 8; j++) {
                gears[i][j] = line.charAt(j) - '0';
            }
        }

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken()) - 1;
            int dir = Integer.parseInt(st.nextToken());
            visited = new boolean[T];
            rotateChain(num, dir);
        }

        int result = 0;
        for (int i = 0; i < T; i++) {
            if (gears[i][0] == 1) {
                result += (1 << i);
            }
        }
        System.out.println(result);
    }

    static void rotateChain(int idx, int dir) {
        visited[idx] = true;

        if (idx > 0 && !visited[idx - 1]) {
            if (gears[idx][6] != gears[idx - 1][2]) {
                rotateChain(idx - 1, -dir);
            }
        }

        if (idx < T - 1 && !visited[idx + 1]) {
            if (gears[idx][2] != gears[idx + 1][6]) {
                rotateChain(idx + 1, -dir);
            }
        }

        rotate(idx, dir);
    }

    static void rotate(int idx, int dir) {
        if (dir == 1) {
            int temp = gears[idx][7];
            for (int i = 7; i > 0; i--) {
                gears[idx][i] = gears[idx][i - 1];
            }
            gears[idx][0] = temp;
        } else {
            int temp = gears[idx][0];
            for (int i = 0; i < 7; i++) {
                gears[idx][i] = gears[idx][i + 1];
            }
            gears[idx][7] = temp;
        }
    }
}