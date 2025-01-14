from turtledemo.chaos import jumpto

t = int(input())
for i in range(t):
    n,k=map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    v = sorted((a[i],i) for i in range(n))
    b.sort()
    result=[0] * n
    for i in range(n):
        result[v[i][1]] = b[i]
    print(" ".join(map(str,result)))


