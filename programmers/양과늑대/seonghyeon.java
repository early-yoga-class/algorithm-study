import java.util.*;

class Solution {
    int node;
    List<Integer>[] graph;
    int result = 0;
    public int solution(int[] info, int[][] edges) {
        
        int cnt = info.length;
        graph = new ArrayList[cnt];
        for(int i=0;i<cnt;i++){
            graph[i] = new ArrayList<>();
        }
        
        for(int[] edge : edges){
            graph[edge[0]].add(edge[1]);
        }
        
        dfs(info, new State(0, new ArrayList<>(List.of(0)), 0, 0));
        
        return result;
    }
    
    class State{
        int node;
        List<Integer> childs;
        int sheep;
        int wolf;
        
        State(int node, List<Integer> childs, int sheep, int wolf){
            this.node = node;
            this.childs = childs;
            this.sheep = sheep;
            this.wolf = wolf;
        }
    }
    
    private void dfs(int[] info, State state){
        int now = state.node;
        List<Integer> candidate = state.childs;
        int sheep = state.sheep;
        int wolf = state.wolf;
        
        if(info[now] == 0) sheep++;
        else wolf++;
        
        if(sheep <= wolf) return;
        
        result = Math.max(result, sheep);
        
        List<Integer> next = new ArrayList<>(candidate);
        next.remove(Integer.valueOf(now));
        
        for(int child : graph[now]){
            if(info[child] == 1 && graph[child].isEmpty()) continue;
            next.add(child);
        }
        
        for(int nextNode : next){
            dfs(info, new State(nextNode, new ArrayList<>(next), sheep, wolf));
        }
    }
}
