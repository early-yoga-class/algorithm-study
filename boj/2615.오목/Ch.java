import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int[][] board = new int[19][19];
    static boolean[][] checked = new boolean[19][19];
    // 북쪽부터 시계방향 탐색
    static int[] dx = {0, 1, 1, -1};
    static int[] dy = {1, 0, 1, 1};
    static int ans = 0;
    static int[] pos = new int[2];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        // 검은색 승 1, 흰색 승 2, 진행중 0
        for(int i = 0; i < 19; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 19; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // 예외처리 = 6개 이상이면 이긴 것이 아니다.
        outer: for(int i = 0; i < 19; i++){
            for(int j = 0; j < 19; j++) {
                if (board[i][j] == 0) continue;
                // 검은색 1, 흰색 2
                int currentColor = board[i][j];
                for(int d = 0; d < 4; d++){
                    int nx = i + dx[d];
                    int ny = j + dy[d];
                    if(nx < 0 || ny < 0 || nx >= 19 || ny >= 19) continue;
                    if(board[nx][ny] == 0) continue;

                    int count = 1;
                    int curX = nx;
                    int curY = ny;
                    while(true){
                        if(curX < 0 || curY < 0 || curX >= 19 || curY >= 19) break;
                        if(board[curX][curY] != currentColor) break;
                        count++;
                        curX = curX + dx[d];
                        curY = curY + dy[d];
                    }

                    if (count == 5){
                        int bx = i - dx[d];
                        int by = j - dy[d];
                        if (bx < 0 || by < 0 || bx >= 19 || by >= 19 || board[bx][by] != currentColor) {
                            ans = currentColor;
                            pos[0] = i + 1;
                            pos[1] = j + 1;
                            break outer;
                        }
                    }
                }
            }
        }

        if(ans != 0){
            System.out.println(ans);
            System.out.println(pos[0] + " " + pos[1]);
        }else{
            System.out.println(ans);
        }
    }
}