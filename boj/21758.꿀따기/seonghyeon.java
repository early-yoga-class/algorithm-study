import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader bf =  new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(bf.readLine());
        StringTokenizer st = new StringTokenizer(bf.readLine());

        List<Integer> honeies = new ArrayList<>();
        for(int i=0;i<n;i++){
            honeies.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> forwardSum = new ArrayList<>();
        List<Integer> backSum = new ArrayList<>();

        forwardSum.add(honeies.get(0));
        backSum.add(honeies.get(n-1));
        for(int i=1;i<n;i++){
            forwardSum.add(honeies.get(i)+forwardSum.get(i-1));
            backSum.add(honeies.get(n-i-1)+backSum.get(i-1));
        }

        System.out.println(calculateHoney(forwardSum,honeies));
    }

    private static long calculateHoney(List<Integer> prefix, List<Integer> honeies) {
        long total = prefix.get(n - 1);
        long answer = 0L;

        for (int i = 1; i < n - 1; i++) {

            long case1 = total - prefix.get(0) - honeies.get(i)
                    + total - prefix.get(i);

            long case2 = total - honeies.get(n - 1) - honeies.get(i)
                    + prefix.get(i) - honeies.get(i);

            long case3 = (long) prefix.get(i) - honeies.get(0)
                    + prefix.get(n - 2) - prefix.get(i - 1);

            long honey = Math.max(case1, Math.max(case2, case3));
            answer = Math.max(answer, honey);
        }

        return answer;
    }
}
