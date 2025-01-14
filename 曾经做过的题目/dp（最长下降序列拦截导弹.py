
k = int(input())
m=list(map(int,input().split()))
dp =[1]*k #dp[i]表示以i元素为结尾的递减序列有多长
for i in range(1,k):
    for j in range(i):
        if m[i]<=m[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
