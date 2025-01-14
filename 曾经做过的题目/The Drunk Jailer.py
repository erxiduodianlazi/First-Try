t = int(input())
for _ in range(t):
    n = int(input())
    lst = [0]*n
    for i in range(2,n+1):
        for j in range(i-1,n,i):
            lst[j]^=1
    print(lst.count(0))

import math
t = int(input())
for _ in range(t):
    n = int(input())
    print(int(math.sqrt(n)))