from collections import deque
def bfs(i,j,k,l,c):
    q=deque()
    q.append((i,j,k,l))
    visited.append((i,j,k,l))
    while q:
        i,j,k,l=q.popleft()
        if c[i][j]==9 or c[k][l]==9:
            return True
        for dx,dy in directions:
            ni=i+dx;nj=j+dy
            nk=k+dx;nl=l+dy
            if 0<=ni<n and 0<=nj<n and 0<=nk<n and 0<=nl<n and c[ni][nj] !=1 and c[nk][nl] !=1 and (ni,nj,nk,nl) not in visited:
                q.append((ni,nj,nk,nl))
                visited.append((ni,nj,nk,nl))
    return False


directions=[(1,0),(-1,0),(0,1),(0,-1)]
visited=[]
now=[]
n=int(input())
c=[list(map(int,input().split())) for _ in range(n)]
for a in range(n):
    for b in range(n):
        if c[a][b]==5:
            now.append(a)
            now.append(b)
i,j,k,l=now
if bfs(i,j,k,l,c):
    print('yes')
else:
    print('no')