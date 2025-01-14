n=int(input())
c=[]
for i in range(n):
    c.append(list(map(int,input().split())))
for i in range(n-2,-1,-1):
    for j in range(i+1):
        c[i][j]=max(c[i][j]+c[i+1][j],c[i][j]+c[i+1][j+1])
print(c[0][0])