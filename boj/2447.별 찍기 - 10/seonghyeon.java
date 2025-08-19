import java.io.*;
import java.util.*;

public class Main {
    static char[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        board = new char[N][N];
        for (int i = 0; i < N; i++) Arrays.fill(board[i], ' ');

        draw(0, 0, N);

        StringBuilder sb = new StringBuilder(N * (N + 1));
        for (int i = 0; i < N; i++) {
            sb.append(board[i]).append('\n');
        }
        System.out.print(sb);
    }

    static void draw(int r, int c, int n) {
        if (n == 1) {
            board[r][c] = '*';
            return;
        }
        int size = n / 3;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 1 && j == 1) continue;
                draw(r + i * size, c + j * size, size);
            }
        }
    }
}