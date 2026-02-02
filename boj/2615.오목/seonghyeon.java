import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int[][] board = new int[20][20];
    static int[] dx = {0,1,1,1,0,-1,-1,-1};
    static int[] dy = {1,1,0,-1,-1,-1,0,1};
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        for(int i=1;i<20;i++){
            st = new StringTokenizer(bf.readLine());
            for(int j=1;j<20;j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result;
        for(int i=1;i<20;i++){
            for(int j=1;j<20;j++){
                if(board[i][j] != 0){
                    result = checkWin(i,j, board[i][j]);
                    if(result != 0) {
                        System.out.println(result);
                        System.out.println(i + " " + j);
                        return;
                    }
                }
            }
        }
        System.out.println(0);
    }

    public static int checkWin(int x, int y, int color){
        int result = 0;

        for(int i=0;i<8;i++){
            int colorCnt = 1;
            if(i==3) continue;
            for(int j=1;j<6;j++){
                int nx = x + (dx[i] * j);
                int ny = y + (dy[i] * j);

                if(nx>=1&&nx<20&&ny>=1&&ny<20){
                    int nextColor = board[nx][ny];
                    if(nextColor==color) colorCnt++;
                    if(nextColor!=color && j<5) break;
                }
            }
            if(colorCnt == 5) {
                int tempX = x + dx[(i+4) % 8];
                int tempY = y + dy[(i+4) % 8];
                if(tempX >=0 && tempY>=0 && tempY<20 && tempX<20 && board[tempX][tempY] != color){
                    return color;
                }
            }
        }
        return result;
    }
}
