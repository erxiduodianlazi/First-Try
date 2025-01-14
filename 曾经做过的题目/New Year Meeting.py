#本人
x,y,z= list(map(int,input().split()))
output=()
if x<y<z :
    output=z-x
elif x<z<y:
    output=y-x
elif y<x<z:
    output=z-y
elif y<z<x:
    output=x-y
elif z<x<y:
    output=y-z
elif z<y<x:
    output=x-z
print(output)

#简洁的答案
x = list(map(int,input().split()))
x.sort()
print(x[-1]-x[0])