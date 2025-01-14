#巧妙地减去
q=int(input())
for _ in range(q):
    n=int(input())
    c=list(map(int,input().split()))
    c.sort(reverse=True)

    b=2048
    you=False
    for i in c:
        if b-i<0:
            continue
        elif b-i>0:
            b-=i
        else:
            you = True
            break
    print('YES' if you else 'NO')
#直接模拟，我想要的是这种，只是不知道要怎么样用语法写出来
q=int(input())
l=[1,2,4,8,16,32,64,128,256,512,1024]
for i in range(q):
    n=int(input())
    s=[int(x) for x in input().split()]

    for j in range(11):
        while s.count(l[j])>1:
            s.remove(l[j])
            s.remove(l[j])
            s.append(2*l[j])

    if 2048 in s:
        print('YES')
    else:
        print('NO')

