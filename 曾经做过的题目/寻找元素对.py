n = int(input())
m = list(map(int,input().split()))
K = int(input())
num = 0
for i in range(n):
    for j in range(i+1,n):
        if m[i] + m[j] == K:
            num+=1
print(num)