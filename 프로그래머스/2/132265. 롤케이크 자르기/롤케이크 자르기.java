import java.util.*;
class Solution {
    static Set<Integer> set = new HashSet<>();
    static Map<Integer, Integer> map = new HashMap<>();
    public static int solution(int[] topping) {
        int answer = 0;
        int leng = topping.length;
        for (int i = 0; i < leng; i++) {
            map.put(topping[i], map.getOrDefault(topping[i], 0) + 1);
        }
        for (int i = 0; i < leng; i++) {
            set.add(topping[i]);
            map.put(topping[i], map.get(topping[i]) - 1);
            if (map.get(topping[i]) == 0) {
                map.remove(topping[i]);
            }
            if (set.size() == map.size()) {
                answer++;
            }
        }
        return answer;
    }
}