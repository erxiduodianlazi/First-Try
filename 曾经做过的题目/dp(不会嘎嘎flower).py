t,k=map(int,input().split())
dp=[1]+[0]*100000
s=[0]*100001
chu=1000000007#用来取模的数，防止数据过大产生错误
for i in range(1, 100001):
    if i >= k:
        dp[i] = (dp[i-1] + dp[i-k]) % chu
    else:
        dp[i] = dp[i-1] % chu
    s[i] = s[i-1] + dp[i]
for _ in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1])%chu)

