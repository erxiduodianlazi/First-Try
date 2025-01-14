# pylint: skip-file
import sys
sys.setrecursionlimit(20000)

def dfs(x,y,c):
    global cnt
    c[x][y]='.'
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M and c[nx][ny]=='W':
            cnt+=1
            dfs(nx,ny,c)


for _ in range(int(input())):
    N,M=map(int,input().split())
    c=[list(input()) for i in range(N)]
    max_number=0
    directions=[(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(1,-1),(-1,-1)]
    for i in range(N):
        for j in range(M):
            if c[i][j]=='W':
                cnt=1
                dfs(i,j,c)
                max_number=max(max_number,cnt)
    print(max_number)