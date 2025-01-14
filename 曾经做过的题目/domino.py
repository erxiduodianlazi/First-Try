M,N =map(int, input().split())
if N % 2 == 0:
    print(N//2*M)
else:
    print(N//2*M + M//2)