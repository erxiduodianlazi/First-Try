n,m= map(int,input().split())
zhi = list(map(int,input().split()))
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(1,m+1):
    for j in zhi:
        if j<=i:
             dp[i]=min(dp[i-j]+1,dp[i])
if dp[m] != float('inf'):
    print(dp[m])
else:
    print(-1)

