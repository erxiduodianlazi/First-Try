def dfs(x,y,c):
    field[x][y]='#'
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and field[nx][ny]==c:
            dfs(nx,ny,c)


for _ in range(int(input())):
    n=int(input())
    field=[list(input()) for i in range(n)]
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    r=0;b=0
    for i in range(n):
        for j in range(n):
            if field[i][j]=="r":
                dfs(i,j,'r')
                r+=1
            if field[i][j]=='b':
                dfs(i,j,'b')
                b+=1
    print(r,b)