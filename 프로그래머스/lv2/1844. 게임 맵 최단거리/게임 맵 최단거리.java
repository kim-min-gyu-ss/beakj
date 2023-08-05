import java.util.*;
class Solution {
    private int[] dx = {-1,1,0,0};
    private int[] dy = {0,0,-1,1};
    
    public int solution(int[][] maps) {
        int answer = -1;
        boolean[][] visited = new boolean[maps.length][maps[0].length];
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[i].length; j++) {
                if (maps[i][j] == 0) {
                    visited[i][j] = true;
                }
            }
        }
        
        return bfs(maps, visited);
    }
    
    private int bfs(int[][] maps, boolean[][] visited) {
        Queue<Nd> result = new LinkedList<>();
        int ym = maps.length;
        int xm = maps[0].length;
        visited[0][0] = true;
        result.offer(new Nd(0,0,1));
        
        int mx = ym * xm + 1;
        int mn = mx;
        
        while (!result.isEmpty()) {
            
            Nd tmp = result.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.getY() + dy[i];
                int new_x = tmp.getX() + dx[i];
                
                if (new_y < 0 || new_y >= ym || new_x < 0 || new_x >= xm || visited[new_y][new_x]) continue;
                
                int cnt = tmp.getCnt() + 1;
                result.offer(new Nd(new_y,new_x,cnt));
                visited[new_y][new_x] = true;
                
                if (new_y == ym - 1 && new_x == xm - 1) {
                    mn = Math.min(mn, cnt);
                }
            }
        }
        return mn == mx ? -1 : mn;
    }
    
    public class Nd {
        private int y;
        private int x;
        private int cnt;
        
        public Nd(int y, int x, int cnt) {
            this.y = y;
            this.x = x;
            this.cnt = cnt;
        }
        
        public int getY() {
            return y;
        }
        public int getX() {
            return x;
        }
        public int getCnt() {
            return cnt;
        }
    }
    
}