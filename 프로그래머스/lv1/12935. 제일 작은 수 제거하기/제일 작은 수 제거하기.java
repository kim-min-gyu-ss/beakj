
class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) {
            int[] answer = {-1};
            return answer;
        }
        int[] answer = new int[arr.length - 1];
        int mn = arr[0];
        int idx = 0;
        
        for (int i = 0; i < arr.length; i++) {
            mn = Math.min(mn,arr[i]);
        }
        
        for (int j = 0; j < arr.length; j++) {
            if (mn == arr[j]) continue;
            answer[idx] = arr[j];
            idx++;
        }
        
        return answer;
    }
}