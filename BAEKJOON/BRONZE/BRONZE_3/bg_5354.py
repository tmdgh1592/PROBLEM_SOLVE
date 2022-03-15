n = int(input())
arr = [int(input()) for _ in range(n)]

for i in range(len(arr)):
    j_size = arr[i]

    if(j_size < 3):
        for _ in range(j_size):
            print('#'*j_size)
    else:
        print('#' * j_size)
        for _ in range(j_size - 2):
            print('#' + 'J'*(j_size - 2) + '#')
        print('#' * j_size)

    print()
