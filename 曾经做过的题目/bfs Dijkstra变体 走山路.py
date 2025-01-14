#这个不行，因为不是普通的Dijkstra，这个是求差值，不到最后是不知道的，提前标记visited 会出事
import heapq
def tili(x,y,c):
    pos=[]
    heapq.heappush(pos,(0,x,y))
    visited[x][y]=True
    while pos:
        strength, x, y=heapq.heappop(pos)
        if x==a and y==b :
            return strength
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and c[nx][ny]!='#' and not visited[nx][ny]:
                visited[nx][ny]=True
                heapq.heappush(pos,(strength+abs(int(c[nx][ny])-int(c[x][y])),nx,ny))
    else:
        return "No"

m,n,p = map(int,input().split())
c=[list(map(str,input().split())) for _ in range(m)]
visited=[[False]*n for _ in range(m)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(p):
    x,y,a,b=map(int,input().split())
    if c[x][y]=='#' or c[a][b]=='#':
        print('No')
        continue
    result=tili(x,y,c)
    print(result)

#别人的好答案
import heapq
m,n,p = map(int,input().split())
c=[list(map(str,input().split())) for _ in range(m)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def tili(x,y,a,b):
    pos=[]
    dist = [[float('inf')] * n for _ in range(m)]
    heapq.heappush(pos, (0, x, y))
    dist[x][y]=0
    while pos:
        strength,x,y=heapq.heappop(pos)
        if x==a and y==b :
            return strength
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and c[nx][ny]!='#':
                if dist[nx][ny]>strength+abs(int(c[nx][ny])-int(c[x][y])):
                    dist[nx][ny]=strength+abs(int(c[nx][ny])-int(c[x][y]))
                    heapq.heappush(pos,(dist[nx][ny],nx,ny))
    return 'NO'
for _ in range(p):
    x,y,a,b=map(int,input().split())
    if c[x][y]=='#' or c[a][b]=='#':
        print('NO')
        continue
    result=tili(x,y,a,b)
    print(result)