import java.util.Scanner;

public class Main {
    static int x;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        x = sc.nextInt();

        int totalLen = 64; // 막대기 길이 총 합
        int shortestStick = 64; // 현재 가장 짧은 막대기 길이
        int cnt = 1; // 막대기 개수

        while(totalLen > x){
            cnt--; // 가장 짧은 막대기 제거
            int tempStickLen = shortestStick/2; // 새롭게 만들 가장 짧은 막대기 길이 구하기
            shortestStick = tempStickLen; // 짧은 막대기 길이 업데이트
            if((totalLen - tempStickLen) >= x){
                totalLen -= tempStickLen; // 가장 짧은 막대기 한 개 제외
                cnt+=1; // 하나 버렸으므로 한 개만 더하기
            }else{
                cnt+=2; // 버리는 막대기 없으므로 두 개 더하기
            }
        }

        System.out.println(cnt);
    }
}