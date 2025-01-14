a,b = map(int,input().split())
x = True
y = []
for i in range(a-1,b+1):
    j = str(i)
    if int(j[0])**3 +int(j[1])**3 +int(j[2])**3 == i:
        y.append(j)
        x = False
if x:
    print("NO")
else:
    print(" ".join(y))

#也可以
if y:
    print(" ".join(y))
else:
    print("NO")