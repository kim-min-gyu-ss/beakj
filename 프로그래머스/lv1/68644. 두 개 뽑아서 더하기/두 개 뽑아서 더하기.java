import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.length - 1; i ++) {
            for (int j = i+1; j < numbers.length; j ++) {
                int tmp = numbers[i] + numbers[j];
                if (!result.contains(tmp)) {
                    result.add(tmp);
                }
            }
        }
        Collections.sort(result);
        int[] answer = new int[result.size()];
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}