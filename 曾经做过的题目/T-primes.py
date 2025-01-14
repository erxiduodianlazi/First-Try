import math
def sieve(limit):
    is_prime=[True]*(limit+1)
    is_prime[0]=False
    is_prime[1]=False
    for i in range(2,int(math.sqrt(limit)+1)):
        if is_prime[i]:
            for j in range(i*i,limit+1,i):
                is_prime[j]=False
    return is_prime


limit=10**6
primelist = sieve(limit)


n =  int(input())
m = map(int,input().split())
for j in m:
    t = math.sqrt(j)
    if int(t)==t:
        g = int(t)
        if primelist[g]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")