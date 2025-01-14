import math
n = int(input())
for i in range(n):
    a,b,c=map(float,input().split())
    if b==0:
        b=-b
        if b**2 - 4*a*c ==0:
            num=-b/a/2
            print(f'x1=x2={"%.5f"%num}')
        elif b**2 - 4*a*c >0:
             x1 =  (-b + math.sqrt(b*b-4*a*c))/(2*a)
             x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)
             if x1<x2:
                 x1,x2=x2,x1
             print(f'x1={"%.5f"%x1};x2={"%.5f"%x2};')
        else:
            p =-b/a/2
            q=math.sqrt(-(b*b-4*a*c))/(2*a)
            print(f'x1={"%.5f"%p}+{"%.5f"%q}i;x2={"%.5f"%p}-{"%.5f"%q}i')
  #不对的，oj平台自己也有点问题
  #答案的解法，求q的步骤不同


