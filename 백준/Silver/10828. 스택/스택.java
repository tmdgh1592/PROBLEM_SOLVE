import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder();
    private StringTokenizer st;
    private final Deque<Integer> stack = new ArrayDeque<>();

    private void solution() throws Exception {
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            String cmd = st.nextToken();

            if (cmd.equals("push")) {
                int val = Integer.parseInt(st.nextToken());
                stack.add(val);
            } else if (cmd.equals("pop")) {
                sb.append((stack.isEmpty() ? -1 : stack.pollLast()) + "\n");
            } else if (cmd.equals("size")) {
                sb.append(stack.size() + "\n");
            } else if (cmd.equals("empty")) {
                sb.append((stack.isEmpty() ? 1 : 0) + "\n");
            } else {
                sb.append((stack.isEmpty() ? -1 : stack.peekLast()) + "\n");
            }
        }

        bw.write(sb + "");
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}