n=int(input())
for _ in range(n):
    dic='ABCDEFGHIJKL'
    g=set()
    light=set()
    heavy=set()
    for _ in range(0,3):
        m,n,zhuangtai=input().split()
        if zhuangtai=='even':
            g.update(m)
            g.update(n)
        elif zhuangtai=='up':
            heavy.update(m)
            light.update(n)
        else:
            light.update(m)
            heavy.update(n)
    for i in dic:
        if i in g:
            continue
        if i in heavy and i not in light:
            print(f'{i} is the counterfeit coin and it is heavy.')
            break#一定要及时break
        elif i in light and i not in heavy:
            print(f'{i} is the counterfeit coin and it is light.')
            break


