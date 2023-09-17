class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int len = p.length();
        for(int i = 0; i <= t.length() - len; i++) {
            boolean isSmall = true;
            for(int j = 0; j < len; j++) {
                if(t.charAt(i+j) == p.charAt(j)) {
                    continue;
                }

                if(t.charAt(i+j) > p.charAt(j)) {
                    isSmall = false;
                }
                break;
            }
            if(isSmall) {
                answer++;
            }
        }
        return answer;
    }
}