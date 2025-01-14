sentence=''
s=0
ss=0
sums=[]
for j in range(1,33000):
    sentence+=str(j)
    s+=len(str(j))
    ss+=s
    sums.append(ss)

t=int(input())
for _ in range(t):
    n=int(input())
    #注意排除常数
    if n==1:
        print(1)
    else:
        for i in range(len(sums)):
            if n<=sums[i]:
                offset=n-sums[i-1]-1
                print(sentence[offset])
                break



#春竹打法又超内存了哈，看看人家cop怎么写的,而且是错的，只可能存在一到九和0的数字，你这样减去是铁得不到一到九的
t=int(input())
x=1
c=[(0,0)]

for i in range(1,66000):
    c.append((i,c[i-1][1]+i))

for _ in range(t):
    n=int(input())
    i=1
    while i<len(c)-1 and not (c[i][1]<=n<c[i+1][1]):
        i+=1
    print(i)
    print(c[i+1][1])
    print(c[i+1][0])
    if n==c[i][1]:
        num=c[i][0]
    else:
        num=c[i+1][0]-(c[i+1][1]-n)
    print(num)

