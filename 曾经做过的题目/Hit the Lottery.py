n = int(input())
m = [100,20,10,5,1]
o = 0
p = n
for i in m:
    o += p//n
    p = p%n
print(o)