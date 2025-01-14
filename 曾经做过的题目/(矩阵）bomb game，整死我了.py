#改改改改终于对了版
A,B,K=map(int,input().split())
c=[[0]*B for _ in range(A)]
t=[]
d=list()
for i in range(K):
    R,S,P,T=map(int,input().split())
    if T==0:
        t.append((R-1,S-1,P,0))
    else:
        t.append((R-1,S-1,P,1))
for i in range(len(t)):
    ban=(t[i][2]-1)//2
    for j in range(max(0,t[i][0]-ban),min(t[i][0]+ban+1,A)):
        for k in range(max(0,t[i][1]-ban),min(t[i][1]+ban+1,B)):
            if t[i][3]==0:
                c[j][k]=-1
            else:
                if c[j][k]!=-1:
                    c[j][k]+=1
for i in range(A):
    for j in range(B):
        d.append(c[i][j])
print(d.count(max(d)))

#chatgpt的简洁版
A,B,K = map(int,input().split())
c=set((i,j) for i in range(1,A+1) for j in range(1,B+1))
for _ in range(K):
    R,S,P,T=map(int,input().split())
    r=(P-1)//2
    bomb_range=set()
    for i in range(max(1,R-r),min(A+1,R+r+1)):#末尾值是取不到的啊啊所以要加以嘛
        for j in range(max(1,S-r),min(B+1,S+r+1)):
            bomb_range.add((i,j))
    if T==1:
        c&=bomb_range
    else:
        c-=bomb_range
print(len(c))
