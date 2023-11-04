import java.util.*;
class Solution {
    static Set<String> set = new HashSet<>();
    public int[] solution(String s) {
        String tmp = firstParsh(s);
        String tmp2 = firstParsh(tmp);
        List<String> tmp3 = secondParsh(tmp2);
        Collections.sort(tmp3,Comparator.comparing(String::length));
        List<String> lst = new ArrayList<>();
        for (String a : tmp3) {
            if (a.length() > 0) {
                String[] spl = a.split(",");
                for (String spstr : spl) {
                    if (!set.contains(spstr)) {
                        set.add(spstr);
                        lst.add(spstr);
                    }
                }
            }
        }
        int[] answer = new int[lst.size()];
        for (int i = 0; i < lst.size(); i++) {
            answer[i] = Integer.parseInt(lst.get(i));
        }
        return answer;
    }
    
    
    private static List<String> secondParsh(String s) {
        String[] str = s.split("\\},\\{");
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < str.length; i++) {
            ans.add(str[i]);
        }
        return ans;
    }
    
    private static String firstParsh(String s) {
        return s.substring(1, s.length() - 1);
    }
}