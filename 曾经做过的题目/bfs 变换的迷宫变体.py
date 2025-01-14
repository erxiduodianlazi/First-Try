from collections import deque
def bfs(x,y):
    visited=set()
    visited.add((0,x,y))
    q=deque([(0,x,y)])
    while q:
        time,x,y=q.popleft()
        if m[x][y]=="E":
            return time
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c  and ((time+1)%k,nx,ny) not in visited:
                if m[nx][ny]!='#' or (time+1)%k==0:
                    q.append((time+1,nx,ny))
                    visited.add(((time+1)%k,nx,ny))
    return "Oop!"


directions=[(1,0),(-1,0),(0,1),(0,-1)]
t=int(input())
for _ in range(t):
    r,c,k=map(int,input().split())
    m=[list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if m[i][j]=='S':
                print(bfs(i,j))



#错了，是不对的
from collections import deque
def bfs(x,y):
    q=deque()
    q.append((x,y,0))
    visited[x][y]=True
    while q:
        x,y,time=q.popleft()
        if m[x][y]=='E':
            return time
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if time%k==0:
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                    q.append((nx,ny,time+1))
                    visited[nx][ny]=True
            else:
                if 0<=nx<r and 0<=ny<c and m[nx][ny] =='.' and not visited[nx][ny]:
                    q.append((nx,ny,time+1))
                    visited[nx][ny]=True
    return 'Oop!'


T=int(input())
directions=[(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(T):
    r,c,k=map(int,input().split())
    visited=[[False]*c for _ in range(r)]
    m=[input() for i in range(r)]
    x=0;y=0
    for i in range(r):
        for j in range(c):
            if m[i][j]=='S':
                x,y=i,j
                break
        else:
            break
    print(bfs(x,y))
