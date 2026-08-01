import java.util.Scanner;
import java.io.FileInputStream;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    board[i][j] = sc.nextInt();

            int result = -1;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    result = Math.max(result, plusBfs(board, m, i, j));
                    result = Math.max(result, multiBfs(board, m, i, j));
                }
            }
            System.out.println("#"+test_case+ " " +result); 
        }
    } 

    static int plusBfs(int[][] board, int m, int i, int j) {
        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int size = board.length;
        int calculate = board[i][j];
        for (int idx = 0; idx < 4; idx++) {
            for (int mul = 1; mul < m; mul++) { 
                int nx = i + dx[idx] * mul;
                int ny = j + dy[idx] * mul;
                if (nx < 0 || nx >= size || ny < 0 || ny >= size) continue;
                calculate += board[nx][ny];
            }
        }
        return calculate;
    }

    static int multiBfs(int[][] board, int m, int i, int j) {
        int[] dx = {1, -1, -1, 1};
        int[] dy = {-1, -1, 1, 1};
        int size = board.length;
        int calculate = board[i][j];
        for (int idx = 0; idx < 4; idx++) {
            for (int mul = 1; mul < m; mul++) {
                int nx = i + dx[idx] * mul;
                int ny = j + dy[idx] * mul;
                if (nx < 0 || nx >= size || ny < 0 || ny >= size) continue;
                calculate += board[nx][ny];
            }
        }
        return calculate;
    }
}  
