#自己写的劣质的哈
n = int(input())
c=[]
for _ in range(n):
    c.append(tuple(map(int,input().split())))
i=1
if n>1:
    num=2
else:
    num=1
k=[0]*n
for i in range(1,n-1):
    if c[i][0]-c[i][1]>c[i-1][0]+k[i-1]:
        num+=1
    else:
        if c[i][0]+c[i][1]<c[i+1][0]:
            num+=1
            k[i]=c[i][1]
print(num)