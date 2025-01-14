n,a,b=map(int,input().split())
a1=a;b1=b
c=list(map(int,input().split()))
num=0
i=0;j=n-1
while i<=j:
    if i==j:
        if max(a,b)>=c[i]:
            break
        else:
            num+=1
            break
    else:
        if a>=c[i]:
            a-=c[i]
        elif a<c[i]:
            a=a1
            a-=c[i]
            num+=1
        if b>=c[j]:
            b-=c[j]
        elif b<c[j]:
            b=b1
            b-=c[j]
            num+=1
        i+=1;j-=1
print(num)

