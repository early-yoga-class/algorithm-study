import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int[][] map;
    static List<Tv> list = new ArrayList<>();
    static int N, M;
    static int minValue = Integer.MAX_VALUE;
    static int[][][] cctvDir = {
            {},
            {{0},{1},{2},{3}},
            {{0, 2},{1, 3}},
            {{0, 1},{1, 2}, {2, 3},{3, 0}},
            {{0, 1, 2}, {1, 2, 3}, {2, 3, 0},{3, 0, 1}},
            {{0, 1, 2, 3}}
    };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == 0) cnt++;
                if (map[i][j] != 0 && map[i][j] != 6) {
                    list.add(new Tv(map[i][j], i,j));
                }
            }
        }

        bruteForce(0,cnt);

        System.out.println(minValue);
    }

    private static void bruteForce(int depth, int cnt) {
        if (depth >= list.size()) {
            minValue = Math.min(minValue, cnt);
            return;
        }

        Tv tv = list.get(depth);
        for (int i = 0; i < cctvDir[tv.num].length; i++) {
            int temp = tv.watch(i);
            bruteForce(depth+1, cnt-temp);
            tv.unWatch(i);
        }
    }

    static class Tv {
        int num;
        int x, y;
        int[][] dir = {{-1,0},{0,1},{1,0},{0,-1}};

        Tv(int num,int x,int y) {
            this.num = num;
            this.x = x;
            this.y = y;
        }

        public int watch(int direction){
            int count = 0;

            for (int d : cctvDir[num][direction]) {
                int nx = this.x;
                int ny = this.y;

                while (true) {
                    nx += dir[d][0];
                    ny += dir[d][1];

                    if (nx < 0 || ny < 0 || nx >= N || ny >= M) break;
                    if (map[nx][ny] == 6) break;

                    if (map[nx][ny] <= 0) {
                        if(map[nx][ny] == 0) count++;
                        map[nx][ny]--; // 감시 표시

                    }
                }
            }

            return count;
        }

        public void unWatch(int direction){
            for (int d : cctvDir[num][direction]) {
                int nx = this.x;
                int ny = this.y;

                while (true) {
                    nx += dir[d][0];
                    ny += dir[d][1];

                    if (nx < 0 || ny < 0 || nx >= N || ny >= M) break;
                    if (map[nx][ny] == 6) break;

                    if (map[nx][ny] < 0) {
                        map[nx][ny]++;
                    }
                }
            }
        }
    }

}
