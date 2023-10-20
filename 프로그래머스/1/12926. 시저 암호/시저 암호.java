class Solution {
    public String solution(String s, int n) {
        String answer = "";
        char[] upper = {'A','B','C','D','E','F','G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

        char[] lower = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if(Character.isUpperCase(ch)) {
                answer = getAnswer(ch, answer, upper, n);
            }
            else if(Character.isLowerCase(ch)) {
                answer = getAnswer(ch, answer, lower, n);
            } else {
                answer += " ";
            }
        }
        return answer;
    }

    static private String getAnswer(char ch,
                                    String answer,
                                    char[] charArr,
                                    int n) {
         for(int j=0; j < charArr.length; j++) {
            if(ch == charArr[j]) {
                if(j+n >= charArr.length) {
                    if(charArr.length - j -n < 0) {
                        answer += charArr[-(charArr.length - j -n)];    
                    } else {
                        answer += charArr[charArr.length - j -n];    
                    }

                } else {
                    answer += charArr[j+n]; 

                }       
            }
        }
        return answer;
    }
}