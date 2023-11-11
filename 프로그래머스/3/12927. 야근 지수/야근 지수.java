import java.util.*;
class Solution {
    static PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    public long solution(int n, int[] works) {
        long answer = 0;
        for (int work : works) {
            pq.offer(work);
        }
        while (n > 0 && pq.size() > 0) {
            int tmp = pq.poll();
            tmp--;
            if (tmp > 0) pq.offer(tmp);
            n--;
        }
        while (pq.size() > 0) {
            answer += Math.pow(pq.poll(),2);
        }
        return answer;
    }
}