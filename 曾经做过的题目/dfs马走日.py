cnt=0
def dfs(x,y):
    global cnt
    if all(all(b==1 for b in x) for x in c):
        cnt+=1
        return
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and c[nx][ny]==0:
            c[nx][ny]=1
            dfs(nx,ny)
            c[nx][ny]=0
    return

for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    c=[[0]*m for _ in range(n)]
    directions=[(1,2),(1,-2),(2,1),(-2,1),(-1,2),(-1,-2),(2,-1),(-2,-1)]
    c[x][y]=1
    cnt=0
    dfs(x,y)
    print(cnt)