import java.io.*;
import java.util.*;

public class Main {

    static int n, m;
    static int[] gender;
    static int[] parent;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        gender = new int[n + 1];
        parent = new int[n + 1];

        for (int i = 1; i <= n; i++) parent[i] = i;

        st = new StringTokenizer(bf.readLine());
        for (int i = 1; i <= n; i++) {
            if (st.nextToken().equals("M")) gender[i] = 1;
            else gender[i] = 0;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(bf.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            if (gender[u] == gender[v]) continue;

            pq.add(new Edge(u, v, d));
        }

        int sum = 0;
        int pick = 0;

        while (!pq.isEmpty()) {
            Edge e = pq.poll();

            if (find(e.u) != find(e.v)) {
                union(e.u, e.v);
                sum += e.w;
                pick++;

                if (pick == n - 1) break;
            }
        }

        if (pick == n - 1) System.out.println(sum);
        else System.out.println(-1);
    }

    static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) parent[b] = a;
    }

    static class Edge implements Comparable<Edge> {
        int u, v, w;

        Edge(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

        @Override
        public int compareTo(Edge o) {
            return this.w - o.w;
        }
    }
}