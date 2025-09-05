import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.Comparable;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int N = Integer.parseInt(st.nextToken());
        PriorityQueue<Number> queue = new PriorityQueue<>();
        int command = 0;
        for(int i=0;i<N;i++){
            st = new StringTokenizer(bf.readLine());
            command = Integer.parseInt(st.nextToken());

            if(command == 0){
                try{
                    Number num = queue.poll();
                    System.out.println(num.value);
                }catch(NullPointerException e){
                    System.out.println(0);
                }
            }else{
                queue.add(new Number(command));
            }
        }
    }

    static class Number implements Comparable<Number> {
        int value;
        int absValue;

        Number(int value){
            this.value = value;
            this.absValue = Math.abs(value);
        }

        @Override
        public int compareTo(Number o){
            if(this.absValue < o.absValue){
                return -1;
            }else if(this.absValue == o.absValue){
                if(this.value < o.value){
                    return -1;
                }else if(this.value>=o.value){
                    return 1;
                }
            }else{
                return 1;
            }
            return 0;
        }

    }
}