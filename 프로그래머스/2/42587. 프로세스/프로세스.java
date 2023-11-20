import java.util.*;
class Solution {
    static int[] result;
    static boolean[] visited;
    static Integer[] pri;
    static Queue<Integer> q = new LinkedList<>();
    public int solution(int[] priorities, int location) {
        int leng = priorities.length;
        result = new int[leng];
        pri = new Integer[leng];
        visited = new boolean[leng];
        for (int i = 0; i < leng; i++) {
            pri[i] = priorities[i];
            q.offer(priorities[i]);
        }
        Arrays.sort(pri, Collections.reverseOrder());
        int idx = 0;
        int cnt = 0;
        int gap = 0;
        while (cnt < leng) {
            int tmp = q.poll();
            if (tmp == pri[cnt]) {
                result[idx] = cnt + 1;
                visited[idx] = true;
                cnt++;
            }
            idx++;
            if (idx >= leng) {
                idx = 0;
            }
            // System.out.println("idx " + idx + " tmp " + tmp + " cnt " + cnt);
            q.offer(tmp);
        }
        return result[location];
    }
}