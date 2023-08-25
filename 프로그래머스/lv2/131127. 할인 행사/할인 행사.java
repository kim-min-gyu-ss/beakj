import java.util.*;
class Solution {    
    static int[] tmp;
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        List<String> list = new ArrayList<>();
        for (int i = 0; i < want.length; i++) {
            list.add(want[i]);
        }
        
        for (int i = 0; i < discount.length - 10 + 1; i++) {
            tmp = new int[number.length];
            for (int j = i; j < i + 10; j++) {
                if (list.contains(discount[j])) {
                    int idx = list.indexOf(discount[j]);
                    tmp[idx] += 1;
                }
            }
            int cnt = 0;
            for (int k = 0; k < number.length; k++) {
                if(number[k] == tmp[k]) {
                    cnt++;
                }
            }
            if (cnt == number.length) {
                answer += 1;
            }
        } 
        return answer;
    }
}