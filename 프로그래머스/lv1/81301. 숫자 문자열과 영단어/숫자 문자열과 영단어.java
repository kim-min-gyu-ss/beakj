import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        String rst = "";
        Map<String, Integer> dan = new HashMap<>();
        dan.put("zero",0);
        dan.put("one",1);
        dan.put("two",2);
        dan.put("three",3);
        dan.put("four",4);
        dan.put("five",5);
        dan.put("six",6);
        dan.put("seven",7);
        dan.put("eight",8);
        dan.put("nine",9);
        // System.out.print(dan);
        char[] ch = s.toCharArray();
        String call = "";
        for (char tmp : ch) {
            if (Character.isDigit(tmp)) {
                rst += String.valueOf(tmp);
            }
            else {
                call += String.valueOf(tmp);
                if (dan.containsKey(call)) {
                    rst += dan.get(call);
                    call = "";
                }
            }
        }
        
        answer = Integer.parseInt(rst);
        return answer;
    }
}