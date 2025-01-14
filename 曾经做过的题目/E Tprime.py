import math
def sieve(limit):
    is_prime=[True]*(limit+1)
    is_prime[0]=is_prime[1]=False
    for i in range(2,int(math.sqrt(limit))+1):
        if is_prime[i]:
            for j in range(i*i,limit+1,i):
                is_prime[j]=False
    return is_prime
limit=1000
is_prime_list=sieve(1000)
m,n = map(int,input().split())
for i in range(m):
    c=list(map(int,input().split()))
    num=0
    for j in c:
        if math.sqrt(j)==int(math.sqrt(j)):
            if is_prime_list[int(math.sqrt(j))]:
                num+=j
        else:
            continue
    if num==0:
        print(0)
    else:
        print('{:.2f}'.format(num/len(c)))