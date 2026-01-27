import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Pos{
    int likeCnt, blankCnt;
    int x, y;

    public Pos(int likeCnt, int blankCnt, int x, int y){
        this.likeCnt = likeCnt;
        this.blankCnt = blankCnt;
        this.x = x;
        this.y = y;
    }
}

// 주변에 좋아하는 사람 내림차순, 빈칸 내림차순, 좌표 오름차순
class PosComparator implements Comparator<Pos>{
    @Override
    public int compare(Pos o1, Pos o2) {
        if(o1.likeCnt == o2.likeCnt){
            if (o1.blankCnt == o2.blankCnt){
                if(o1.x == o2.x){
                    return o1.y - o2.y;
                }
                return o1.x - o2.x;
            }
            return o2.blankCnt -o1.blankCnt;
        }
        return o2.likeCnt - o1.likeCnt;
    }
}

public class ch {
    static int[][] board;
    static int N;
    static Map<Integer, int[]> map = new LinkedHashMap<>();
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {-1, 1, 0, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        N = Integer.parseInt(br.readLine());
        board = new int[N][N];

        for(int i = 0; i < N * N; i++){
            st = new StringTokenizer(br.readLine());
            int key = Integer.parseInt(st.nextToken());
            int[] value = new int[4];
            for(int j = 0; j < 4; j++){
                value[j] = Integer.parseInt(st.nextToken());
            }
            map.put(key, value);
        }

        for(int key : map.keySet()){
            solve(key);
        }

        System.out.println(getScore());

    }

    public static void solve(int target){
        PriorityQueue<Pos> pq = new PriorityQueue<>(new PosComparator());

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if (board[i][j] != 0) continue;
                int likeCnt = 0, blankCnt = 0;
                for(int d = 0; d < 4; d++){
                    int nx = dx[d] + i;
                    int ny = dy[d] + j;
                    if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                    if (board[nx][ny] == 0) blankCnt++;
                    else {
                        for(int el : map.get(target)){
                            if(el == board[nx][ny]) {
                                likeCnt++;
                                break;
                            }
                        }
                    }
                }
                pq.add(new Pos(likeCnt, blankCnt, i, j));
            }
        }
        Pos select = pq.poll();
        board[select.x][select.y] = target;
    }

    public static int getScore(){
        int sum = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                int likeCnt = 0;
                for(int d = 0; d < 4; d++){
                    int nx = dx[d] + i;
                    int ny = dy[d] + j;
                    if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
                    if (board[nx][ny] != 0)  {
                        for(int el : map.get(board[i][j])){
                            if(el == board[nx][ny]) likeCnt++;
                        }
                    }
                }
                if (likeCnt != 0) sum += (int) Math.pow(10, likeCnt - 1);
            }
        }
        return sum;
    }
}