import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String, Integer> dict = new HashMap<>();
        for (int i=0; i<name.length; i++) {
            dict.put(name[i], yearning[i]);
        }
        
        int[] answer = new int[photo.length];
        for (int i=0; i<photo.length; i++) {
            String[] people = photo[i];
            for (String man : people) {
                answer[i] += dict.getOrDefault(man, 0);
            }
        }
        
        return answer;
    }
}