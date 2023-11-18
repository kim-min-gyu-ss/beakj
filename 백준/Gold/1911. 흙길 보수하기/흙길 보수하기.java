import java.io.*;
import java.util.*;

public class Main {
    static int N, L, answer, cnt;
    static int[][] woongdung2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken());
        woongdung2 = new int[N][2];
        for (int i = 0; i < N; i++) {
            int[] tmp = new int[2];
            st = new StringTokenizer(br.readLine());
            tmp[0] = Integer.parseInt(st.nextToken());
            tmp[1] = Integer.parseInt(st.nextToken());
            woongdung2[i] = tmp;
        }
        Arrays.sort(woongdung2, Comparator.comparing(woong -> woong[0]));
        answer = 0;
        cnt = 0;
        for(int[] num : woongdung2) {
            if (num[0] > cnt) {
                cnt = num[0];
            }
            if (num[1] > cnt) {
                while (num[1] > cnt) {
                    cnt += L;
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}

