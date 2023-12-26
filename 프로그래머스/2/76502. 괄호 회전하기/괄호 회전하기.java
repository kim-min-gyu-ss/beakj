import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;
        if (isProper(s)) {
            answer++;
        }
        for (int x = 1; x < s.length(); x++) {
            s = makeString(s);
            if (isProper(s)) {
                answer++;
            }
        }
        return answer;
    }

    private String makeString(String s) {
        return s.substring(1) + s.charAt(0);
    }

    private boolean isProper(String s) { 
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '[' || s.charAt(i) == '(' || s.charAt(i) == '{') {
                stack.push(s.charAt(i));
            } else {
                if (!stack.isEmpty()) {
                    switch (s.charAt(i)) {
                        case ']':
                            checkPeek(stack, '[');
                            break;
                        case ')':
                            checkPeek(stack, '(');
                            break;
                        case '}':
                            checkPeek(stack, '{');
                            break;
                    }
                } else {
                    stack.push(s.charAt(i));
                }
            }
        }
        return stack.isEmpty();
    }
    
    private void checkPeek(Stack<Character> stack, char chr) {
        if (stack.peek() == chr) {
            stack.pop();
        }
    }
}