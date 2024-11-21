class Solution {
    fun solution(names: Array<String>, yearning: IntArray, photo: Array<Array<String>>): IntArray {
        val answer = mutableListOf<Int>()
        val scores = mutableMapOf<String, Int>()

        names.forEachIndexed { index, name ->
            scores[name] = yearning[index]
        }

        photo.forEachIndexed { index, photos ->
            answer.add(0)
            photos.forEach { name ->
                answer[index] += scores[name] ?: 0
            }
        }

        return answer.toIntArray()
    }
}