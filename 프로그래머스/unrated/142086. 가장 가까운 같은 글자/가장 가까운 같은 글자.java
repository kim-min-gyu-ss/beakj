class Solution {
    public int[] solution(String s) {
        int tmp = s.length();
        int[] answer = new int[tmp];
        for (int i = 0; i < tmp - 1; i++){
            if (answer[i] < 1) {
                answer[i] = -1;
            }
            for (int j = i + 1; j < tmp; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    answer[j] = j - i;
                    break;
                }
            }
        }
        if (answer[answer.length - 1] == 0) {
            answer[answer.length - 1] = -1;
        }
        return answer;
    }
}