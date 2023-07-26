import java.util.*;
class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        int ln = citations.length;
        Arrays.sort(citations);
        
        for (int i = 0; i < ln; i++) {
            if (citations[i] >= ln - i) {
                answer = ln - i;
                break;
            }
        }
        
        return answer;
    }
}