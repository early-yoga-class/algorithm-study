import java.util.*;

class Solution {

    public int solution(int[] players, int m, int k) {
        int answer = 0;

        int[] expire = new int[24 + k + 1];

        int activeServers = 0;

        for (int hour = 0; hour < 24; hour++) {

            activeServers -= expire[hour];

            int requiredServers = players[hour] / m;

            if (requiredServers > activeServers) {
                int needToAdd = requiredServers - activeServers;

                answer += needToAdd;
                activeServers += needToAdd;

                expire[hour + k] += needToAdd;
            }
        }

        return answer;
    }
}