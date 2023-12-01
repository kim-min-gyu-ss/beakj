import java.util.*;
class Solution {
    static class Truck {
        private int time;
        private int wei;
        
        public Truck(int time, int wei) {
            this.time = time;
            this.wei = wei;
        }
        
        public int getTime() {
            return this.time;
        }
        
        public int getWei() {
            return this.wei;
        }
    }
    static Queue<Truck> q = new LinkedList<>();
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int cnt = 0;
        int idx = 0;
        int total_wei = 0;
        while (cnt < truck_weights.length) {
            answer++;
            for (int i = 0; i < q.size(); i++) {
                Truck t = q.poll();
                if (t.getTime() == answer) {
                    total_wei -= t.getWei();
                    cnt++;
                } else {
                    q.offer(t);
                }
            }
            if (q.size() < bridge_length) {
                if (total_wei + truck_weights[idx] <= weight) {
                    total_wei += truck_weights[idx];
                    q.offer(new Truck(answer + bridge_length, truck_weights[idx]));
                    if (idx < truck_weights.length - 1) idx++;
                }
            }
        }
        return answer;
    }
}