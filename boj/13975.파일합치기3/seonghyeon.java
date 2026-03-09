import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer  st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());

        for(int i=0;i<t;i++){
            st = new StringTokenizer(br.readLine());
            int k =  Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            PriorityQueue<Long> naturalOrder = new PriorityQueue<>();
            for(int j=0;j<k;j++){
                Long num = Long.parseLong(st.nextToken());
                naturalOrder.add(num);
            }
            Long result = 0L;
            while(naturalOrder.size() > 1){
                Long file1 = naturalOrder.poll();
                Long file2 = naturalOrder.poll();

                result += (file1+file2);
                naturalOrder.add((file1+file2));
            }

            System.out.println(result);
        }
    }
}