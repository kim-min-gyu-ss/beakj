import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int answer = -1;
        int leng = s.length();
        String[] words = s.split("");
        Stack<String> stack = new Stack<>();
        for (String word : words) {
            if (!stack.isEmpty() && stack.peek().equals(word)) {
                stack.pop();
            } else {
                stack.push(word);
            }
        }
        answer = stack.isEmpty() ? 1 : 0;

        return answer;
    }
}