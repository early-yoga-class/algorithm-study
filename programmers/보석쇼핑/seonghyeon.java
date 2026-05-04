import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        Set<String> gemTotal = new HashSet<>(Arrays.asList(gems));
        int totalKinds = gemTotal.size();
        
        Map<String, Integer> gemCnt = new HashMap<>();
        
        int answerLeft = 0;
        int answerRight = gems.length - 1;
        int left = 0, right = 0;
        
        for (; right < gems.length; right++) {
            gemCnt.merge(gems[right], 1, Integer::sum);
            
            while (gemCnt.size() == totalKinds) {
                if (right - left < answerRight - answerLeft) {
                    answerLeft = left;
                    answerRight = right;
                }
                gemCnt.computeIfPresent(gems[left], (k, v) -> v > 1 ? v - 1 : null);
                left++;
            }
        }
        
        return new int[]{answerLeft + 1, answerRight + 1};
    }
}
