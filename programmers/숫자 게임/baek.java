import java.io.*;
import java.util.*;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        int idx = 0;

        for (int i=0; i<A.length; i++){
            while (B[idx]<=A[i] && idx!= A.length-1){
                idx++;
            }
                
            if (A[i]<B[idx]){
                answer++;
                idx++;
                if (idx == A.length){
                    return answer;
                }
            }
        }      
        return answer;
    }
}

// 어차피 최대 승점만 리턴하면 되므로 출전순서는 상관 없음. 둘다 sort하자
