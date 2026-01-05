import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    static int r, c, t;
    static int[][] board;
    static Queue<Dust> queue;
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        t = Integer.parseInt(st.nextToken());

        board = new int[r][c];
        int down = 0;
        for(int i=0;i<r;i++){
            st = new StringTokenizer(bf.readLine());
            for(int j=0;j<c;j++){
                board[i][j] = Integer.parseInt(st.nextToken());
                if(board[i][j] == -1){
                    down = i;
                }
            }
        }
        for(int i=0;i<t;i++){
            dustCheckAndSpread();
            clean(down);
        }
        int sum_dust=0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                sum_dust+=board[i][j];
            }
        }
        System.out.println(sum_dust+2);
    }

    public static void clean(int down){
        int up=down-1;

        for(int i=up-1;i>0;i--){
            board[i][0]=board[i-1][0];
        }
        for(int i=0;i<c-1;i++){
            board[0][i]=board[0][i+1];
        }
        for(int i=0;i<up;i++){
            board[i][c-1]=board[i+1][c-1];
        }
        for(int i=c-1;i>1;i--){
            board[up][i]=board[up][i-1];
        }
        board[up][1]=0;
        for(int i=down+1;i<r-1;i++){
            board[i][0]=board[i+1][0];
        }
        for(int i=0;i<c-1;i++){
            board[r-1][i]=board[r-1][i+1];
        }
        for(int i=r-1;i>down;i--){
            board[i][c-1]=board[i-1][c-1];
        }
        for(int i=c-1;i>1;i--){
            board[down][i]=board[down][i-1];
        }
        board[down][1]=0;
    }

    private static void dustCheckAndSpread(){
        queue = new LinkedList<>();
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(board[i][j] != 0 && board[i][j] != -1){
                    queue.add(new Dust(i,j, board[i][j]));
                }
            }
        }

        while(!queue.isEmpty()){
            Dust dust = queue.poll();
            dust.spread();
        }
    }

    private static class Dust{
        int x;
        int y;
        int amount;

        public Dust(int x, int y, int amount){
            this.x = x;
            this.y = y;
            this.amount = amount;
        }

        public void spread(){
            int[] dx = {1,0,-1,0};
            int[] dy = {0,1,0,-1};
            int spreadAmount = amount / 5;
            for(int i=0;i<4;i++){
                int nx = x+dx[i];
                int ny = y+dy[i];

                if(nx>=0 && nx<r && ny>=0 && ny<c && board[nx][ny] != -1){
                    board[nx][ny] += spreadAmount;
                    board[x][y] -= spreadAmount;
                }
            }
        }
    }
}