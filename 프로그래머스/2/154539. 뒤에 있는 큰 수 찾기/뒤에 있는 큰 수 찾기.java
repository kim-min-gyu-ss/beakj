import java.util.*;
class Solution {
    static Stack<Integer> gap = new Stack<>();
    static Stack<Integer> idx = new Stack<>();
    public int[] solution(int[] numbers) {
        int leng = numbers.length;
        int[] answer = new int[leng];
        for (int i = 0; i < leng; i++) {
            if (i == 0) {
                gap.push(numbers[i]);
                idx.push(i);
                continue;
            }
            while (!gap.isEmpty() && numbers[i] > gap.peek()) {
                int tmp_gap = gap.pop();
                int tmp_idx = idx.pop();
                answer[tmp_idx] = numbers[i];    
            }
            gap.push(numbers[i]);
            idx.push(i);
        }
        while (!idx.isEmpty()) {
            int t = idx.pop();
            answer[t] = -1;
        }
        return answer;
    }
}