n=int(input())
c=list(map(int,input().split()))
c.sort()
a=[int(i) for i in range(1,n+1)]
b=[]
for i in c:
    if i>n:
        b.append(i)
    else:
        a.remove(i)
a.sort()
b.sort()
print(' '.join(map(str,a)))
print(' '.join(map(str,b)))