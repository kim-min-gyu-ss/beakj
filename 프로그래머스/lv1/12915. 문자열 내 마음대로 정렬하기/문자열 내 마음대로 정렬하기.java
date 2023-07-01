import java.util.*;
class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        HashMap<String, String> tmp = new HashMap<>();
        for (String st : strings) {
            tmp.put(st, String.valueOf(st.charAt(n)));
        }
        TreeMap<String, String> sortedMap = new TreeMap<>(
                (a, b) -> {
                    int compare = tmp.get(a).compareTo(tmp.get(b));
                    if (compare == 0) {
                        return a.compareTo(b);
                    } else {
                        return compare;
                    }
                }
        );
        sortedMap.putAll(tmp);
        int cnt = 0;
        for (Map.Entry<String, String> entry : sortedMap.entrySet()) {
            answer[cnt] = entry.getKey();
            cnt++;
        }
        return answer;
    }
}