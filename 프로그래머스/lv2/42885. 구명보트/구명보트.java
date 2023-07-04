import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        List<Integer> intlist = new ArrayList<>();
        for (int i = 0; i < people.length; i++) {
            intlist.add(people[i]);
        }
        
        
        
        while (intlist.size() > 0) {
            int tmp = 0;
            int cnt = 0;
            while (tmp < limit) {
                if (cnt % 2 == 0) {
                    if (tmp + intlist.get(intlist.size() - 1) > limit) break;
                    tmp += intlist.get(intlist.size() - 1);
                    intlist.remove(intlist.size() - 1);
                } else {
                    if (tmp + intlist.get(0) > limit) break;
                    tmp += intlist.get(0);
                    intlist.remove(0);
                }
                cnt++;
                if (cnt > intlist.size()) break;
                if (intlist.size() == 0) break;
            }
            answer++;
        }
        return answer;
    }
}