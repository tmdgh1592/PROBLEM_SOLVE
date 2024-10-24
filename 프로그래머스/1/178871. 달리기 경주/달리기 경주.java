import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        int playerSize = players.length;
        Map<String, Integer> playerDict = new HashMap<>();
        
        for (int i=0; i<players.length; i++) {
            playerDict.put(players[i], i);
        }
        
        for (String call : callings) {
            int playerPos = playerDict.get(call);
            String curPlayer = call;
            String frontPlayer = players[playerPos - 1];
            
            playerDict.put(curPlayer, playerPos - 1);
            playerDict.put(frontPlayer, playerPos);
            players[playerPos - 1] = curPlayer;
            players[playerPos] = frontPlayer;
        }
        
        return players;
    }
}