#超时的dfs，不能用
import sys
sys.setrecursionlimit(20000)

m,n = map(int,input().split())
directions=[(1,0),(0,1)]
c=[[0]*n for i in range(m)]
cnt=0
def dfs(x,y):
    global cnt
    if x==m-1 and y==n-1:
        cnt+=1
        return cnt
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and c[nx][ny]!=1:
            c[nx][ny]=1
            dfs(nx,ny)
            c[nx][ny]=0
dfs(0,0)
print(cnt)
#dp
m,n = map(int,input().split())
dp=[[0]*n for _ in range(m)]
dp[0][1]=1;dp[1][0]=1
for i in range(1,m):
    for j in range(1,n):
        dp[i][j]=max(dp[i][j],dp[i-1][j]+dp[j-1][i])

print(dp[-1][-1])