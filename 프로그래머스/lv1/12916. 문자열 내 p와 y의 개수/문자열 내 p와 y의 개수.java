class Solution {
    boolean solution(String s) {
        boolean answer = true;
        String[] lst = s.toLowerCase().split("");
        int p = 0, y = 0;
        for (int i = 0; i < lst.length; i++) {
            if (lst[i].equals("p")) {
                p++;
            }
            else if (lst[i].equals("y")) {
                y++;
            }
        }
        if (p - y == 0) {
            return true;
        }
        return false;
    }
}