import java.util.*;

class Solution {
    static Queue<Integer> q = new LinkedList<>();
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        for (int price : prices) {
            q.offer(price);
        }

        int idx = 0;
        while (q.size() > 0) {
            int gap = q.poll();

            answer[idx] = 0;

            for (Integer num : q) {
                answer[idx]++;
                if (gap > num) {
                    break;
                }
            }

            idx++;
        }

        return answer;
    }
}