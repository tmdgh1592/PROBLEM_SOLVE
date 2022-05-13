def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

n, m = map(int, input().split())
arr = sort(list(map(int, input().split())))
result = [0]

def permutation(n,m):
    if len(result) == m+1:
        print(*result[1:])
        return

    for x in arr:
        if x >= result[-1]:
            result.append(x)
            permutation(n, m)
            result.pop()

permutation(n,m)