import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        List<Integer> sushiList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            sushiList.add(Integer.parseInt(bf.readLine()));
        }

        Queue<Integer> window = new LinkedList<>();
        Map<Integer, Integer> count = new HashMap<>();

        int kind = 0;

        for (int i = 0; i < k; i++) {
            int sushi = sushiList.get(i);
            window.add(sushi);
            count.put(sushi, count.getOrDefault(sushi, 0) + 1);
            if (count.get(sushi) == 1) {
                 kind++;
            }
        }

        int max = count.containsKey(c) ? kind : kind + 1;

        for (int i = k; i < n + k; i++) {
            int remove = window.poll();
            count.put(remove, count.get(remove) - 1);
            if (count.get(remove) == 0) {
                count.remove(remove);
                kind--;
            }

            int add = sushiList.get(i % n);
            window.add(add);
            count.put(add, count.getOrDefault(add, 0) + 1);
            if (count.get(add) == 1) {
                kind++;
            }

            int current = count.containsKey(c) ? kind : kind + 1;
            max = Math.max(max, current);
        }

        System.out.println(max);
    }
}