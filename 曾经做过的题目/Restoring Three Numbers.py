p = list(map(int,input().split()))
p.sort()
a = p[3]-p[0]
b = p[3]-p[1]
c = p[3]-p[2]
print(a,b,c)
