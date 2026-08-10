import java.util.Arrays;

class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);
        
        int answer = 0;
        int idx = 0;
        
        for (int i = 0; i < B.length; i++) {
            if (B[i] > A[idx]) {
                answer++;
                idx++;
            }
        }
        
        return answer;
    }
}
