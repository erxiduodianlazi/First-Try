#greedy法
n=int(input())
m=list(map(int,input().split()))
if n==1:
    print(1)
elif n==2:
    if m[0]!=m[1]:
        print(2)
    else:
        print(1)
else:
    up=1
    down=1
    for i in range(1,n):
        if m[i]>m[i-1]:
            up=down+1#因为一直上升的话 down是没有改变的，所以up也不会改变
        elif m[i]<m[i-1]:
            down=up+1
    print(max(up,down))
#dp法
n=int(input())
m=list(map(int,input().split()))
if n==1:
    print(1)
elif n==2:
    if m[0]!=m[1]:
        print(2)
    else:
        print(1)
else:
    up=[1]*n;down=[1]*n
    for i in range(1,n):
        if m[i]>m[i-1]:
            up[i]=down[i-1]+1
            down[i]=down[i-1]
        elif m[i]<m[i-1]:
            down[i]=up[i-1]+1
            up[i]=up[i-1]
        else:
            up[i]=up[i-1]
            down[i]=down[i-1]
    print(max(up[-1],down[-1]))

#比较直接的思路
def sgn(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

n=int(input())
m=list(map(int,input().split()))
delta =[sgn(m[i+1]-m[i]) for i in range(n-1)]

result=1
pre=0
for i in range(n-1):
    if pre*delta[i] < 0 or (pre==0 and delta[i]!=0):
        result+=1
        pre = delta[i]
print(result)