import java.util.*;
import java.io.*;
public class Main {

    static int[] dy = {-1,1,0,0};
    static int[] dx = {0,0,-1,1};
    static int[][] tomato;
    static Queue<int[]> q = new LinkedList<>();
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        tomato = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                tomato[i][j] = Integer.parseInt(st.nextToken());
                if (tomato[i][j] == 1) {
                    q.add(new int[] {i, j});
                }
            }
        }
        System.out.println(bfs());
    }

    public static int bfs() {
        while (!q.isEmpty()) {
            int[] tmp = q.poll();
            int y = tmp[0];
            int x = tmp[1];

            for (int i =0; i < 4; i++) {
                int new_y = y + dy[i];
                int new_x = x + dx[i];
                if (new_y < 0 || new_x < 0 || new_y >= N || new_x >= M) continue;
                if (tomato[new_y][new_x] == 0) {
                    tomato[new_y][new_x] = tomato[y][x] + 1;
                    q.add(new int[]{new_y, new_x});
                }
            }
        }
        int result = Integer.MIN_VALUE;
        if (valid()) {
            return -1;
        } else {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (result < tomato[i][j]) result = tomato[i][j];
                }
            }
        }
        return result - 1;
    }
    public static boolean valid() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (tomato[i][j] == 0) return true;
            }
        }
        return false;
    }
}