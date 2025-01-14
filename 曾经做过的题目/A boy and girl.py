a = list(input())
print(a)
b = 0
for i in a:
    for j in a.remove(i):
        if i == j:
            b += 1
print(b)
#不行啊啊啊啊不可以这么做，好像只能拿集合做

a = set(input())
b = len(a)
print(b)




