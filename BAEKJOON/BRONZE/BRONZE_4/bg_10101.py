def triple_sum(A, B, C):
    return A+B+C


A, B, C = [int(input()) for _ in range(3)]

if(A == B == C == 60):
    print('Equilateral')
elif((triple_sum(A, B, C) == 180) & (A == B or B == C or C == A)):
    print('Isosceles')
elif((triple_sum(A, B, C) == 180) & (A != B != C)):
    print('Scalene')
else:
    print('Error')
