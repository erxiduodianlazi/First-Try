t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    m = list(map(int,input().split()))
    i=0
    j=n-1
    if sum(m) % x !=0:
        print(n)
    else:
        while i < n and m[i]%x == 0:
            i+=1
        while j>0 and m[j]%x == 0:
            j-=1
        if i == n:
            print(-1)
        else:
            print(max(n-i-1,j))
