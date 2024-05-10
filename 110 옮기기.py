def solution(s):
    answer = []
    for string in s:
        stack = ""
        cnt = 0
        for x in string:
            if x == "0" and stack[-2:] == "11":
                stack = stack[:-2]
                cnt += 1
            else:
                stack += x

        idx = stack.find("111")
        if idx != -1:
            result = stack[:idx] + "110" * cnt + stack[idx:]
        else:
            idx = stack.rfind("0")
            result = stack[:idx+1] + "110" * cnt + stack[idx+1:]
        answer.append(result)
    return answer