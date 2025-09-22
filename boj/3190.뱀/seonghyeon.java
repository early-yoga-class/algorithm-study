import java.util.*;

public class Main {
    static int n;
    static int[][] board;
    static Queue<Cord> directList = new LinkedList<>();

    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Deque<Cord> snake = new LinkedList<>();
        snake.add(new Cord(0,0));

        n = sc.nextInt();
        board = new int[n][n];
        int cnt = sc.nextInt();

        while(cnt > 0){
            int x = sc.nextInt()-1;
            int y = sc.nextInt()-1;
            board[x][y] = 1;
            cnt--;
        }

        cnt = sc.nextInt();
        while(cnt>0) {
            int time = sc.nextInt();
            String direct = sc.next();

            if(direct.equals("D")){
                directList.add(new Cord(time, 1));
            }else{
                directList.add(new Cord(time, -1));
            }

            cnt--;
        }

        board[0][0] = -1;

        cnt = 0;
        int d = 0;
        while(true){
            cnt++;
            Cord now = snake.peek();
            int nx = now.x + dx[d];
            int ny = now.y + dy[d];

            if((nx < 0 || nx >= n) || (ny < 0 || ny >= n) || board[nx][ny] == -1){
                break;
            }
            snake.addFirst(new Cord(nx,ny));
            if(board[nx][ny] == 1){
                board[nx][ny] = -1;
            }else{
                board[nx][ny] = -1;
                Cord tail = snake.pollLast();
                board[tail.x][tail.y] = 0;
            }

            if(!directList.isEmpty() && cnt == directList.peek().x){
                Cord direct = directList.poll();
                int direction = d + direct.y;
                d = (4+direction)%4;
            }
        }

        System.out.println(cnt);
    }

    static class Cord{
        int x;
        int y;

        Cord(int x, int y){
            this.x = x;
            this.y = y;
        }

    }
}
