import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int tmp = 0;
        Arrays.sort(d);
        for (int item : d) {
            if ((tmp + item) <= budget) {
                tmp += item;
                answer++;
            }
            else continue;
        }
        return answer;
    }
}