import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static int L;
    public static int C;
    public static char[] array;
    public static String match = "aeiou";
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        array = new char[C];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < C; i++){
            array[i] = st.nextToken().charAt(0);
        }

        Arrays.sort(array);


        Stack<Character> selected = new Stack<>();

        dfs(0, selected, 0);
    }

    public static void dfs(int start, Stack<Character> selected, int cnt){
        if(cnt == L){
            int mCnt = 0;
            for(int i = 0; i < L; i++){
                // 모음이 한개라도 있는지 체크
                if (match.indexOf(selected.get(i)) != -1){
                    mCnt++;
                }
            }
            if (mCnt == 0) return;
            if (L - mCnt > 1){
                StringBuilder sb = new StringBuilder();
                for(int i = 0; i < L; i++){
                    sb.append(selected.get(i));
                }
                System.out.println(sb.toString());
            }
            return;
        }

        for(int i = start; i < C; i++){
            selected.push(array[i]);
            dfs(i + 1, selected, cnt + 1);
            selected.pop();
        }
    }
}