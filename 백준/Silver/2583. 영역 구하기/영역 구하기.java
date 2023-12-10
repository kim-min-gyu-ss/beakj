import java.io.*;
import java.util.*;

public class Main {
    static Queue<Node> q = new LinkedList<>();
    static int M, N, K;
    static int[][] area;
    static boolean[][] visited;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static class Node {
        int y;
        int x;
        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        area = new int[M][N];
        visited = new boolean[M][N];
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            int x_1 = Integer.parseInt(st.nextToken());
            int y_1  = Integer.parseInt(st.nextToken());
            int x_2 = Integer.parseInt(st.nextToken());
            int y_2 = Integer.parseInt(st.nextToken());
            check(x_1, y_1, x_2, y_2);
        }
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j]) {
                    answer.add(bfs(i,j));
                }
            }
        }
        Collections.sort(answer);
        System.out.println(answer.size());
        for (Integer ans : answer) {
            System.out.print(ans + " ");
        }
    }

    private static int bfs(int y, int x) {
        int result = 1;
        q.offer(new Node(y,x));
        visited[y][x] = true;
        while (!q.isEmpty()) {
            Node node = q.poll();
            for (int k = 0; k < 4; k++) {
                int new_y = node.y + dy[k];
                int new_x = node.x + dx[k];
                if (new_y >= M || new_x >= N || new_y < 0 || new_x < 0
                || visited[new_y][new_x]) continue;
                result++;
                visited[new_y][new_x] = true;
                q.offer(new Node(new_y, new_x));
            }
        }
        return result;
    }

    private static void check(int x_1, int y_1, int x_2, int y_2) {
        for (int i = y_1; i < y_2; i++) {
            for (int j = x_1; j < x_2; j++) {
                visited[i][j] = true;
            }
        }
    }
}

