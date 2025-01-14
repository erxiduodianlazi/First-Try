#自己想出思路+问ai如何分割 最后ac了好开心TT
n,m = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
d=[]
f=set()
g=[]
num=0
for i in range(1,n):
    d.append((c[i]-c[i-1],i))
d.sort(key = lambda x :x[0],reverse=True)
f.update(d[i][1] for i in range(m-1))
f.add(n)
sorted_f = sorted(f)
start = 0
divide = []
for end in sorted_f:
    divide.append(c[start:end])
    start = end
for k in divide:
    num+=k[-1]-k[0]
print(num)

#答案（差异相加到一定程度再减去最大差

