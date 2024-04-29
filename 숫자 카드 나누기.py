from math import gcd


def solution(arrayA, arrayB):
    a, b = arrayA[0], arrayB[0]
    aa, bb = -1, -1

    for i in range(1, len(arrayA)):
        a = gcd(a, arrayA[i])
        b = gcd(b, arrayB[i])

    for x in arrayA:
        if x % b == 0: break
    else:
        bb = b

    for x in arrayB:
        if x % a == 0: break
    else:
        aa = a

    return 0 if aa == -1 and bb == -1 else max(aa, bb)
