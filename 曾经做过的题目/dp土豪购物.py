c=list(map(int,input().split(',')))
dp1=[0]*len(c)
dp2=[0]*len(c)
dp1[0]=dp2[0]=c[0]
for i in range(1,len(c)):
    dp1[i]=max(c[i],dp1[i-1]+c[i])
    dp2[i]=max(dp1[i-1],dp2[i-1]+c[i],c[i])
print(max(dp2))