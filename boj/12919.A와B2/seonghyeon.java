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
            dfs(s.substring(0, s.length() - 1)); // A 제거
        }
        if (s.startsWith("B")) { // 뒤집기 조건 (끝에서 확인했으니 시작도 가능)
            StringBuilder sb = new StringBuilder(s.substring(1));
            dfs(sb.reverse().toString()); // B 제거 후 뒤집기
        }
    }
}