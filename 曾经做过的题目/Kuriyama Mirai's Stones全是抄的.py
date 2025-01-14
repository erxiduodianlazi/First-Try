n = int(input())
j = list(map(int,input().split()))
prefix_sum = [0]*(n+1)
for i in range(1,n+1):
    prefix_sum[i] = prefix_sum[i - 1] + j[i - 1]
t = sorted(j)
sorted_prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    sorted_prefix_sum[i] = sorted_prefix_sum[i - 1] + t[i - 1]

m = int(input())
for i in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        print(prefix_sum[c]-prefix_sum[b-1]  )
    else:
        print(prefix_sum[c]-prefix_sum[b-1] )