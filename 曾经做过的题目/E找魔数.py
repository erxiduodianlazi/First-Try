import math
c=set()
for i in range(1,32):
    c.add(i**2)
n=int(input())
m=list(map(int,input().split()))
for i in m:
    for j in range(int(math.sqrt(i)),0,-1):
        d=i-j**2
        if d in c:
            print(bin(i),oct(i),hex(i))
            break

