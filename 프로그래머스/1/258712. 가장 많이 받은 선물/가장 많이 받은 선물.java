import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int friendSize = friends.length;
        
        HashMap<String, Integer> nameDict = new HashMap<>();
        for (int i=0; i<friends.length; i++) {
            nameDict.put(friends[i], i);
        }
        
        int[] presentScore = new int[friendSize];
        int[][] presentGraph = new int[friendSize][friendSize];
        
        for (String gift : gifts) {
            String[] names = gift.split(" ");
            String a = names[0];
            String b = names[1];
            
            presentScore[nameDict.get(a)] += 1;
            presentScore[nameDict.get(b)] -= 1;
            presentGraph[nameDict.get(a)][nameDict.get(b)] += 1;
        }
        
        int answer = 0;
        for (String a : friends) {
            int score = 0;
            
            for (String b : friends) {
                if (a.equals(b)) continue;
                
                int aIdx = nameDict.get(a);
                int bIdx = nameDict.get(b);
                
                if (presentGraph[aIdx][bIdx] > presentGraph[bIdx][aIdx]) {
                    score += 1;
                } else if (presentGraph[aIdx][bIdx] == presentGraph[bIdx][aIdx] && presentScore[aIdx] > presentScore[bIdx]) {
                    score += 1;
                }
            }
            
            if (score > answer) {
                answer = score;
            }
        }
        
        return answer;
    }
}