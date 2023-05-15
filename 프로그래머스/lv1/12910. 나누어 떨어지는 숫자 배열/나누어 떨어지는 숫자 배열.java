import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer;
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int a : arr) {
            if (a % divisor == 0) {
                result.add(a);
            }
        }
        Collections.sort(result);
        if (result.size() == 0) {
            answer = new int[1];
            answer[0] = -1;
        }
        else {
            answer = new int[result.size()];
            for (int i = 0; i < result.size(); i++) {
                answer[i] = result.get(i);
            }
        }
        return answer;
    }
}