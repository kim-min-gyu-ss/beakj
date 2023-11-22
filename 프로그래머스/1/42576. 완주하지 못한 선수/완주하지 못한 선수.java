import java.util.*;
class Solution {
    static HashMap<String, Integer> map = new HashMap<>();
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        for (String com : completion) {
            map.put(com, map.getOrDefault(com, 0) + 1);
        }
        for (String par : participant) {
            if (map.get(par) != null && map.get(par) > 0) {
                map.replace(par,map.get(par) - 1);
            } else {
                answer = par;
                break;
            }
        }
        
        return answer;
    }
}