import java.util.*;

class Solution {

    int answer = Integer.MAX_VALUE;

    public int solution(int n, int[] weak, int[] dist) {

        int w = weak.length;

        int[] newWeak = new int[w * 2];
        for (int i = 0; i < w; i++) {
            newWeak[i] = weak[i];
            newWeak[i + w] = weak[i] + n;
        }

        boolean[] visited = new boolean[dist.length];

        for (int start = 0; start < w; start++) {
            dfs(newWeak, dist, start, start + w, 0, visited);
        }

        return answer == Integer.MAX_VALUE ? -1 : answer;
    }

    public void dfs(int[] weak, int[] dist, int start, int end, int friendCount, boolean[] visited) {

        if (start >= end) {
            answer = Math.min(answer, friendCount);
            return;
        }
        if (friendCount >= dist.length || friendCount >= answer) return;

        for (int i = 0; i < dist.length; i++) {
            if (visited[i]) continue;

            visited[i] = true;

            int coverage = weak[start] + dist[i];
            int next = start;

            while (next < end && weak[next] <= coverage) next++;

            dfs(weak, dist, next, end, friendCount + 1, visited);

            visited[i] = false;
        }
    }
}