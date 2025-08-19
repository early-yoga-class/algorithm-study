import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static List<List<Integer>> g;
    static int[][] dp;

    public static void main(String[] args) throws Exception {
        // 입력 처리: N(정점 수), 트리 간선 정보 입력받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        g = new ArrayList<>(N + 1);
        for (int i = 0; i <= N; i++) g.add(new ArrayList<>());
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g.get(a).add(b);
            g.get(b).add(a);
        }
        // dp 정의: dp[x][0] = x가 얼리어답터가 아닐 때 최소값, dp[x][1] = x가 얼리어답터일 때 최소값
        dp = new int[N + 1][2];
        // 트리 DP를 스택으로 순회하여 계산
        iterativeTreeDP(1);
        // 루트에서 최소 얼리어답터 수 출력
        System.out.println(Math.min(dp[1][0], dp[1][1]));
    }
    // 스택을 이용한 트리 DP 순회
    // 각 노드를 방문 → 자식 노드부터 처리 → dp값 계산
    private static void iterativeTreeDP(int root) {
        Deque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[]{root, 0, 0});
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            int u = cur[0], p = cur[1], processed = cur[2];
            if (processed == 0) {
                // 자식 노드 방문 전: 다시 자신을 스택에 넣고, 자식들을 스택에 추가
                stack.push(new int[]{u, p, 1});
                for (int v : g.get(u)) {
                    if (v == p) continue;
                    stack.push(new int[]{v, u, 0});
                }
            } else {
                // 자식 노드 방문 후: dp값 계산
                int notEA = 0; // u가 얼리어답터가 아닐 때: 자식들은 반드시 얼리어답터
                int isEA = 1;  // u가 얼리어답터일 때: 자식들은 얼리어답터일 수도, 아닐 수도 있음
                for (int v : g.get(u)) {
                    if (v == p) continue;
                    notEA += dp[v][1];
                    isEA  += Math.min(dp[v][0], dp[v][1]);
                }
                dp[u][0] = notEA;
                dp[u][1] = isEA;
            }
        }
    }
}