import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {

    static int[] out;
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int answer = 0;
        Map<String, Integer> in = new HashMap<>();

        for (int i = 0; i < N; i++) {
            in.put(br.readLine(),i);
        }
        out = new int[N];

        for (int i = 0; i < N; i++) {
            String num = br.readLine();
            out[i] = in.get(num);
        }

        for(int i = 0; i< N-1; i++){
            for(int j = i+1; j< N; j++){
                if(out[i] > out[j]){
                    answer += 1;
                    break;
                }
            }
        }

        System.out.print(answer);
    }
}
