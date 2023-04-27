import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>(){{
            put("R", 0);
            put("T", 0);
            put("C", 0);
            put("F", 0);
            put("J", 0);
            put("M", 0);
            put("A", 0);
            put("N", 0);
        }};
        for (int i = 0; i < choices.length; i++) {
            char[] chars = survey[i].toCharArray();
            if (choices[i] >= 5) {
                int tmp = map.get(String.valueOf(chars[1]));
                map.put(String.valueOf(chars[1]), tmp + choices[i] - 4);
            }
            else if (choices[i] <= 3) {
                int tmp = map.get(String.valueOf(chars[0]));
                map.put(String.valueOf(chars[0]), tmp + 4 - choices[i]);  
            }
        }
        
        int rValue = map.get("R"); 
        int tValue = map.get("T"); 
        int cValue = map.get("C"); 
        int fValue = map.get("F");
        int jValue = map.get("J"); 
        int mValue = map.get("M");
        int aValue = map.get("A"); 
        int nValue = map.get("N");
        
        // System.out.println(map);
        
        if (rValue >= tValue) {
            answer += 'R';
        }
        else {
            answer += 'T';
        }
        
        if (cValue >= fValue) {
            answer += 'C';
        }
        else {
            answer += 'F';
        }
        
        if (jValue >= mValue) {
            answer += 'J';
        }
        else {
            answer += 'M';
        }
        
        if (aValue >= nValue) {
            answer += 'A';
        }
        else {
            answer += 'N';
        }
        return answer;
    }
}