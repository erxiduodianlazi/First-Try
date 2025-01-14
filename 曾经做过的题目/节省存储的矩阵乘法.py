n,m1,m2=map(int,input().split())
x=[[0]*n for i in range(n)]
y=[[0]*n for j in range(n)]
z=[[0]*n for k in range(n)]
for i in range(m1):
    a,b,c = map(int,input().split())
    x[a][b]=c
for j in range(m2):
    d,e,f = map(int,input().split())
    y[d][e]=f
for i in range(n):
    for j in range(n):
        for l in range(n):
            z[i][j]+=x[i][l]*y[l][j]
        if z[i][j] != 0:
            print(i,j,z[i][j])