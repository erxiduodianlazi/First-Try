directions=[(-1,0),(1,0),(0,-1),(0,1)]
from collections import deque
def bfs(x,y):
    q=deque()
    q.append((x,y))
    iq[x][y]=True
    step=0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if c[x][y] == 1:
                return step
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and not iq[nx][ny] and c[nx][ny] !=2:
                    q.append((nx,ny))
                    iq[nx][ny]=True
        step+=1
    return 'NO'


m,n=map(int,input().split())
iq=[[False]*n for _ in range(m)]
c=[list(map(int,input().split())) for i in range(m)]
print(bfs(0,0))

