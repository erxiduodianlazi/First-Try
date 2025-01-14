n,q=map(int,input().split())
c=[]
like = False
for _ in range(q):
    c.append(tuple(map(int,input().split())))
for i in range(q):
    for j in range(q):
        for k in range(q):
            if c[i][0]==c[k][1] and c[i][1]==c[j][0] and c[j][1]==c[k][0]:
                like = True
                break
if like:
    print("Yes")
else:
    print("No")



