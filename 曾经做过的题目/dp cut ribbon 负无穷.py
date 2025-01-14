n,a,b,c = map(int,input().split())
dp=[0]+[float('-inf')]*n
for i in range(1,n+1):
    for j in (a,b,c):
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)

print(dp[n])
