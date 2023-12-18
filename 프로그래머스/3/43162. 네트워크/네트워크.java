import java.util.*;
class Solution {
    static boolean[] visited;
    public int solution(int n, int[][] computers) {
        visited = new boolean[n];
        int answer = 0;
        for (int i = 0; i < n; i++) {
            if (dfs(n, i, computers)) {
                answer++;    
            }
        }
        return answer;
    }
    private boolean dfs(int leng, int now, int[][] computers) {
        if (visited[now]) return false;
        visited[now] = true;
        for (int i = 0; i < leng; i++) {
            if (computers[now][i] == 0) continue;
            if (visited[i]) continue;
            dfs(leng, i, computers);
        }
        return true;
    }
}