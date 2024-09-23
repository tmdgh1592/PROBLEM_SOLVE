import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder();
    private StringTokenizer st;

    private void solution() throws Exception {
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> q = new LinkedList<>();
        Deque<Integer> inputNumbers = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            inputNumbers.add(num);
        }

        for (int i = 1; i <= n; i++) {
            q.add(i);
            sb.append("+\n");

            while (inputNumbers.peekFirst() != null &&
                    q.peekLast() != null &&
                    inputNumbers.peekFirst().equals(q.peekLast())) {
                inputNumbers.pollFirst();
                q.pollLast();
                sb.append("-\n");
            }
        }

        if (inputNumbers.isEmpty()) {
            bw.write(sb + "");
        } else {
            bw.write("NO");
        }

        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}