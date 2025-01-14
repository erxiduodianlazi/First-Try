n = int(input())
s=[]
m = []
t = []
for _ in range(n):
    a,b,c = map(int,input().split())
    s.append(a)
    m.append(b)
    t.append(c)
if sum(s) ==0and sum (m)==0 and sum(t)==0:
    print("YES")
else:
    print("NO")
