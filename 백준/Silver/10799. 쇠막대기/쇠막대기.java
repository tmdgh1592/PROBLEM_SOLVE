import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder();
    private StringTokenizer st;
    private int answer = 0;

    private void solution() throws Exception {
        String data = br.readLine().strip();
        Deque<Character> q = new ArrayDeque<>();

        for (int i = 0; i < data.length(); i++) {
            Character val = data.charAt(i);

            if (val == '(') {
                q.add('(');
            } else if (val == ')') {
                q.pollLast();

                if (data.charAt(i - 1) == '(') {
                    answer += q.size();
                } else {
                    answer += 1;
                }
            }
        }

        bw.write(Integer.toString(answer));
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}