import java.util.*;
class Solution {
    static Queue<Node> q = new LinkedList<>();
    static boolean[][] visited;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static char[][] mps;
    static int cnt;
    
    static class Node {
        int x;
        int y;
        
        public Node(int y, int x) {
            this.x = x;
            this.y = y;
        }
    }
    public int[] solution(String[] maps) {
        List<Integer> rst = new ArrayList<>();
        visited = new boolean[maps.length][maps[0].length()];
        mps = new char[maps.length][maps[0].length()];
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[0].length(); j++) {
                mps[i][j] = maps[i].charAt(j);
                if (maps[i].charAt(j) == 'X') {
                    visited[i][j] = true;
                }
            }
        }
        
        for (int i = 0; i < maps.length; i++) {
            for (int j = 0; j < maps[0].length(); j++) {
                if (!visited[i][j]) {
                    rst.add(bfs(i,j));    
                }
            }
        }
        int[] answer = new int[rst.size()];
        for (int i = 0; i < rst.size(); i++) {
            answer[i] = rst.get(i);
        }
        Arrays.sort(answer);
        return answer.length > 0 ? answer : new int[] {-1};
    }
    
    private int bfs(int y, int x) {
        cnt = mps[y][x] - '0';
        q.offer(new Node(y, x));
        visited[y][x] = true;
        
        while(!q.isEmpty()) {
            Node node = q.poll();
            for (int k = 0; k < 4; k++) {
                int new_y = node.y + dy[k];
                int new_x = node.x + dx[k];
                if (new_y >= mps.length || new_x >= mps[0].length 
                    || new_y < 0 || new_x < 0 || visited[new_y][new_x]) continue;
                visited[new_y][new_x] = true;
                cnt += mps[new_y][new_x] - '0';
                q.offer(new Node(new_y, new_x));
            }
        }
        return cnt;
    }
}