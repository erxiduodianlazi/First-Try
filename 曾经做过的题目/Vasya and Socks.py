n,m = map(int,input().split())
z=0
d=0
while True:
    z+=1
    if n>0:
        n-=1
        d+=1
    else:
        break
    if z==m:
        n+=1
        z=0
print(d)
