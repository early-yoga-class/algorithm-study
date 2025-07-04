import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        while(true){
            Integer count = Integer.parseInt(st.nextToken());
            if(count == 0){
                break;
            }
            List<String> numList = new ArrayList<>();

            while(st.hasMoreTokens()){
                numList.add(st.nextToken());
            }
            backTracking(new ArrayList<>(), 0, numList);
            System.out.println();
            st = new StringTokenizer(bf.readLine());
        }
    }
    private static void backTracking(List<String> result, int start, List<String> list) {
        if (result.size() == 6) {
            System.out.println(String.join(" ", result));
            return;
        }
        for (int i = start; i < list.size(); i++) {
            result.add(list.get(i));
            backTracking(result, i + 1, list);
            result.remove(result.size() - 1);
        }
    }
}