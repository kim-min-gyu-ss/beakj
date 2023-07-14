import java.util.*;
class Solution {
    public String solution(int[] food) {
        String answer = "";
        String result = "";
        for (int i = 1; i < food.length; i++) {
            int tmp = (int)Math.floor(food[i]/2);
            for (int j = 0; j < tmp; j++) {
                result += i;
            }
        }
        result += 0;
        answer = result;
        for (int i = answer.length() - 2; i > -1; i--) {
            answer += result.charAt(i);
        }
        System.out.println(answer);
        return answer;
    }
}