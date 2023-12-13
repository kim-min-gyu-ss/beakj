import java.util.*;
import java.io.*;

public class Main {
    static int[] top, bottom;
    static int N, H;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());

        top = new int[N / 2];
        bottom = new int[N / 2];
        for (int i = 0; i < N; i++) {
            if (i % 2 == 0) {
                bottom[i / 2] = Integer.parseInt(br.readLine());
            } else {
                top[i / 2] = Integer.parseInt(br.readLine());
            }
        }
        Arrays.sort(top);
        Arrays.sort(bottom);

        int min = Integer.MAX_VALUE;
        int cnt = 0;
        for (int i = 1; i <= H; i++) {
            int down = check(0,N / 2 ,bottom, i);
            int up = check(0,N / 2, top,H - i + 1);

            if (min > down + up) {
                min = down + up;
                cnt = 1;
            } else if (min == down + up) {
                cnt++;
            }
        }
        System.out.println(min + " " + cnt);
    }

    static int check(int left, int right, int[] arr, int h){
        while (left < right) {
            int mid = (left + right) / 2;

            if (arr[mid] >= h) {
                right = mid;
            } else {
                left = mid+1;
            }
        }
        return arr.length - right;
    }
}