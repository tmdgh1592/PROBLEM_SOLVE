T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    aa = a % 10

    if(aa == 0):
        print(10)
    elif(aa in [1, 5, 6]):
        print(aa)
    elif(aa in [2, 3, 7, 8]):
        bb = b % 4
        if(bb == 0):
            print(pow(aa, 4) % 10)
        else:
            print(pow(aa, bb) % 10)
    elif(aa in [4, 9]):
        bb = b % 2
        if(bb == 0):
            print(pow(aa, 2) % 10)
        else:
            print(aa)
