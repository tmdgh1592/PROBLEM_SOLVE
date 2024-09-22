import java.util.*;
import java.io.*;

public class Main {
    private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private final StringBuilder sb = new StringBuilder("<");
    private StringTokenizer st;
    private final Deque<Integer> numbers = new ArrayDeque<>();
    private final List<String> answer = new ArrayList<>();

    private void solution() throws Exception {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            numbers.add(i);
        }

        while (!numbers.isEmpty()) {
            for (int i = 0; i < k - 1; i++) {
                numbers.add(numbers.pollFirst());
            }
            answer.add(numbers.pollFirst() + "");
        }

        sb.append(String.join(", ", answer));

        bw.write(sb + ">");
        bw.flush();
        bw.close();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}