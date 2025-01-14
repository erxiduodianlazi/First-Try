import math
n = int(input())
dic={0:"Sunday",
     1:"Monday",
     2:"Tuesday",
     3:"Wednesday",
     4:'Thursday',
     5:'Friday',
     6:'Saturday'}
for _ in range(n):
    x=list(map(int,input()))
    y =x[2]*10+x[3]
    c =x[0]*10+x[1]
    d =x[6]*10+x[7]
    if x[4]==0:
        if x[5]==1:
            x[5]=13
            if y>=1:
                y-=1
            else:
                c-=1
                y=99
        elif x[5]==2:
            x[5]=14
            if y>=1:
                y-=1
            else:
                c-=1
                y=99
        m = x[5]
    else:
        m = x[4]*10+x[5]
    b=(y+math.floor(y/4) +math.floor(c/4)-2*c+math.floor((26*m+26)/10)+d-1)%7
    print(dic[b])

import math
l = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
n=int(input())
for i in range(n):
    a = input()
    c = int(a[0:2])
    y = int(a[2:4])
    m = int(a[4:6])
    d = int(a[4:8])
    if m <=2:
        m+=12
        if y>0:
            y-=1
        else:
            c-=1
            y =99





