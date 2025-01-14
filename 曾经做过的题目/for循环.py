n,k = [ int(x) for x in input().split()]
l = [int(x) for x in input().split()]
num = 0
s = l[k-1]
for i in range(n):
    t = l[i]
    if t>= s and t >0:
        num += 1
print(num)