import java.util.*;
import java.io.*;

public class Main {
    static int[] num;
    static int N, right, left, result;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        num = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(num);

        result = 0;
        for (int i = 0 ; i < N; i++) {
            left = 0;
            right = N - 1;
            while (true) {
                if (left == i) {
                    left++;
                } else if (right == i) {
                    right--;
                }
                if (left >= right) break;
                if (num[left] + num[right] > num[i]) {
                    right--;
                } else if (num[left] + num[right] < num[i]) {
                    left++;
                } else {
                    result++;
                    break;
                }
            }
        }
        System.out.println(result);
    }

}