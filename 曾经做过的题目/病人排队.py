n = int(input())
c=[]
d=[]
for i in range(n):
    m,n=map(str,input().split())
    if int(n)>= 60:
        d.append((m,n))
    else:
        c.append((m,n))
d.sort(key=lambda x: -int(x[1]))
for i in d:
    print(i[0])
for j in c:
    print(j[0])