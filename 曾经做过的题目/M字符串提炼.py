import math
s=input()
s2=[]
m1=[]
result=[]
n=len(s)
m=int(math.log(n,2))
for i in range(m+1):
    m1.append(s[2**i-1])
k=0
j=len(m1)-k-1
while k<=j:
    if k==j:
        s2.append(m1[k])
        break
    else:
        s2.append(m1[k])
        s2.append(m1[j])
        k+=1
        j-=1

print(''.join(map(str,s2)))

