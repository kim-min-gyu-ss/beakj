class Solution {
    public String solution(String s) {
        String answer = "";
        int cnt = 0;
        for (int i = 0; i < s.length(); i++) {
            char tmp = s.charAt(i);

            if (cnt % 2 == 0) {
                answer += String.valueOf(Character.toUpperCase(tmp));
            }
            else {
                answer += String.valueOf(Character.toLowerCase(tmp));
            }
            if (tmp == ' ') {
                cnt = -1;
            }
            cnt++;
        }       
        return answer;
    }
}