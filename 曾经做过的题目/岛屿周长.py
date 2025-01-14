dic={0:4,1:3,2:2,3:1,4:0}
def zhou(n,m,d):
    c=[[0]*(m+2) for _ in range(n+2)]
    num=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            c[i][j]=d[i-1][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if c[i][j]==1:
                num+=dic[c[i-1][j]+c[i][j-1]+c[i][j+1]+c[i+1][j]]
    return num


n,m = map(int,input().split())
d=[]
for _ in range(n):
    d.append(list(map(int,input().split())))
print(zhou(n,m,d))


#答案只要打一个表就可以了
n,m = map(int,input().split())
l = [[0]*(m+2)] +[[0] +list(map(int,input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]
ans = 0
for i in range(1,n+1):
    for j in range(1, m + 1):
        if l[i][j] == 1:
            ans += 4-l[i+1][j]-l[i][j+1]-l[i-1][j]-l[i][j-1]
print(ans)