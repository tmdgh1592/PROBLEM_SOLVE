class Solution {
    fun inc(alpha:Char, skipSet: Set<Char>): Char {
        val alphas = (97..122).toSet()
        var now = alpha

        while (true) {
            now += 1
            if (now.toInt() !in alphas) {
                now = 'a'
            }
            
            if (now !in skipSet) {
                break
            }
        }
        
        return now
    }

    fun solution(str: String, skip: String, index: Int): String {
        var answer: String = ""
        val skipSet = skip.toSet()

        str.forEach { s ->
            var now = s

            for (i in 0 until index) {
                now = inc(now, skipSet)
            }
            answer += now
        }
        
        return answer
    }
}