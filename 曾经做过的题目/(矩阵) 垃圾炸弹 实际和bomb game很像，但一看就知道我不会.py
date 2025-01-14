#写了依托又是错的哈，学学别人怎么写的
D=int(input())
n=int(input())
c=[]
for _ in range(n):
    x,y,i=map(int,input().split())
    c.append((x,y,i))
c.sort(key = lambda x:(x[0],x[1]))
d=[[0,0,0] for _ in range(n)]
j=0
d[0][0]=c[0][0]+D*2
d[0][1]=c[0][1]+D*2
d[0][2]=c[0][2]
for i in range(1,n):
     if c[i][1]<= d[j][1] and c[i][0]<=d[j][0]:
        d[j][2]+=c[i][2]
     else:
        j+=1
        d[j][1]=c[i][1]+D*2
        d[j][0]=c[i][0]+D*2
        d[j][2]=c[i][2]
d.sort(key = lambda x:(x[2]),reverse=True)
num=1
shu=d[0][2]
for i in range(1,len(d)):
    if d[i][2]==d[0][2]:
        num+=1
    else:
        break
print(num,shu)

#gpt 的滑动窗口？
d=int(input())
n=int(input())
c=[[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,k=map(int,input().split())
    for i in range(max(0,x-d),min(x+d+1,1025)):
        for j in range(max(0,y-d),min(y+d+1,1025)):
            c[i][j]+=k

num=0
shu=0
for i in range(1025):
    for j in range(1025):
        if c[i][j]>num:
            num=c[i][j]
            shu=1
        elif c[i][j]==num:
            shu+=1
print(shu,num)