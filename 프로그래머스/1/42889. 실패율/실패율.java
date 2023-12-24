import java.util.*;
class Solution {
    static int[] chng;
    static List<Stage> stg = new ArrayList<>();
    static class Stage {
        int idx;
        double ratio;
        
        Stage(int idx, double ratio) {
            this.idx = idx;
            this.ratio = ratio;
        }
        
        public int getIdx() {
            return this.idx;
        }
        
        public double getRatio() {
            return this.ratio;
        }
    }
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        chng = new int[N + 1];
        for (int i : stages) {
            chng[i - 1]++;
        }
        
        int total = chng[N];
        for (int i = N; i > 0; i--) {
            total += chng[i - 1];
            stg.add(new Stage(i,total != 0 ? (double) chng[i - 1] / total : 0));
        }
        Collections.sort(stg, Comparator.comparing(Stage::getRatio).reversed()
                        .thenComparing(Stage::getIdx));
        
        for (int i = 0; i < N; i++) {
            answer[i] = stg.get(i).getIdx();
        }
        
        return answer;
    }
}