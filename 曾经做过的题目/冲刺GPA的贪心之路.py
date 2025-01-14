h = int(input())
h*=2
m=int(input())
l=[]
num=0;cnt=0
for i in range(m):
    s,c=map(float,input().split())
    l.append((s,c))
h-=m*0.5
l.sort(key = lambda x:(x[0]*x[1]),reverse = True)
while h>0:
    for s,c in l:
        add=min(5,h*s)
        num+=add*c
        h-=add/s
        cnt+=1
    if cnt==m:
            break
print(format(num,".1f"))
