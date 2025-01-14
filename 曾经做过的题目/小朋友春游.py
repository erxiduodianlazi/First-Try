n = int(input())
m = list(map(int,input().split()))
a =[x for x in range(1,n+1)]
b =[]
for i in m:
    if i>n:
        b.append(i)
    if i<=n:
        a.remove(i)
a.sort()
b.sort()
print(" ".join(map(str,a)))
print(" ".join(map(str,b)))
