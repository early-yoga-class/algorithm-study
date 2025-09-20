import java.io.*;
import java.util.*;

public class Main {
    static int N, K;
    static int zeroCnt = 0;
    static LinkedList<Integer> belts = new LinkedList<>();
    static LinkedList<Integer> robots = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 2 * N; i++) {
            belts.add(Integer.parseInt(st.nextToken()));
        }

        int level = 0;
        while (zeroCnt < K) {
            level++;

            // 1. 벨트 회전 + 로봇 이동
            belts.addFirst(belts.removeLast());
            for (int i = 0; i < robots.size(); i++) {
                int newPos = (robots.get(i) + 1) % (2 * N);
                robots.set(i, newPos);
            }

            robots.removeIf(pos -> pos == N - 1);

            // 2. 로봇 이동 (뒤에서부터)
            for (int i = 0; i < robots.size(); i++) {
                int pos = robots.get(i);
                int next = (pos + 1) % (2 * N);

                if (!robots.contains(next) && belts.get(next) > 0) {
                    robots.set(i, next);
                    belts.set(next, belts.get(next) - 1);
                    if (belts.get(next) == 0) zeroCnt++;
                }
            }
            robots.removeIf(pos -> pos == N - 1);

            // 3. 올리는 위치
            if (belts.get(0) > 0) {
                robots.add(0);
                belts.set(0, belts.get(0) - 1);
                if (belts.get(0) == 0) zeroCnt++;
            }
        }
        System.out.println(level);
    }
}