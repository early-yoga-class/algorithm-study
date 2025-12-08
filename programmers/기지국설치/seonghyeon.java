class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int coverLength = 2 * w + 1;

        int start = 1;

        for (int station : stations) {
            int left = station - w;
            int right = station + w;

            if (start < left) {
                int length = left - start;
                answer += (length + coverLength - 1) / coverLength;
            }

            start = right + 1;
        }

        if (start <= n) {
            int length = n - start + 1;
            answer += (length + coverLength - 1) / coverLength;
        }

        return answer;
    }
}