import java.util.*;
class Solution {
    static class Move {
        private int start;
        private int end;
        
        public Move(int start, int end) {
            this.start = start;
            this.end = end;
        }
        
        public int getEnd() {
            return this.end;
        }
        
        public int getStart() {
            return this.start;
        }
    }
    static List<Move> moves = new ArrayList<>();
    static int mx;
    public int solution(int[][] routes) {
        int answer = 1;
        int leng = routes.length;
        for (int i = 0; i < leng; i++) {
            moves.add(new Move(routes[i][0], routes[i][1]));
        }
        Collections.sort(moves, Comparator.comparing(Move::getEnd));
        mx = moves.get(0).getEnd();
        
        for(int i = 1; i < leng; i++) {
            if (moves.get(i).getStart() <= mx && moves.get(i).getEnd() >= mx) continue;    
            mx = moves.get(i).getEnd();
            answer++;
        }
        return answer;
    }
}