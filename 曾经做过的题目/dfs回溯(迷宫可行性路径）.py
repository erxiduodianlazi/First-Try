#不要保护圈 ，有专门的布尔表的解
cnt=0
def dfs(x,y,t,c):
    global cnt
    if x==n-1 and y==m-1:
        cnt+=1
        return
    for dx,dy in directions:
        nx=x+dx;ny=y+dy
        if 0<=nx<n and 0<=ny<m and not c[nx][ny] and t[nx][ny]==0:
            c[nx][ny]=True
            dfs(nx,ny,t,c)
            c[nx][ny]=False
    return

n,m=map(int,input().split())
t=[[False] * m for _ in range(n)]
c=[list(map(int,input().split())) for i in range(n)]
directions=[(-1,0),(1,0),(0,1),(0,-1)]
if t[0][0]==1:
    print(0)
else:
    c[0][0]= True
    dfs(0,0,t,c)
    print(cnt)

#加保护圈，原地改动
cnt=0
def dfs(x,y,maze):
    global cnt
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if maze[nx][ny]=='e':
            cnt+=1
            continue
        if maze[nx][ny]==0:
            maze[nx][ny]=1
            dfs(nx,ny,maze)
            maze[nx][ny]=0
    return

n, m = map(int, input().split())
maze = []
maze.append([-1 for x in range(m + 2)])
for _ in range(n):
    maze.append([-1] + [int(_) for _ in input().split()] + [-1])
maze.append([-1 for x in range(m + 2)])
maze[1][1] = 's'
maze[n][m] = 'e'
cnt = 0
dfs(1,1,maze)
print(cnt)




#错的
cnt=0
def dfs(x,y,t,c):
    global cnt#把cnt变化成全局变量，但是前面要加cnt=0，因为OJ不能识别
    if x==n-1 and y==n-1:
        cnt+=1
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and not c[nx][ny] and t[nx][ny]==0:
            c[nx][ny]=True
            dfs(nx,ny,t,c)
            c[nx][ny]=False
    return cnt

n,m=map(int,input().split())
c=[[False]*m for _ in range(n)]
directions=[(-1,0),(1,0),(0,1),(0,-1)]
t =[list(map(int, input().split())) for _ in range(n)]
if t[0][0]==1:
    print(0)
else:
    c[0][0]=True
    for i in range(n):#不要遍历，因为迷宫的起点只有（0，0）
        for j in range(m):
            if t[i][j]==0:
                dfs(i,j,t,c)
print(cnt)




