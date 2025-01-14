a = [0]*1000001
a[0]=1
a[1]=2
for i in range(2,1000001):
    a[i]=(a[i-1]*2+a[i-2])%32767

n =int(input())
for _ in range(n):
    m = int(input())
    print(a[m-1])