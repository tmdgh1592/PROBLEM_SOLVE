import java.util.*;
import java.io.*;

public class Main {
    private final StringBuilder sb = new StringBuilder();
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private StringTokenizer st;
    private final Deque<Integer> q = new ArrayDeque<>();

    public void solution() throws Exception {
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String cmd = br.readLine();
            st = new StringTokenizer(cmd);
            String cmdType = st.nextToken();

            if (cmdType.equals("push")) {
                int value = Integer.parseInt(st.nextToken());
                q.add(value);
            } else if (cmdType.equals("pop")) {
                Integer val = q.poll();
                if (val == null) {
                    sb.append("-1\n");
                } else {
                    sb.append(val).append("\n");
                }
            } else if (cmdType.equals("size")) {
                int size = q.size();
                sb.append(size).append("\n");
            } else if (cmdType.equals("empty")) {
                if (q.isEmpty()) {
                    sb.append("1\n");
                } else {
                    sb.append("0\n");
                }
            } else if (cmdType.equals("front")) {
                Integer val = q.peekFirst();
                if (val == null) {
                    sb.append("-1\n");
                } else {
                    sb.append(val).append("\n");
                }
            } else if (cmdType.equals("back")) {
                Integer val = q.peekLast();
                if (val == null) {
                    sb.append("-1\n");
                } else {
                    sb.append(val).append("\n");
                }
            }
        }

        bw.write(sb + "\n");
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}