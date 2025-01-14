
m=int(input())
n=int(input())
c=list(map(str,input().split()))
for i in range(len(c)-1):
    for j in range(i+1, len(c)):
        #print(i,j)
        if int(c[i] + c[j]) < int(c[j] + c[i]):
            c[i], c[j] = c[j], c[i]
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if j<len(c[i-1]):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],int(str(dp[i-1][j-len(c[i-1])])+c[i-1]))
print(dp[-1][-1])

