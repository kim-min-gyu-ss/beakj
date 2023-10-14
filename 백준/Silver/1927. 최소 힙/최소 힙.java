import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static PriorityQueue<Integer> q = new PriorityQueue<Integer>();
    static int N, value;
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            value = Integer.parseInt(br.readLine());
            if (value > 0) {
                q.add(value);
            } else {
                if (!q.isEmpty()) {
                    System.out.println(q.poll());
                } else {
                    System.out.println(0);
                }
            }
        }
    }
}

