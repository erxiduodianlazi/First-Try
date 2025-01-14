n = int(input())
t =[]
g ={}
for b in range(2,n+1):
    bc = b**3
    for c in range(b,n):
        cc=c**3
        for d in range(c,n):
            dc=d**3
            s = bc +cc+dc
            if s not in g:
                g[s]=[]
            g[s].append((b,c,d))
for a in range(2,n+1):
    ac=a**3
    if ac in g:
        for (b,c,d) in g[ac]:
          t.append((a,b,c,d))
t.sort(key=lambda x: (x[0],x[1],x[2],x[3]))
for j in range(len(t)):
    print(f'Cube = {t[j][0]}, Triple = ({t[j][1]},{t[j][2]},{t[j][3]})')

#答案版 用 from functools import lru_cache 缓存计算数据
from functools import lru_cache

@lru_cache(maxsize=128)
def check_cubes(a, b, c, d):
    return a ** 3 == b ** 3 + c ** 3 + d ** 3

n = int(input())
for a in range(2,n+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if check_cubes(a,b,c,d):
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
#列表版

n = int(input())
m = [i**3 for i in range(n+1)]
for a in range(2,n+1):
    for b in range(2,a):
        for c in range(b,a):
            for d in range(c,a):
                if m[a]==m[b]+m[c]+m[d]:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
