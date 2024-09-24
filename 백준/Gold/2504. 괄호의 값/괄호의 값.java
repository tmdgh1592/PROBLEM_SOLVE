import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder();
    private StringTokenizer st;
    private int answer = 0, temp = 1;
    Deque<Character> stack = new ArrayDeque<>();

    private void solution() throws Exception {
        String data = br.readLine();
        for (int i = 0; i < data.length(); i++) {
            char x = data.charAt(i);

            if (x == '(') {
                stack.add(x);
                temp *= 2;
                continue;
            }
            if (x == '[') {
                stack.add(x);
                temp *= 3;
                continue;
            }
            if (x == ')') {
                if (stack.isEmpty() || stack.peekLast() == '[') {
                    answer = 0;
                    break;
                }
                if (data.charAt(i - 1) == '(') {
                    answer += temp;
                }
                stack.pollLast();
                temp /= 2;
                continue;
            }
            if (x == ']') {
                if (stack.isEmpty() || stack.peekLast() == '(') {
                    answer = 0;
                    break;
                }
                if (data.charAt(i - 1) == '[') {
                    answer += temp;
                }

                stack.pollLast();
                temp /= 3;
            }
        }

        if (!stack.isEmpty()) {
            answer = 0;
        }

        bw.write(Integer.toString(answer));
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}