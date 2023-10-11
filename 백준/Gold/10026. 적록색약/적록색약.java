import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static String[][] rgb1, rgb2;
    static int N, answer1, answer2;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static Queue<Node> q = new LinkedList<>();
    static class Node {
        int y;
        int x;
        Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        rgb1 = new String[N][N];
        rgb2 = new String[N][N];
        for (int i = 0; i < N; i++) {
            String st = br.readLine();
            for (int j = 0; j < N; j++) {
                String tmp = String.valueOf(st.charAt(j));
                rgb1[i][j] = tmp;
                rgb2[i][j] = tmp;
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                normalBfs(i, j);
                rgbBfs(i, j);
            }
        }
        System.out.println(answer1 + " " + answer2);
    }

    private static void normalBfs(int y, int x) {
        String s = rgb1[y][x];
        if (s.equals("W")) return;
        rgb1[y][x] = "W";
        if (s != "W") answer1++;
        q.offer(new Node(y,x));
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || N <= new_x
                        || rgb1[new_y][new_x] == "W" || !rgb1[new_y][new_x].equals(s)) continue;
                rgb1[new_y][new_x] = "W";
                q.offer(new Node(new_y, new_x));
            }
        }
    }
    private static void rgbBfs(int y, int x) {
        String s = rgb2[y][x];
        if (s.equals("W")) return;
        rgb2[y][x] = "W";
        if (s != "W") answer2++;
        q.offer(new Node(y,x));
        while (!q.isEmpty()) {
            Node tmp = q.poll();
            for (int i = 0; i < 4; i++) {
                int new_y = tmp.y + dy[i];
                int new_x = tmp.x + dx[i];
                if (0 > new_y || N <= new_y || 0 > new_x || N <= new_x
                        || rgb2[new_y][new_x] == "W") continue;
                if (s.equals("B")) {
                    if (!rgb2[new_y][new_x].equals(s)) continue;
                } else {
                    if (rgb2[new_y][new_x].equals("B")) continue;
                }
                rgb2[new_y][new_x] = "W";
                q.offer(new Node(new_y, new_x));
            }
        }
    }
}
