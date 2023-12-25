import java.util.*;
class Solution {
    PriorityQueue<Integer> mnq = new PriorityQueue<>();
    PriorityQueue<Integer> mxq = new PriorityQueue<>(Collections.reverseOrder());
    public int[] solution(String[] operations) {
        for (String str : operations) {
            String[] split_str = str.split(" ");
            if (split_str[0].equals("I")) {
                mnq.offer(Integer.parseInt(split_str[1]));
                mxq.offer(Integer.parseInt(split_str[1]));
            } else if (mnq.size() == 0) continue;
            else if (split_str[1].equals("1")) {
                int tmp = mxq.poll();
                mnq.remove(tmp);
            } else {
                int tmp = mnq.poll();
                mxq.remove(tmp);
            }
        }
        int[] answer = mnq.size() == 0 ? new int[] {0,0} : new int[] {mxq.poll(), mnq.poll()};
        return answer;
    }
}