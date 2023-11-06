class Solution { 
    static int cnt;
    public String solution(int a, int b) {
        int[] m = {31,29,31,30,31,30,31,31,30,31,30,31};
        String[] d = {"THU","FRI","SAT","SUN","MON","TUE","WED"};                                  
        String answer = "";
        cnt = 0;                                  
        for (int i = 0; i < a - 1; i++) {
            cnt += m[i];
        }
        cnt += b;
        int c = cnt % 7;
                                          
        return d[c];
    }
}