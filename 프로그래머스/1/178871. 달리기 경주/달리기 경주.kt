class Solution {
    fun solution(players: Array<String>, callings: Array<String>): Array<String> {
        val ranks = mutableMapOf<String, Int>()
        players.forEachIndexed { index, player -> 
            ranks[player] = index
        }
        
        callings.forEach { player1 ->
            val rank1 = ranks[player1]!!
            val rank2 = rank1 - 1
            val player2 = players[rank2]
            
            players[rank2] = player1
            players[rank1] = player2
            
            ranks[player1] = rank2
            ranks[player2] = rank1
        }
        
        return players
    }
}