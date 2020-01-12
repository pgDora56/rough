A = int(input())
B = int(input())
C = int(input())
X = int(input())
cnt = 0
for ap in range(A+1):
    for bp in range(B+1):
        for cp in range(C+1):
            if ap * 500 + bp * 100 + cp * 50 == X:
                cnt += 1
print(cnt)
