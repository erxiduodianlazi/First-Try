N = int(input())
for _ in range(N):
    n,m,b = map(int,input().split())
    c={}
    tl=[]
    for _ in range(n):
        x,y =map(int,input().split())
        if x not in c:
            c[x]=[y]
            tl.append(x)
        else:
            c[x].append(y)
    tl.sort()
    for t in tl:
        d=sum(sorted(c[t],reverse = True)[:m])
        b-=d
        if b<=0:
            print(t)
            break
    else:
        print('alive')


#我想要写的元组未实现，但人家的代码ok版
nCases = int(input())
while nCases > 0:
    nCases -= 1
    n, m, b = [int(i) for i in input().split()]

    skill = []
    for i in range(n):
        t, x = [int(i) for i in input().split()]
        skill.append((t, x))

    sort_skill = sorted(skill, key=lambda a: (a[0], -a[1]))

    if sort_skill[0][1] >= b:
        print(sort_skill[0][0])
        continue

    pre_t = sort_skill[0][0]

    first = True
    cnt = 0
    for e in sort_skill:
        if first:
            b -= e[1]
            cnt += 1
            first = False
            continue

        if e[0] == pre_t:
            cnt += 1
        else:
            cnt = 1
            pre_t = e[0]

        if cnt > m:
            continue

        if e[1] >= b:
            print(e[0])
            break
        else:
            b -= e[1]
    else:
        print('alive')






