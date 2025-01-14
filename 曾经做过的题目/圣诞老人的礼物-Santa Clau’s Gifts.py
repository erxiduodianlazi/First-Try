n,w = map(int,input().split())
l=[]
m =0
for i in range(n):
    a,b = map(int,input().split())
    c=a/b
    l.append((c,b))
l.sort()
l.reverse()
if w>0:
    for j in range(len(l)):
       c,b = l[j]
       if w>=b:
           m+=c*b
           w-=b
       else:
           m+=c*w
           break

    print(format(m,".1f"))