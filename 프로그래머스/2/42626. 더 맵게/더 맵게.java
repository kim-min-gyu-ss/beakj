import java.util.*;
class Solution {
    static int mx;
    static PriorityQueue<Integer> pq = new PriorityQueue<>();
    public int solution(int[] scoville, int K) {
        int answer = 0;
        mx = 0;
        for (int sc : scoville) {
            pq.offer(sc);
            mx = Math.max(mx, sc);
        }
        while(pq.peek() < K) {
            int fst = pq.poll();
            int scd = pq.poll();
            if (fst >= scd) {
                pq.offer(scd + 2 * fst);
            } else {
                pq.offer(fst + 2 * scd);
            }
            answer++;
            if (pq.size() == 1 && pq.peek() < K) {
                answer = -1;
                break;
            }
        }  
        return answer;
    }
}