import math
t=int(input())
for i in range(t):
    n=int(input())
    result=n*(n+1)//2
    result-=2*(2**(int(math.log(n,2))+1)-1)
    print(int(result))
