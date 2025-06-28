import java.io.InputStreamReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        String s = st.nextToken();

        int zeroCount = 0;
        int oneCount = 0;

        List<String> str = Arrays.stream(s.split("")).collect(Collectors.toList());
        List<String> result = new ArrayList<>(str);

        for(int i=0;i<s.length();i++){
            if(str.get(i).equals("0"))
                zeroCount++;
            else if (str.get(i).equals("1")) {
                oneCount++;
            }
        }
        zeroCount/=2;
        oneCount/=2;

        for(int i=0;i<s.length();i++){
            if(str.get(i).equals("1") && oneCount-- != 0){
                result.set(i,"-1");
            }
            if(oneCount == 0)
                break;
        }

        for(int i=s.length()-1;i>=0;i--){
            if(str.get(i).equals("0") && zeroCount-- != 0){
                result.set(i,"-1");
            }
            if(zeroCount==0){
                break;
            }
        }

        for (String string : result) {
            if(string.equals("-1")){
                continue;
            }else{
                System.out.print(string);
            }
        }
    }
}