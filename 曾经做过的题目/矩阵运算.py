A,B,C=[],[],[]
a,b = map(int,input().split())
for i in range(a):
    A.append(list(map(int,input().split())))
c,d = map(int,input().split())
for i in range(c):
    B.append(list(map(int,input().split())))
e,f = map(int,input().split())
for i in range(e):
    C.append(list(map(int,input().split())))
if b!=c or a!=e or d!=f:
    print("Error!")
else:
    for i in range(e):
        for j in range(f):
            C[i][j]+=sum(A[i][p]*B[p][j] for p in range(b))
    for i in range(e):
        print(" ".join(str(j) for j in C[i]))#下面是另一种做法
        print(*C[i])#将c【i】这一行元素分开打印出来
