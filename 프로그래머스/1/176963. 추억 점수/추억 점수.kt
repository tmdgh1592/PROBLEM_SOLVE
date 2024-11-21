class Solution {
    fun solution(names: Array<String>, yearning: IntArray, photo: Array<Array<String>>): IntArray {
        val answer = mutableListOf<Int>()
        val scores = names.zip(yearning.toTypedArray()).toMap()

        photo.forEachIndexed { index, photos ->
            answer.add(0)
            photos.forEach { name ->
                answer[index] += scores[name] ?: 0
            }
        }

        return answer.toIntArray()
    }
}