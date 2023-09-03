import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int N;
    static int[][] danji;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static List<Integer> result = new ArrayList<>();
    static Queue<Node> q = new LinkedList<>();
    static class Node {
        int y;
        int x;
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        danji = new int[N][N];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                danji[i][j] = str.charAt(j) - '0';
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                bfs(i, j);
            }
        }

//        result.sort(Comparator.naturalOrder());
        Collections.sort(result);
        System.out.println(result.size());
        for (int i = 0; i < result.size(); i++) {
            System.out.println(result.get(i));
        }
    }

    private static void bfs(int y, int x) {
        if (danji[y][x] == 0) return;
        danji[y][x] = 0;
        int cnt = 1;
        q.offer(new Node(y,x));
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || N <= new_x
                        || danji[new_y][new_x] == 0) continue;
                danji[new_y][new_x] = 0;
                q.offer(new Node(new_y, new_x));
                cnt++;
            }
        }
        result.add(cnt);
    }
}

