import java.util.*;

public class Main {
    static String[] cal = {" ","+", "-"};
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testcase = sc.nextInt();
        int target;
        for(int i=0;i<testcase;i++){
            target = sc.nextInt();
            bruteForce(target);
            System.out.println();
        }
    }
    private static void bruteForce(int target){
        Deque<String> stack = new LinkedList<>();
        stack.push("1");
        backTracking(target, 2,stack);
    }
    private static void backTracking(int target, int num, Deque<String> stack){
        if(num > target){
            calculate(stack);
            return;
        }

        for(int i=0;i<3;i++){
            stack.addLast(cal[i]);
            stack.addLast(Integer.toString(num));
            backTracking(target, num + 1, stack);
            stack.pollLast();
            stack.pollLast();
        }
    }
    private static void calculate(Deque<String> strings){
        List<String> list = new ArrayList<>(strings);
        StringBuilder merged = new StringBuilder();

        for (int i = 0; i < list.size(); i++) {
            merged.append(list.get(i));
        }

        String expr = merged.toString().replaceAll(" ", "");

        List<Integer> nums = new ArrayList<>();
        List<Character> ops = new ArrayList<>();

        int idx = 0;
        while (idx < expr.length()) {
            StringBuilder num = new StringBuilder();
            while (idx < expr.length() && Character.isDigit(expr.charAt(idx))) {
                num.append(expr.charAt(idx));
                idx++;
            }
            nums.add(Integer.parseInt(num.toString()));
            if (idx < expr.length()) {
                ops.add(expr.charAt(idx));
                idx++;
            }
        }

        int result = nums.get(0);
        for (int i = 0; i < ops.size(); i++) {
            if (ops.get(i) == '+') {
                result += nums.get(i + 1);
            } else if (ops.get(i) == '-') {
                result -= nums.get(i + 1);
            }
        }

        if (result == 0) {
            StringBuilder res = new StringBuilder();
            for (String s : list) {
                res.append(s);
            }
            System.out.println(res.toString().trim());
        }
    }
}