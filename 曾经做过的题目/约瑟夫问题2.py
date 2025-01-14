while True:
    n,p,m=map(int,input().split())
    if n+p+m==0:
        break
    index=0
    l = list(range(p, n + 1)) + list(range(1, p))
    c=[]
    while len(l)>0:
        index+=1
        z=l.pop(0)
        if index==m:
            c.append(z)
            index=0
        else:
            l.append(z)
    print(','.join(map(str,c)))