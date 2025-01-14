from functools import lru_cache

@lru_cache(maxsize=None)

def sou(n,m):
    if n==m:
        return True
    elif n<m or n%3 != 0:
        return False
    return sou(n//3,m) or sou(2* n//3,m)


t=int(input())
for i in range(t):
    n,m = map(int,input().split())
    if sou(n,m):
        print("YES")
    else:
        print("NO")

#又错了大姐别写你那个东西了，想得太简单了）
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dp=[0]*(n+1)
    if n==m:
        print("YES")
    elif n%3 !=0 or n<m:
        print("NO")
    else:
        n=n//3
        dp[m]=1
        for i in range(1,n+1):
            dp[3*i]=dp[i]+dp[2*i]
        if dp[n*3]>0:
            print("YES")
        else:
            print("NO")