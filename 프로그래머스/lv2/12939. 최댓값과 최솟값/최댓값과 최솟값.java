import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        List<Integer> tmpList = new ArrayList<>();
        String[] strList = s.split(" ");
        for (String st : strList) {
            tmpList.add(Integer.parseInt(st));
        }
        Collections.sort(tmpList);
        String mn = String.valueOf(tmpList.get(0));
        String mx = String.valueOf(tmpList.get(tmpList.size() - 1));
        
        answer += mn;
        answer += " ";
        answer += mx;
        return answer;
    }
}