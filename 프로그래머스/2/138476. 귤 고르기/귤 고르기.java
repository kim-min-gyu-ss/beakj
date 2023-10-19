import java.util.*;
class Solution {
    static Map<Integer, Integer> map = new TreeMap<>();
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        for (int e : tangerine) {
            map.put(e, map.getOrDefault(e, 0) + 1);
        }
        List<Integer> keylist = new ArrayList<>(map.keySet());
        Collections.sort(keylist, Comparator.comparing
                         (v -> map.get(v), Comparator.reverseOrder()));
        for (Integer e : keylist) {
            if (k <= 0) 
                break;
            answer++;
            k -= map.get(e);
        }
        return answer;
    }
}