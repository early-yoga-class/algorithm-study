import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine().trim());

        N = Integer.parseInt(st.nextToken());
        List<List<Integer>> inGraph = new ArrayList<>();
        List<List<Integer>> outGraph = new ArrayList<>();
        List<Job> jobList = new ArrayList<>();

        inGraph.add(new ArrayList<>());
        outGraph.add(new ArrayList<>());
        jobList.add(new Job(0, 0));

        for (int i = 1; i <= N; i++) {
            inGraph.add(new ArrayList<>());
            outGraph.add(new ArrayList<>());
        }

        int[] inDegreeCount = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(bf.readLine());
            int work = Integer.parseInt(st.nextToken());
            int beforeJobCount = Integer.parseInt(st.nextToken());
            inDegreeCount[i] = beforeJobCount;
            jobList.add(new Job(i, work));

            for (int j = 0; j < beforeJobCount; j++) {
                int in = Integer.parseInt(st.nextToken());
                inGraph.get(i).add(in);
                outGraph.get(in).add(i);
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (inDegreeCount[i] == 0) {
                queue.add(i);
                jobList.get(i).calculateEndTime(0);
            }
        }

        while (!queue.isEmpty()) {
            int jobIdx = queue.poll();
            List<Integer> outDegree = outGraph.get(jobIdx);

            for (Integer out : outDegree) {
                inDegreeCount[out]--;

                int latestStartTime = -1;
                for (Integer in : inGraph.get(out)) {
                    latestStartTime = Math.max(latestStartTime, jobList.get(in).endWorkTime);
                }
                jobList.get(out).calculateEndTime(latestStartTime);

                if (inDegreeCount[out] == 0) {
                    queue.add(out);
                }
            }
        }

        int answer = 0;
        for (int i = 1; i <= N; i++) {
            answer = Math.max(answer, jobList.get(i).endWorkTime);
        }

        System.out.println(answer);
    }

    private static class Job {
        int index;
        int workTime;
        int endWorkTime = 0;

        Job(int idx, int time) {
            this.index = idx;
            this.workTime = time;
        }

        public void calculateEndTime(int startTime) {
            this.endWorkTime = startTime + this.workTime;
        }
    }
}