import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class CCTV {
    int x, y, type;

    public CCTV(int x, int y, int type){
        this.x = x;
        this.y = y;
        this.type = type;
    }
}

public class Ch {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    // 1 <= N, M <= 8
    static int N, M;
    static int[][] board;
    static int ans = Integer.MAX_VALUE;
    static Map<Integer, String[]> checked = new HashMap<>();
    // 벽 통과 불가능, cctv끼리 통과 가능
    static ArrayList<CCTV> cctvs = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++){
                board[i][j] = Integer.parseInt(st.nextToken());
                if(board[i][j] > 0 && board[i][j] < 6){
                    cctvs.add(new CCTV(i, j, board[i][j]));
                }
            }
        }
        initDir();
        backtracking(0);

        System.out.println(ans);
    }

    public static void initDir(){
        checked.put(1, new String[]{"0", "1", "2", "3"});
        checked.put(2, new String[]{"02", "13"});
        checked.put(3, new String[]{"01", "12", "23", "30"});
        checked.put(4, new String[]{"012", "123", "230", "301"});
        checked.put(5, new String[]{"0123"});
    }

    public static int getBlindArea(){
        int sum = 0;
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if (board[i][j] == 0) sum++;
            }
        }
        return sum;
    }

    public static void start(int cctvNum, String str){
        CCTV cctv = cctvs.get(cctvNum);
        for(int d = 0; d < str.length(); d++){
            int nx = cctv.x;
            int ny = cctv.y;
            int dir = str.charAt(d) - '0';

            while(true){
                nx += dx[dir];
                ny += dy[dir];
                if(nx < 0 || ny < 0 || nx >= N || ny >= M) break;
                if(board[nx][ny] == 6) break;

                if(board[nx][ny] <= 0){
                    board[nx][ny] -= 1;
                }
            }
        }
    }

    public static void end(int cctvNum,  String str){
        CCTV cctv = cctvs.get(cctvNum);

        for(int d = 0; d < str.length(); d++){
            int nx = cctv.x;
            int ny = cctv.y;
            int dir = str.charAt(d) - '0';

            while(true){
                nx += dx[dir];
                ny += dy[dir];
                if(nx < 0 || ny < 0 || nx >= N || ny >= M) break;
                if(board[nx][ny] == 6) break;

                if(board[nx][ny] < 0){
                    board[nx][ny] += 1;
                }
            }
        }
    }

    public static void backtracking(int count){
        if(count == cctvs.size()){
            int blindSpots = getBlindArea();
            if(ans > blindSpots){
                ans = blindSpots;
            }
            return;
        }

        CCTV current = cctvs.get(count);
        String[] dirs = checked.get(current.type);

        for (String dir : dirs) {
            start(count, dir);
            backtracking(count + 1);
            end(count, dir);
        }
    }
}