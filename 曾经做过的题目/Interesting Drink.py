import bisect
n = int(input())
m = list(map(int,input().split()))
q=int(input())
c =[]
for _ in range(q):
    c.append(int(input()))
m.sort()
for i in c:
    right=bisect.bisect_right(m,i)
    print(right)