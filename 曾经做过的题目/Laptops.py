n = int(input())
v = []
for _ in range(n):
    a,b = map(int,input().split())
    v.append((a,b))
v.sort()
for i in range(1,n):
    if v[i][1] < v[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")