import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder();
    private StringTokenizer st;

    private void solution() throws Exception {
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> q = new ArrayDeque<>();

        for(int i = 1; i <= n; i++) {
            q.add(i);
        }

        while (q.size() > 1) {
            q.pollFirst();
            Integer x = q.pollFirst();

            if (x != null) {
                q.add(x);
            }
        }

        sb.append(q.peekFirst());

        bw.write(sb + "");
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}