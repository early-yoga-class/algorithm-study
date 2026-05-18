import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

class Solution {
    private static final int INF = 1_000_000_000;

    private int n;
    private int m;
    private String[] grid;
    private int elevatorR;
    private int elevatorC;

    private final int[] dr = {-1, 1, 0, 0};
    private final int[] dc = {0, 0, -1, 1};

    public int solution(int h, String[] grid, int[][] panels, int[][] seqs) {
        this.grid = grid;
        this.n = grid.length;
        this.m = grid[0].length();

        findElevator();

        int k = panels.length;

        int[] floors = new int[k];
        int[] rows = new int[k];
        int[] cols = new int[k];

        for (int i = 0; i < k; i++) {
            floors[i] = panels[i][0] - 1;
            rows[i] = panels[i][1] - 1;
            cols[i] = panels[i][2] - 1;
        }

        int[][] gridDistancesFromPanel = new int[k][];
        for (int i = 0; i < k; i++) {
            gridDistancesFromPanel[i] = bfs(rows[i], cols[i]);
        }

        int[][] moveCost = new int[k][k];

        for (int from = 0; from < k; from++) {
            for (int to = 0; to < k; to++) {
                if (from == to) {
                    moveCost[from][to] = 0;
                    continue;
                }

                int targetIndex = rows[to] * m + cols[to];
                int elevatorIndex = elevatorR * m + elevatorC;

                if (floors[from] == floors[to]) {
                    moveCost[from][to] = gridDistancesFromPanel[from][targetIndex];
                } else {
                    int fromToElevator = gridDistancesFromPanel[from][elevatorIndex];
                    int elevatorToTarget = gridDistancesFromPanel[to][elevatorIndex];
                    int floorMove = Math.abs(floors[from] - floors[to]);

                    moveCost[from][to] = fromToElevator + floorMove + elevatorToTarget;
                }
            }
        }

        int[] required = new int[k];

        for (int[] seq : seqs) {
            int before = seq[0] - 1;
            int after = seq[1] - 1;

            required[after] |= 1 << before;
        }

        int maxMask = 1 << k;
        int[][] dp = new int[maxMask][k];

        for (int i = 0; i < maxMask; i++) {
            Arrays.fill(dp[i], INF);
        }

        dp[0][0] = 0;

        for (int mask = 0; mask < maxMask; mask++) {
            for (int last = 0; last < k; last++) {
                if (dp[mask][last] == INF) {
                    continue;
                }

                for (int next = 0; next < k; next++) {
                    int nextBit = 1 << next;

                    if ((mask & nextBit) != 0) {
                        continue;
                    }

                    if ((mask & required[next]) != required[next]) {
                        continue;
                    }

                    int nextMask = mask | nextBit;
                    int nextCost = dp[mask][last] + moveCost[last][next];

                    if (nextCost < dp[nextMask][next]) {
                        dp[nextMask][next] = nextCost;
                    }
                }
            }
        }

        int answer = INF;
        int fullMask = maxMask - 1;

        for (int last = 0; last < k; last++) {
            answer = Math.min(answer, dp[fullMask][last]);
        }

        return answer;
    }

    private void findElevator() {
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r].charAt(c) == '@') {
                    elevatorR = r;
                    elevatorC = c;
                    return;
                }
            }
        }
    }

    private int[] bfs(int startR, int startC) {
        int[] distance = new int[n * m];
        Arrays.fill(distance, INF);

        Queue<int[]> queue = new ArrayDeque<>();

        int startIndex = startR * m + startC;
        distance[startIndex] = 0;
        queue.offer(new int[] {startR, startC});

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int r = current[0];
            int c = current[1];

            int currentIndex = r * m + c;

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m) {
                    continue;
                }

                if (grid[nr].charAt(nc) == '#') {
                    continue;
                }

                int nextIndex = nr * m + nc;

                if (distance[nextIndex] != INF) {
                    continue;
                }

                distance[nextIndex] = distance[currentIndex] + 1;
                queue.offer(new int[] {nr, nc});
            }
        }

        return distance;
    }
}