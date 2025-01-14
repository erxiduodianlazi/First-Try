import math
def is_prime(limit):
    primes = [True]*(limit+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(limit)+1)):
        if primes[i]:
            for j in range(i*i,limit,i):
                primes[j]=False
    return primes


n = int(input())
limit=n
is_prime_list=is_prime(limit)
c=[]

for i in range(n):
    if is_prime_list[i]:
        j=n-i
        if is_prime_list[j] is False:
            continue
        else:
            c.append((i,j,abs(i-j)))

c.sort(key = lambda x:x[2])
a=c[0][0]
b=c[0][1]
print(a*b)


#答案版，通过比较而不通过推断
S = int(input())


def isprime(n):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            return False
    else:
        return True


maxmultiple = 0
f = 2
while f < S:
    if isprime(S - f):
        maxmultiple = max(maxmultiple, f * (S - f))

    f += 1
    while isprime(f) == False:
        f += 1

print(maxmultiple)