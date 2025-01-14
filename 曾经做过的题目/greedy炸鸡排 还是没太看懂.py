n,k=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
s=sum(c)
while True:
    if s/k < c[-1]:
        s-=c.pop()
        k-=1
    else:
        print('{:.3f}'.format(s/k))
        break