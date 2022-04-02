import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x


def binary_search(start, end):
    result = -1

    while start <= end:
        mid = (start+end) // 2
        val = ((y+mid)*100) // (x+mid)

        if z < val:
            result = mid
            end = mid-1
        else:
            start = mid+1

    return result


if x == y:
    print(-1)
else:
    print(binary_search(1, x))
