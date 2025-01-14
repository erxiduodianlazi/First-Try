n,m = map(int,input().split())
c=[]
num=0
for i in range(n):
    c.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if c[i][j] *(c[0][j]*1000+c[i][-1]*100+c[-1][j]*10+c[i][0])>num:
            num=c[i][j] *(c[0][j]*1000+c[i][-1]*100+c[-1][j]*10+c[i][0])
print(num)
