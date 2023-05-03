class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        int[] sample = new int[n];
        for (int i = 0; i< n; i++){
            sample[i] = arr1[i] | arr2[i];
            answer[i] = "";
            for (int j = n - 1; j >= 0; j--){
                if ((sample[i] & (1 << j)) > 0){
                    answer[i] += "#";
                }else{
                    answer[i] +=  " ";
                }
            }
        }
        
        return answer;
    }
}