class Solution {
    fun solution(wallpaper: Array<String>): IntArray {
        var answer: IntArray = intArrayOf(1000, 1000, -1, -1)
        
        wallpaper.forEachIndexed { y, row -> 
            row.forEachIndexed { x, col ->
                if (col == '#') {
                    val lux = y
                    val luy = x
                    val rdx = y + 1
                    val rdy = x + 1
                    
                    if (answer[0] > lux) answer[0] = lux
                    if (answer[1] > luy) answer[1] = luy
                    if (answer[2] < rdx) answer[2] = rdx
                    if (answer[3] < rdy) answer[3] = rdy
                }
            }
        }
        
        return answer
    }
}