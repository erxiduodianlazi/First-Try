a=[]
m=[]
while True:
    try:
        s=input().split()
        if s[0]=='pop':
            if a:
                a.pop()
                if m:
                    m.pop()
        elif s[0]=='min':
            if m:
                print(m[-1])
        else:
            num=int(s[1])
            a.append(num)
            if not m:
                m.append(num)
            else:
                m.append(min(num,m[-1]))
    except EOFError:
        break