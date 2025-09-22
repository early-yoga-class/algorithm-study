import java.util.*;

public class Main {
    static int n;
    static int[][] board; // 뱀 : -1, 사과 : 1
    static Queue<Cord> directList = new LinkedList<>(); // 뱡향 전환 정보 리스트

    static int[] dx = {0,1,0,-1};
    static int[] dy = {1,0,-1,0};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Deque<Cord> snake = new LinkedList<>(); // 뱀 몸통 좌표 리스트 -> 머리 위치 추적용
        snake.add(new Cord(0,0));

        n = sc.nextInt();
        board = new int[n][n];
        int cnt = sc.nextInt();

        while(cnt > 0){
            int x = sc.nextInt()-1;
            int y = sc.nextInt()-1;
            board[x][y] = 1; // 사과 위치
            cnt--;
        }

        cnt = sc.nextInt();
        // 방향 전환 정보 저장
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

        board[0][0] = -1; // 뱀 몸통 표시

        cnt = 0;
        int d = 0;
        while(true){
            cnt++;
            Cord now = snake.peek(); // 현재 뱀 머리 위치
            // 다음 뱀 머리 위치
            int nx = now.x + dx[d];
            int ny = now.y + dy[d];

            // 범위 밖 or 뱀 몸통 충돌 확인
            if((nx < 0 || nx >= n) || (ny < 0 || ny >= n) || board[nx][ny] == -1){
                break;
            }
            snake.addFirst(new Cord(nx,ny)); // 머리 이동
            if(board[nx][ny] != 1){
                Cord tail = snake.pollLast();
                board[tail.x][tail.y] = 0;
            }
            board[nx][ny] = -1; // 뱀 좌표 업데이트

            // 방향 전환
            if(!directList.isEmpty() && cnt == directList.peek().x){
                Cord direct = directList.poll();
                int direction = d + direct.y;
                d = (4+direction)%4;
            }
        }

        System.out.println(cnt);
    }

    // 죄표 값 클래스
    static class Cord{
        int x;
        int y;

        Cord(int x, int y){
            this.x = x;
            this.y = y;
        }

    }
}
