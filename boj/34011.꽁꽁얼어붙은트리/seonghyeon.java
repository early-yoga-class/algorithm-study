import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main{
    static List<Integer>[] graph;
    static Set<Integer> stopNode = new HashSet<>();
    static int maxNode = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());
        graph = new List[N+1];
        for (int i = 0; i <= N; i++) graph[i] = new ArrayList<>();

        st = new StringTokenizer(bf.readLine());
        for (int i = 1; i < N; i++) {
            int parent = Integer.parseInt(st.nextToken());
            graph[i+1].add(parent);
            graph[parent].add(i+1);
        }

        int[] depth = bfs(N);

        int maxDepth = 0;
        for (int i = 1; i <= N; i++) maxDepth = Math.max(maxDepth, depth[i]);

        int[] count = new int[maxDepth + 1];
        for (int i = 1; i <= N; i++) count[depth[i]]++;

        for (int d = 2; d <= maxDepth; d++) {
            int sum = 0;
            for (int k = d; k <= maxDepth; k += d) {
                sum += count[k];
            }
            maxNode = Math.max(maxNode, 1 + sum);
        }

        System.out.println(maxNode);
    }

    private static int[] bfs(int n){
        int[] depth = new int[n+1];
        Arrays.fill(depth, -1);
        depth[1] = 0;

        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(1);

        while (!queue.isEmpty()){
            int node = queue.poll();
            for (int child : graph[node]) {
                if (depth[child] != -1) continue;
                depth[child] = depth[node] + 1;
                queue.add(child);
            }
        }
        return depth;
    }
}