import java.util.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main {

    public static void main(String[] args) throws IOException{

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<Integer> arr1 = new ArrayList<>();
        List<Integer> arr2 = new ArrayList<>();

        st = new StringTokenizer(bf.readLine());
        for(int i=0;i<n;i++){
            arr1.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(bf.readLine());
        for(int i=0;i<m;i++){
            arr2.add(Integer.parseInt(st.nextToken()));
        }

        arr1.addAll(arr2);
        arr1.sort(Integer::compareTo);

        StringJoiner sj = new StringJoiner(" ");
        for (Integer i : arr1) {
            sj.add(Integer.toString(i));
        }

        System.out.print(sj);
    }
}