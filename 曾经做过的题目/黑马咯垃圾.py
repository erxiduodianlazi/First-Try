k = int(input())
s = input()
x = 'zyxwvutsrqponmlkjihgfedcba'
b=[]
for i in s:
    t = i.lower()
    c = int(x.index(t)) + k
    if c <= 25:
        if i.isupper():
            b.append(x[c].upper())
        else:
            b.append(x[c].lower())
    else:
        if i.isupper():
            b.append(x[int(c % 26)].upper())#改成直接除以26就对了
        else:
            b.append(x[int(c % 26)].lower())
print(''.join(b))

#终于对了版
k = int(input())
s = input()
b='abcdefghijklmnopqrstuvwxyz'
c=[]
for i in s:
    t = i.lower()
    d = int(b.index(t))-k
    if i.isupper():
        c.append(b[d%26].upper())
    else:
        c.append(b[d%26])
print(''.join(c))

k = int(input())
s = input()
c=[]
a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b='abcdefghijklmnopqrstuvwxyz'
for i in s:
    if i in a:
        c.append(chr((ord(i)-ord('A')-k)%26+ord('A')))
    else:
        c.append(chr((ord(i)-ord('a')-k)%26+ord('a')))
print(''.join(c))