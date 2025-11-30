import java.util.*;

public class Main {
    static boolean result = false;
    static String start, target;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        start = sc.next();
        target = sc.next();

        dfs(target);
        System.out.println(result ? 1 : 0);
    }

    static void dfs(String s) {
        if (s.length() == start.length()) {
            if (s.equals(start)) result = true;
            return;
        }
        if (s.endsWith("A")) {
            dfs(s.substring(0, s.length() - 1));
        }
        if (s.startsWith("B")) {
            StringBuilder sb = new StringBuilder(s.substring(1));
            dfs(sb.reverse().toString());
        }
    }
}