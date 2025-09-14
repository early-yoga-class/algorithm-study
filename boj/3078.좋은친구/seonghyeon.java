import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main{
    static int N, K;
    static Queue<String> queue = new LinkedList<>();
    static HashMap<Integer, Integer> map = new HashMap<>();
    static long result =0;
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        String name;

        for(int i=2;i<21;i++){
            map.put(i, 0);
        }

        for(int i=0;i<N;i++){
            st = new StringTokenizer(bf.readLine());
            name = st.nextToken();

            if(queue.size() == (K+1)){
                String pollName = queue.poll();
                map.replace(pollName.length(), map.get(pollName.length())-1);
            }
            queue.add(name);
            int len = name.length();
            result+=map.get(len);
            map.replace(len, map.get(len)+1);
        }
        System.out.println(result);
    }
}