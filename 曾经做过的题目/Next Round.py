n,k =list(map(int,input().split()))
a = [int(x) for x in input().split()]
m = a[k-1]
num = 0
for i in a:
    if i >=m and i != 0:
        num += 1
print(num)
