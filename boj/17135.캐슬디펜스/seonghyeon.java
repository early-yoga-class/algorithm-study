import java.io.*;
import java.util.*;

public class Main {
    static int N, M, D;
    static int[][] origin;
    static int best = 0;

    static final int[] dr = {0, -1, 0};
    static final int[] dc = {-1, 0, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());

        origin = new int[N][M];
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < M; c++) {
                origin[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        for (int c1 = 0; c1 < M - 2; c1++) {
            for (int c2 = c1 + 1; c2 < M - 1; c2++) {
                for (int c3 = c2 + 1; c3 < M; c3++) {
                    best = Math.max(best, simulate(c1, c2, c3));
                }
            }
        }

        System.out.println(best);
    }

    static int simulate(int c1, int c2, int c3) {
        int[][] map = copyMap(origin);
        int kill = 0;

        for (int round = 0; round < N; round++) {
            int[][] targets = new int[3][2];
            targets[0] = findTarget(map, c1);
            targets[1] = findTarget(map, c2);
            targets[2] = findTarget(map, c3);

            boolean[][] toRemove = new boolean[N][M];
            for (int[] t : targets) {
                int r = t[0], c = t[1];
                if (r >= 0) toRemove[r][c] = true;
            }
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < M; c++) {
                    if (toRemove[r][c] && map[r][c] == 1) {
                        map[r][c] = 0;
                        kill++;
                    }
                }
            }

            for (int r = N - 1; r >= 1; r--) {
                System.arraycopy(map[r - 1], 0, map[r], 0, M);
            }
            Arrays.fill(map[0], 0);
        }
        return kill;
    }

    static int[] findTarget(int[][] map, int archerCol) {
        boolean[][] visited = new boolean[N][M];
        Deque<Node> q = new ArrayDeque<>();
        if (N - 1 >= 0) {
            q.add(new Node(N - 1, archerCol, 1));
            if(0 <= (N-1) && (N-1) < N && 0 <= archerCol && archerCol < M)
                visited[N - 1][archerCol] = true;
        }

        while (!q.isEmpty()) {
            Node cur = q.poll();
            if (cur.dist > D) break;

            int r = cur.r, c = cur.c;
            if ((0 <= r && r < N && 0 <= c && c < M) && map[r][c] == 1) {
                return new int[]{r, c};
            }

            // 좌, 상, 우 순서로 확장(거리 증가)
            for (int k = 0; k < 3; k++) {
                int nr = r + dr[k];
                int nc = c + dc[k];
                if (!(0 <= nr && nr < N && 0 <= nc && nc < M) || visited[nr][nc]) continue;
                visited[nr][nc] = true;
                q.add(new Node(nr, nc, cur.dist + 1));
            }
        }
        return new int[]{-1, -1};
    }
    static int[][] copyMap(int[][] src) {
        int[][] dst = new int[N][M];
        for (int r = 0; r < N; r++) System.arraycopy(src[r], 0, dst[r], 0, M);
        return dst;
    }

    static class Node {
        int r, c, dist;
        Node(int r, int c, int dist) { this.r = r; this.c = c; this.dist = dist; }
    }
}