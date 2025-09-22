import java.util.Scanner;

public class Main {
    static int x;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        x = sc.nextInt();

        int totalLen = 64;
        int shortestStick = 64;
        int cnt = 1;

        while(totalLen > x){
            int tempStickLen = shortestStick/2;
            cnt--;
            if((totalLen - tempStickLen) >= x){
                totalLen -= tempStickLen;
                shortestStick = tempStickLen;
                cnt+=1;
            }else{
                shortestStick = tempStickLen;
                cnt+=2;
            }
        }

        System.out.println(cnt);
    }
}