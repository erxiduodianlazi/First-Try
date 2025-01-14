#滚动矩阵
N,B = map(int,input().split())
prices=list(map(int,input().split()))
weights=list(map(int,input().split()))
dp = [0] * (B+1)
for i in range(N):
    for j in range(B,weights[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weights[i]]+prices[i])
print(max(dp))
#二维矩阵 B是包的容量，N是东西的数目
N,B = map(int,input().split())
price=[0]+[int(x) for x in input().split()]
weight =[0]+[int(x) for x in input().split()]
bag = [[0]*(B+1) for i in range(N+1)]
for i in range(1,N+1):
    for j in range(1,B+1):
        if weight[i]<=j:
            bag[i][j]=max(bag[i-1][j],bag[i-1][j-weight[i]]+price[i])
        else:
            bag[i][j]=bag[i-1][j]
print(bag[-1][-1])