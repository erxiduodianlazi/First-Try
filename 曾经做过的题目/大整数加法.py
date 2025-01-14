#好蠢，写了半天在干嘛，自己写出来o的
print(int(input()) + int(input()))

#字符串解法等下再看ww


m = input()
n = input()
c=[]
if len(m)==len(n):
    print(int(m)+int(n))
else:
    if len(m)>len(n):
        a = len(m)-len(n)
        n=[str(i) for i in n]
        n.insert(0,'0'*a)
        n = ''.join(n)
    else:
        b = len(n)-len(m)
        m=[str(i) for i in m]
        m.insert(0,'0'*b)
        m=''.join(m)
    print(int(m)+int(n))
#以上是对的，补零就行



#进位算了好幽默的依托
m = input()
n = input()
c=[]
if len(m)==len(n):
    print(int(m)+int(n))
else:
    if len(m)>len(n):
        a = len(m)-len(n)
        n=[str(i) for i in n]
        n.insert(0,'0'*a)
        n.reverse()
        n = ''.join(n)
    else:
        b = len(n)-len(m)
        m=[str(i) for i in m]
        m.insert(0,'0'*b)
        m.reverse()
        m=''.join(m)
    c = [0]*len(m)
    for i in range(len(m)):
        d =int(m[i])+int(n[i])
        if d != 0 and d+c[i]<10:
            c[i]=d
        elif d+c[i]>10:
            c[i]=(d+c[i])-10
            c[i+1]=1
    c.reverse()

    print(''.join(map(str,c)))

