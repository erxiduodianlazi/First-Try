n,m = map(int,input().split())
mx =[[0]*(m+2) for j in range(n+2)]
c=[]
for _ in range(n):
  c.append(list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(1,m+1):
        mx[i][j]=c[i-1][j-1]
new_mx = [[0]*(m+2) for j in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        x =mx[i-1][j-1]+mx[i-1][j]+mx[i-1][j+1]+mx[i][j-1]+mx[i][j+1]+mx[i+1][j-1]+mx[i+1][j]+mx[i+1][j+1]
        if mx[i][j]==1:
            if x<2:
                new_mx[i][j]=0
            elif x==2 or x==3:
                new_mx[i][j]=1
            else:
                new_mx[i][j]=0
        else:
            if x==3:
                new_mx[i][j]=1
for i in range(1,n+1):
    print(' '.join(map(str,new_mx[i][1:m+1])))
