n=int(input())
a0,b0=map(int,input().split())
c=[]
for _ in range(n):
    c.append(list(map(int,input().split())))
c.sort(key=lambda x:(x[0]*x[1]))
result=0
for i in range(n):
    result=max(result,a0//c[i][1])
    a0*=c[i][0]
print(result)