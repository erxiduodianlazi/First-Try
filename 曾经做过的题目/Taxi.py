import math
n = int(input())
m =list(map(int,input().split()))
num4=m.count(4)
num3=m.count(3)
num2=math.ceil(m.count(2)/2)
num1=m.count(1)
num=num2+num3+num4
if num1>num3:
    num1-=num3
else:
    num1=0
if num1>m.count(2)%2:
    num1-=m.count(2)%2*2
else:
    num1=0
num+=math.ceil(num1/4)

print(num)
#答案简洁版
a,b,c,d = map(input().count,('1','2','3','4'))
print(c+d+math.ceil((b*2+max(0,a-c))/4))
