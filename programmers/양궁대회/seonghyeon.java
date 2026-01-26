import java.util.List;
import java.util.ArrayList;

class Solution {
    static List<int[]> winCases = new ArrayList<>();
    static int maxDiff = -1;

    public int[] solution(int n, int[] info) {

        int[] lionCase = new int[11];
        backTracking(info, lionCase, n, 0);

        return getBestCase();
    }

    public void backTracking(int[] info, int[] lionCase, int arrowCnt, int idx) {
        if (idx == 11) {
            lionCase[10] = arrowCnt;
            int diff = winner(info, lionCase);
            if (maxDiff < diff) {
                winCases.clear();
                winCases.add(lionCase.clone());
                maxDiff = diff;
            } else if (maxDiff == diff) {
                winCases.add(lionCase.clone());
            }
            lionCase[10] = 0;
            return;
        }
        if (arrowCnt == 0) {
            int diff = winner(info, lionCase);
            if (maxDiff < diff) {
                winCases.clear();
                winCases.add(lionCase.clone());
                maxDiff = diff;
            } else if (maxDiff == diff) {
                winCases.add(lionCase.clone());
            }
            return;
        }

        int needToWin = info[idx] + 1;

        if (arrowCnt >= needToWin) {
            lionCase[idx] = needToWin;
            backTracking(info, lionCase, arrowCnt - needToWin, idx + 1);
            lionCase[idx] = 0;
        }

        backTracking(info, lionCase, arrowCnt, idx + 1);
        return;
    }

    private int winner(int[] info, int[] lionCase) {
        int peach = 0;
        int lion = 0;
        for (int i = 0; i < 11; i++) {
            if (info[i] == 0 && lionCase[i] == 0) {
                continue;
            } else if (info[i] >= lionCase[i]) {
                peach += (10 - i);
            } else {
                lion += (10 - i);
            }
        }

        return lion - peach;
    }

    private int[] getBestCase() {
        if (maxDiff <= 0 || winCases.isEmpty()) {
            return new int[]{-1};
        }

        int[] best = winCases.get(0);

        for (int i = 1; i < winCases.size(); i++) {
            int[] current = winCases.get(i);

            for (int j = 10; j >= 0; j--) {
                if (current[j] > best[j]) {
                    best = current;
                    break;
                } else if (current[j] < best[j]) {
                    break;
                }
            }
        }

        return best;
    }
}