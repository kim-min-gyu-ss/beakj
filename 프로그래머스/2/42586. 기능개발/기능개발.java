import java.util.*;
class Solution {
    static Queue<Integer> prg = new LinkedList<>();
    static Queue<Integer> spd = new LinkedList<>();
    static List<Integer> rst = new ArrayList<>();

    public int[] solution(int[] progresses, int[] speeds) {
        // int[] answer = {};
        int leng = progresses.length;
        int cnt = 0;
        for (int i = 0; i < leng; i++) {
            prg.offer(progresses[i]);
            spd.offer(speeds[i]);
        }
        
        while (cnt < leng) {
            int check = prg.size();
            int tmp = 0;
            int ans = 0;
            while (tmp < check) {
                int tmp1 = prg.poll();
                int tmp2 = spd.poll();
                prg.offer(tmp1 + tmp2);
                spd.offer(tmp2);
                tmp++;
            }
            boolean state = true;
            for (int i = 0; i < check; i++) {
                int tmp1 = prg.poll();
                int tmp2 = spd.poll();
                if (state) {
                    if (tmp1 >= 100) {
                        ans++;
                    } else {
                        prg.offer(tmp1);
                        spd.offer(tmp2);
                        state = false;
                    }
                } else {
                    prg.offer(tmp1);
                    spd.offer(tmp2);
                }
            }
            if (ans > 0) {
                rst.add(ans);
            }
            cnt += ans;
        }
        int[] answer = new int[rst.size()];
        for (int i = 0; i < rst.size(); i++) {
            answer[i] = rst.get(i);
        }
        return answer;
    }
}