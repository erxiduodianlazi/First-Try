import math

t = int(input())
for _ in range(t):
    n = int(input())
    sumv = n*(n+1)//2

    maxp = int(math.log2(n))

    for i in range(maxp + 1):
        sumv -= 2 * (2 ** i)

    print(sumv)




#总是超时版
t = int(input())
for _ in range(t):
    n = int(input())
    b=[]
    for i in range(1,n+1):
        if i&(i-1)==0:
            b.append(-i)
        else:
            b.append(i)
    print(sum(b))
#ai优化版还是超时了笑死人了
t = int(input())
for _ in range(t):
    n = int(input())
    total_sum=0
    for i in range(1,n+1):
        if i&(i-1)==0:
            total_sum -=i
        else:
            total_sum+=i
    print(total_sum)
#ai再try：
import math
t = int(input())
for _ in range(t):
    n = int(input())
    total_sum=n*(n+1)//2

    maxp=int(math.log2(n))
    for i in range(maxp+1):
        total_sum -= 2*(2**i)
    print(total_sum)


