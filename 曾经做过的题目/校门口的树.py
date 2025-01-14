L,M=map(int,input().split())
s = set()
for i in range(M):
    m,n=map(int,input().split())
    s.update(range(m,n+1))
k = len(s)
print(L+1-k)

L,M=map(int,input().split())
n = [False] * (L+1)
for i in range(M):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        n[j] = True
print(n.count(False))
#答案的

L,M=map(int,input().split())
s = set()
for i in range(M):
    m,n=map(int,input().split())
    s.update(range(m,n+1))
k = len(s)
print(L+1-k)

