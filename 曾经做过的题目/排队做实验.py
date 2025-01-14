n = int(input())
t = list(map(int,input().split()))
c=[]
d=[]
num=0
k=1
l=n-2
for i in range(1,n+1):
    c.append((t[i-1],i))
c.sort(key = lambda x:(x[0],x[1]))
for j in c:
    d.append(j[1])
while k<n:
    num+=c[l][0]*k
    k+=1
    l-=1
num=num/n
print(" ".join(map(str,d)))
print(format(num,".2f"))

#答案版，用了enumerate函数以及前缀和
n = int(input())
t = [(i, int(j)) for i, j in enumerate(input().split(), 1)]
tt = t.copy()
tt.sort(key=lambda x: x[1])

ans = []
for i in tt:
    ans.append(i[0])

print(*ans)

dp = [0] * n
dp[0] = 0
for i in range(1, n):
    dp[i] = dp[i - 1] + tt[i - 1][1]

print('{:.2f}'.format(sum(dp) / n))