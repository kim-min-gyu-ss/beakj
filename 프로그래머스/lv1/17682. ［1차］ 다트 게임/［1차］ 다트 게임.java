import java.util.*;
class Solution {
    
    static Stack<Integer> stack;
    
    public int solution(String dartResult) {
        stack = new Stack<>();
        int answer = 0;
        String sttmp = "";
        String[] list = dartResult.split("");
        for (int i = 0; i < list.length; i++) {
            if (list[i].equals("*")) {
                if (sttmp.length() > 0) {
                    stack.push(Integer.parseInt(sttmp));
                    sttmp = "";
                }
                star();
            } else if (list[i].equals("#")) {
                if (sttmp.length() > 0) {
                    stack.push(Integer.parseInt(sttmp));
                    sttmp = "";
                }
                shap();
            } else if (list[i].equals("S")) {
                if (sttmp.length() > 0) {
                    stack.push(Integer.parseInt(sttmp));
                    sttmp = "";
                }
                one();
            } else if (list[i].equals("D")) {
                if (sttmp.length() > 0) {
                    stack.push(Integer.parseInt(sttmp));
                    sttmp = "";
                }
                two();
            } else if (list[i].equals("T")) {
                if (sttmp.length() > 0) {
                    stack.push(Integer.parseInt(sttmp));
                    sttmp = "";
                }
                three();
            } else {
                sttmp += list[i];
            }
        }
        while (stack.size() > 0) {
            answer += stack.pop();
        }
        return answer;
    }
    
    public static void star() {
        int cnt = 0;
        int[] stars = new int[2];
        while (stack.size() > 0 && cnt < 2) {
            stars[cnt] = stack.pop() * 2;
            cnt++;
        }
        for (int i = cnt - 1; i >= 0; i--) {
            stack.push(stars[i]);
        }
    }
    
    public static void shap() {
        int cnt = stack.pop();
        stack.push(cnt * -1);
    }
    public static void one() {
        Integer tmp = stack.pop();
        stack.push(tmp);
    }
    public static void two() {
        Integer tmp = stack.pop();
        double tmp2 = Math.pow(tmp, 2);
        stack.push((int)tmp2);
    }
    public static void three() {
        Integer tmp = stack.pop();
        double tmp2 = Math.pow(tmp, 3);
        stack.push((int)tmp2);
    }
}