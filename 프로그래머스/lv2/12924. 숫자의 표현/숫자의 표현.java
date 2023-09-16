class Solution {
    public int solution(int n) {
        int answer = 0;
        int left = 0;
        int right = 0;
        int hap = 0;
        while(left < n) {
            if (hap < n) {
                right++;
                hap += right;
            } else {
                if (hap == n) answer++;
                left++;
                hap -= left;
            }
        }
        return answer;
    }
}