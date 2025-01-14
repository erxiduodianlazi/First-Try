#错的错的不知道为什么错但是不想管了呵呵
t= int(input())
for _ in range(t):
    n = int(input())
    ai=list(map(int,input().split()))
    bi=list(map(int,input().split()))
    c=[(a,b,b-a) for a in ai for b in bi]
    c.sort(key = lambda x:x[2])
    d=[]
    for i in range(len(c)):
        d.append(c[i][0])
    min_time = min(max(ai),sum(bi))
    for i in range(len(c)-1):
        bt = sum(x[1] for x in c[:i])
        at = max(d[i+1:])
        min_time=min(max(at,bt),min_time)
    print(min_time)
#答案的贪心算法
t= int(input())
ans=[]
for _ in range(t):
    n = int(input())
    ai=list(map(int,input().split()))
    bi=list(map(int,input().split()))
    c=sorted(list(zip(ai,bi)),reverse=True)
    d=0
    for i in range(n):
        d+=c[i][1]
        if c[i][0]<=d:
            d=max(c[i][0],d-c[i][1])#除了当前自取时间外之前的自取时间
            break
    ans.append(d)
print('\n'.join(map(str,ans)))
