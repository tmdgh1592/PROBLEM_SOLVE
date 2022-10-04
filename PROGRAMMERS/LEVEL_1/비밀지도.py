converter = {'0':' ', '1':'#'}

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        bit = bin(arr1[i] | arr2[i])[2:]
        bit = bit.zfill(n)
        res = ''
        for b in bit:
            res += converter[b]
        answer.append(res)
    
    return answer