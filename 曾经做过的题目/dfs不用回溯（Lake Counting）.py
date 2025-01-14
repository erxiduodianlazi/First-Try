#单纯的递归
import sys
sys.setrecursionlimit(20000)
def dfs(x,y):
    field[x][y]='.'
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
            dfs(nx,ny)

n,m=map(int,input().split())
field=[list(input()) for i in range(n)]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
cnt=0
for i in range(n):
    for j in range(m):
        if field[i][j]=='W':
            dfs(i,j)
            cnt+=1
print(cnt)

#用栈来模拟递归的过程，可以不用写开头那个，可以避免因递归过深而导致的栈溢出问题
def dfs(x,y):
    stack=[(x,y)]
    while stack:
        x,y=stack.pop()
        if field[x][y] != 'W':
            continue
        field[x][y]='.'
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and field[nx][ny]=='W':
                stack.append((nx,ny))

n,m = map(int,input().split())
field =[list(map(int,input().split()))]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
cnt=0
for i in range(n):
    for j in range(m):
        if field[i][j] == 'W':
            dfs(i, j)
            cnt += 1
print(cnt)


