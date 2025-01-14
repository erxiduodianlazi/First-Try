n = int(input())
m =list(map(int,input().split()))
num=1
s=[]
if n>1:
    for i in range(1,n):
        if m[i-1] <=m[i]:
            num+=1
        elif m[i-1]>m[i]:
            s.append(num)
            num=1
            continue
        s.append(num)
    print(max(s))
else:
    print(1)

#答案版
n = int(input())
a = [int(i) for i in input().split()]
f = [0]*n
f[0]=1
max_m=1
for i in range(1,n):
    if a[i]>=a[i-1]:
        f[i]=f[i-1]+1
        if f[i]>max_m:
            max_m = f[i]
    else:
        f[i]=1