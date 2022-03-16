t = int(input())

for _ in range(t):
    input()
    
    n = int(input())
    total_candy = 0
    
    for i in range(n):
        total_candy += int(input())
    
    if(total_candy % n == 0):
        print('YES')
    else:
        print('NO')