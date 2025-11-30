import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] arr = new int[2 * N][2];

        for(int i = 0; i < N; i ++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            int TE = Integer.parseInt(st.nextToken());
            int TX = Integer.parseInt(st.nextToken());

            arr[2 * i] = new int[] {TE, 1};
            arr[2 * i + 1] = new int[] {TX, -1};
        }

        Arrays.sort(arr, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o1[0] - o2[0]);

        int sum = 0;
        int max = 0;
        int ans_start = 0, ans_end = 0;

        boolean opened = false;

        int i = 0;
        while(i < 2 * N) {
            int cur_time = arr[i][0];

            while(i < 2 * N && arr[i][0] == cur_time) {
                sum += arr[i][1];
                i++;
            }

            if(sum > max) {
                max = sum;
                ans_start = cur_time;
                opened = true;
            } else if(sum < max && opened) {
                ans_end = cur_time;
                opened = false;
            }
        }

        System.out.println(max);
        System.out.println(ans_start + " " + ans_end);
    }

}