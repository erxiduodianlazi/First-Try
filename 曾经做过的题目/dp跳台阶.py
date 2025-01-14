n=int(input())
dp=[0]+[1]*n
for i in range(2,n+1):
    for j in range(1,i):
        dp[i]+=dp[i-j]
print(dp[n])