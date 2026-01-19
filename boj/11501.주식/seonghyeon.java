import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

import java.util.PriorityQueue;
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Map;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int testCase = Integer.parseInt(st.nextToken());

        for(int i=0;i<testCase;i++) {
            long result = 0L;
            st = new StringTokenizer(bf.readLine());
            int len = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(bf.readLine());

            List<Integer> origin = new ArrayList<>();

            for(int j=0;j<len;j++) {
                int price = Integer.parseInt(st.nextToken());
                origin.add(price);
            }


            int maxStockPrice = 0;
            for(int j=len-1;j>=0;j--) {
                int stock = origin.get(j);
                if(stock > maxStockPrice) {
                    maxStockPrice = stock;
                }else {
                    result += (maxStockPrice - stock);
                }
            }
            System.out.println(result);
        }
    }
}