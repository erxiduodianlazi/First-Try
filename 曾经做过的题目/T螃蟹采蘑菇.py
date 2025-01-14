from collections import deque
def bfs1(x1,x2,y):
    q=deque([(x1,x2,y)])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited=[[False]*n for _ in range(n)]
    visited[x1][y]=True
    visited[x2][y]=True
    while q:
        x1,x2,y=q.popleft()
        if c[x1][y]==9 or c[x2][y]==9:
            return True
        for dx,dy in directions:
            nx1,ny=x1+dx,y+dy
            nx2,ny=x2+dx,y+dy
            if 0<=nx1<n and 0<=ny<n and 0<=nx2<n and not visited[nx1][ny] and not visited[nx2][ny] and c[nx1][ny] != 1 and c[nx2][ny] != 1 :
                q.append((nx1,nx2,ny))
                visited[nx1][y] = True
                visited[nx2][y] = True
    return False


def bfs2(x,y1,y2):
    q=deque([(x,y1,y2)])
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    visited=[[False]*n for _ in range(n)]
    visited[x][y1]=True
    visited[x][y2]=True
    while q:
        x,y1,y2=q.popleft()
        if c[x][y1]==9 or c[x][y2]==9:
            return True
        for dx,dy in directions:
            nx,ny1=x+dx,y1+dy
            nx,ny2=x+dx,y2+dy
            if 0<=nx<n and 0<=ny1<n and 0<=ny2<n and not visited[nx][ny1] and not visited[nx][ny2] and c[nx][ny1] != 1 and c[nx][ny2] !=1:
                q.append((nx,ny1,ny2))
                visited[nx][ny1] = True
                visited[nx][ny2] = True
    return False


n=int(input())
c=[list(map(int,input().split())) for i in range(n)]
d=list()

for i in range(n):
    for j in range(n):
        if c[i][j]==5:
            d.append((i,j))

if d[0][0]!=d[1][0]:
    if bfs1(d[0][0],d[1][0],d[0][1]):
        print('yes')
    else:
        print('no')
else:
    if bfs2(d[0][0],d[0][1],d[1][1]):
        print('yes')
    else:
        print('no')



