m,n,p,q = map(int,input().split())
c=[]
d=[]
for _ in range(m):
    c.append(list(map(int,input().split())))
for _ in range(p):
    d.append(list(map(int,input().split())))
e =[[0 for j in range(n+1-q)] for i in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for k in range(p):
            for l in range(q):
                e[i][j]+=c[i+k][j+l]*d[k][l]
for i in range(m+1-p):
    print(' '.join(map(str,e[i])))