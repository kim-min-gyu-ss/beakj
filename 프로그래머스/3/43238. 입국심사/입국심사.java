import java.util.*;

public class Solution {
    public long solution(int n, int[] times) {
        int length = times.length;
        Arrays.sort(times);

        long maxTime = (long) times[length - 1] * n; 
        long minTime = 1; 
        long answer = maxTime; 

        while (minTime <= maxTime) {
            long averageTime = (minTime + maxTime) / 2;
            long tmp_n = 0;

            for (int i = 0; i < length; i++) {
                tmp_n += averageTime / times[i];
                if (tmp_n >= n) break; 
            }

            if (tmp_n < n) {
                minTime = averageTime + 1;
            } else {
                answer = Math.min(answer, averageTime);
                maxTime = averageTime - 1;
            }
        }

        return answer;
    }
}
