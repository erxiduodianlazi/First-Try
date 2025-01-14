from collections import deque
def dfs(x,y,c,queue):
    c[x][y]=2
    queue.append((x,y))
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and c[nx][ny]==1:
            dfs(nx,ny,c,queue)

distance=0
def bfs(c,queue):
    global distance
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx <n and 0<=ny<n:
                    if c[nx][ny]==1:
                        return distance
                    elif c[nx][ny]==0:
                        c[nx][ny]=2
                        queue.append((nx,ny))
        distance+=1
    return distance
n = int(input())
c=[list(map(int,input())) for i in range(n)]
directions=[(-1,0),(0,1),(1,0),(0,-1)]
queue=deque()
def jisuan(n,c):
    for i in range(n):
        for j in range(n):
            if c[i][j]==1:
                dfs(i,j,c,queue)
                return bfs(c,queue)#必须用函数，用两层break的化会输出错误
print(jisuan(n,c))

#Dijk算法 等下好好钻研一下 heapq ！
# 俞天麒 24物理学院
import heapq
n=int(input())
land=[]
dir=[[0,1],[0,-1],[1,0],[-1,0]]
for i in range(n):
    land.append(input())
visited=[[True]*(len(land[i])) for i in range(len(land))]
def find(x1,y1):
    pos=[]
    heapq.heappush(pos,(0,x1,y1))
    visited[x1][y1]=False
    while pos:
        step,x,y=heapq.heappop(pos)
        #print(step,x,y)
        if land[x][y]=="1" and step!=0:
            return step
        for dx,dy in dir:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<len(land[nx]) and visited[nx][ny]:
                visited[nx][ny]=False
                if land[nx][ny]==land[x][y] and land[x][y]!="0":
                    heapq.heappush(pos,(step,nx,ny))
                else:
                    heapq.heappush(pos,(step+1,nx,ny))
mark=False
for i in range(n):
    for j in range(len(land[i])):
        if land[i][j]=="1":
            print(find(i,j)-1)
            exit()