n,m = [int(x) for x in input().split()]
a = set()
for i in range(n):
    a.update(map(int,input().split()[1:]))
if len(a) == m:
    print("Yes")
else:
    print("No")