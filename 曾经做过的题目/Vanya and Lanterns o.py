n,l = map(int,input().split())
m = list(map(int,input().split()))
m.sort()
max_distance=0
for i in range(1,n):
    t = (m[i] - m[i-1])/2
    if t>max_distance:
        max_distance = t
result = format(max(m[0],l-m[-1],max_distance),'.10f')
print(result)