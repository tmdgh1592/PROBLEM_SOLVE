class Solution {
    fun solution(park: Array<String>, routes: Array<String>): IntArray {
        val n = park.size
        val m = park[0].length
        val dirs = mapOf(
            "N" to Pair(-1, 0),
            "S" to Pair(1, 0),
            "W" to Pair(0, -1),
            "E" to Pair(0, 1),
        )

        var sx = 0
        var sy = 0

        park.forEachIndexed { i, row ->
            row.forEachIndexed { j, col ->
                if (col == 'S') {
                    sx = i
                    sy = j
                }
            }
        }

        routes.forEach { routeInfo ->
            val routeInfos = routeInfo.split(" ")
            val dir = routeInfos[0]
            val dis = routeInfos[1].toInt()

            val (dx, dy) = dirs[dir]!!
            
            var tmpX = sx
            var tmpY = sy
            var shouldMove = true
            
            for (i in 0 until dis) {
                tmpX += dx
                tmpY += dy
                
                if (tmpX !in 0 until n || tmpY !in 0 until m) {
                    shouldMove = false
                    break
                }
                if (park[tmpX][tmpY] == 'X') {
                    shouldMove = false
                    break
                }
            }
            
            if (shouldMove) {
                sx = tmpX
                sy = tmpY
            }
        }
        
        return intArrayOf(sx, sy)
    }
}