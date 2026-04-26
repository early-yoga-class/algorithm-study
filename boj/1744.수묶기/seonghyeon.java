import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine().trim());

        PriorityQueue<Integer> plusNumbers = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minusNumbers = new PriorityQueue<>();

        for(int i=0;i<n;i++){
            int number = Integer.parseInt(bf.readLine().trim());

            if(number > 0){
                plusNumbers.add(number);
            }else if(number <= 0){
                minusNumbers.add(number);
            }
        }

        int result = 0;

        while(!plusNumbers.isEmpty()){
            int first = plusNumbers.poll();
            if(plusNumbers.isEmpty()){
                result+=first;
                break;
            }
            int second = plusNumbers.poll();
            if(second == 1){
                result+=(first+second);
                continue;
            }
            result+=(first*second);
        }

        while(!minusNumbers.isEmpty()){
            int first = minusNumbers.poll();
            if(minusNumbers.isEmpty()){
                result+=first;
                break;
            }
            int second = minusNumbers.poll();



            result+=(first*second);
        }

        System.out.println(result);
    }
}
