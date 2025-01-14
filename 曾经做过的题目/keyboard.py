f = input()
n = input()
a = ["q","w",'e','r','t','y','u','i','o','p']
b = ['a','s','d','f','g','h','j','k','l',';']
c =['z','x','c','v','b','n','m',',','.','/']
s =[]
if f =="L":
    for i in n:
        if i in a:
            num =int(a.index(i))
            s.append(a[num+1])
        if i in b:
            num =int(b.index(i))
            s.append(b[num+1])
        if i in c:
            num =int(c.index(i))
            s.append(c[num+1])
if f =="R":
    for i in n:
        if i in a:
            num =int(a.index(i))
            s.append(a[num-1])
        if i in b:
            num =int(b.index(i))
            s.append(b[num-1])
        if i in c:
            num =int(c.index(i))
            s.append(c[num-1])
print("".join(s))


#答案版
d = input()
s = input()
kb = 'qwertyuiopasdfghjkl;zxcvbnm,./'

if d=='R':
        for c in s:
                print(kb[kb.index(c) - 1], end='')
else:
        for c in s:
                print(kb[kb.index(c) + 1], end='')

print()