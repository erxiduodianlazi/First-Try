#别人写的很简单的你还能看懂的
n=int(input())
M=int(1e5)
a=[0]*(M+1)
for x in map(int,input().split()):
    a[x]+=1

dp=[[0,0] for i in range(M+1)]
for j in range(1,M+1):
    dp[j][0]=max(dp[j-1][0],dp[j-1][1])
    dp[j][1]=dp[j-1][0]+a[j]*j
print(max(dp[M][1],dp[M][0]))

#哇塞是根本不会的dp我完蛋咯
n = int(input())
c=[0]*100001
for m in map(int,input().split()):
    c[m]+=1
dp=[0]*100001
dp[1]=c[1]
for i in range(2,100001):
    dp[i]=max(dp[i-1],dp[i-2]+c[i]*i)

print(max(dp))


#写了一堆根本不对哈哈哈
n = int(input())
m = list(map(int, input().split()))
if n==1:
    print(m[0])
else:
    m.sort()
    c=[]
    num = 1

    # 统计每个数字的频次
    for i in range(1, n):
        if m[i] == m[i - 1]:
            num += 1
        else:
            c.append((m[i - 1], num, 1))
            num = 1
    c.append((m[-1], num, 1))

    # 动态规划数组初始化
    dp = [float('-inf')] * (len(c) + 1)
    dp[0] = 0

    for i in range(1, len(c)):
        if c[i][2] > 0:
            dp[i] = max(dp[i], dp[i - 1] + c[i][0] * c[i][1])

            # 检查边界并处理相邻相同数字的情况
            if i > 0 and c[i - 1][0] == c[i][0]:
                c[i - 1] = (c[i - 1][0], c[i - 1][1], 0)
            if i < len(c) - 1 and c[i + 1][0] == c[i][0]:
                c[i + 1] = (c[i + 1][0], c[i + 1][1], 0)
        else:
            dp[i] = dp[i - 1]

    print(max(dp))


