#搞了很久还是不对版
while True:
    R,n = map(int,input().split())
    if R==n==-1:
        break
    x = list(map(int,input().split()))
    x.sort()
    js = len(x)
    i=1
    j=[1]*(len(x)+2)
    while i>=1 and i<len(x)-1:
        if x[i]-x[i-1] <=R and x[i+1]-x[i] > R:
            js-=j[i-1]
            j[i]=j[i-1]=0
            i+=1
        elif x[i]-x[i-1]<=R and x[i+1]-x[i]<=R:
            if i>1:
                if j[i]+j[i-1]+j[i-2]==0:
                    i+=1
                    continue
            js -= j[i - 1]
            js -= j[i + 1]
            j[i - 1] = j[i] = j[i + 1] = 0
            i+=1
        elif x[i]-x[i-1]>R and x[i+1]-x[i]<=R:
            js-=j[i+1]
            j[i]=j[i+1]=0
            i+=1
        else:
            i+=1
    print(js)
#应该使用的贪心版
while True:
    R,n = map(int,input().split())
    if R==n==-1:
        break
    c=list(map(int,input().split()))
    c.sort()
    cnt=0
    i=0
    while i<n:
        cnt+=1
        s=c[i]
        i+=1
        while i<n and c[i] <= s+R:
            i+=1

        p = c[i-1]
        while i<n and c[i] <= p+R:
            i+=1
    print(cnt)
