import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder();
    private StringTokenizer st;

    private void solution() throws Exception {
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            sb.append((isVPS(br.readLine()) ? "YES" : "NO") + "\n");
        }

        bw.write(sb + "");
        bw.flush();
        bw.close();
    }

    private boolean isVPS(String data) {
        int n = data.length();
        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < n; i++) {
            if (data.charAt(i) == '(') {
                stack.add('(');
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                if (stack.peekLast() != '(') {
                    return false;
                }
                stack.pollLast();
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}