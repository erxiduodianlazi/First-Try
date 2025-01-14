p = int(input())
n = [int(x) for x in input().split()]
n.sort()

cnt=0
i=0
j=len(n)-1

while i<=j:
    if p>=n[i]:
        p-=n[i]
        cnt+=1
        i+=1
    else:
        if j == i:
            break
        if cnt>0:
            p+=n[j]
            cnt-=1
            j-=1
        else:
            break
print(cnt)

