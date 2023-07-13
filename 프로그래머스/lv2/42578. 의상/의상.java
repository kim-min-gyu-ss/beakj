import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 0;
        HashMap<String, Integer> result = new HashMap<String, Integer>();
        for (String[] cloth : clothes) {
            if (result.containsKey(cloth[1])) {
                result.put(cloth[1],result.get(cloth[1]) + 1);
            } else {
                result.put(cloth[1], 2);
            }
        }
        System.out.println(result);
        int tmp = 1;
        for (String it : result.keySet()) {
            tmp *= result.get(it);
        }
        answer = tmp;
        return answer - 1;
    }
}