#不知道为什么不对
g = int(input())
for i in range(g):
    n = int(input())
    c=[]
    for j in range(n):
        a,b=map(int,input().split())
        c.append((a,b))
    merged = set()
    for l in range(len(c)-1):
        if l in merged:
            continue
        for k in range(l+1,len(c)):
            if c[k][0]<=c[l][1] and c[k][1] >= c[l][0]:
                if k not in merged:
                    n-=1
                    merged.add(k)
    print(n)

#标准版
k = int(input())
for _ in range(k):
    n = int(input())
    c=[]
    for _ in range(n):
        a,b = map(int,input().split())
        c.append((a,b))
    c.sort(key = lambda x:x[1])

    last = 0
    test = 0
    for i in range(len(c)):
        if c[i][0] > last:
            last = c[i][1]
            test +=1
    print(test)
