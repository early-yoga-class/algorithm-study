import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<Integer> primeNumbers = new ArrayList<>();
        // 아리스머시기 체
        boolean[] visited = new boolean[n+1];

        for(int i=2;i<=n;i++){
            if(visited[i]) continue;
            primeNumbers.add(i);

            for(int j=i*2;j<=n;j+=i){
                visited[j] = true;
            }
        }

        // 투 포인터
        int left = 0;
        int right = 0;
        int count = 0;
        if(n == 1){
            System.out.println(0);
            return;
        }
        int sum = primeNumbers.get(0);

        while(left < primeNumbers.size()){
            if(sum == n) {
                count++;
                sum-=primeNumbers.get(left++);
            }else if(sum < n){
                right++;
                if(right == primeNumbers.size()) break;
                sum+=primeNumbers.get(right);
            }else{
                sum-=primeNumbers.get(left++);
            }
        }
        System.out.println(count);
    }
}