class Solution {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer = arrayListOf<Int>()
        val termMap = hashMapOf<String, Int>()
        
        terms.forEach { termInfo ->
            val (term, duration) = termInfo.split(" ")
            termMap[term] = duration.toInt()
        }
        val (todayYear, todayMonth, todayDay) = today.split(".").map { it.toInt() }
        val todayInt = todayYear * 12 * 28 + todayMonth * 28 + todayDay

        privacies.forEachIndexed { index, privacy ->
            val (date, term) = privacy.split(" ")
            val (year, month, day) = date.split(".").map { it.toInt() }
            val duration = termMap[term]!!
            
            var totalMonths = year * 12 + month + duration
            var expireYear = totalMonths / 12
            var expireMonth = totalMonths % 12
            if (expireMonth == 0) {
                expireYear -= 1
                expireMonth = 12
            }
            
            val expireDay = day - 1
            if (expireDay == 0) {
                expireMonth -= 1
                if (expireMonth == 0) {
                    expireYear -= 1
                    expireMonth = 12
                }
            }

            val expiryInt = expireYear * 12 * 28 + expireMonth * 28 + (if (expireDay == 0) 28 else expireDay)
            
            if (expiryInt < todayInt) {
                answer.add(index + 1)
            }
        }

        return answer.toIntArray()
    }
}