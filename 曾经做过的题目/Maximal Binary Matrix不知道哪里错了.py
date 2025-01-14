n, k = map(int, input().split())
num = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if k>1 and i != j:
            num[i][j]=num[j][i]=1
            k-=2
        elif k>0 and i ==j:
            num[i][i]=1
            k-=1
if k==0:
    for row in num:
        print(*row)
else:
    print(-1)


#不知道为什么一直不对，不能先把对角线填满，有时候先填满前面
n,k = map(int,input().split())
c=[[0]*n for i in range(n)]
if k<=n:
    i=0
    while k>0:
        c[i][i]=1
        i+=1
        k-=1
    for i in range(n):
        print(' '.join(map(str,c[i])))
elif k> n**2:
    print(-1)
else:
    k-=n
    if k%2 !=0 :
        print(-1)
    else:
        for i in range(n):
            c[i][i]=1
        while k>0:
            for i in range(n):
                for j in range(i+1,n):
                    c[i][j]=c[j][i]=1
                    k-=2
                    if k==0:
                        break
                if k==0:
                    break

        for i in range(n):
            print(' '.join(map(str,c[i])))