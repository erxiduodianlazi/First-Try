n = int(input())
s = []

for i in range(1, n + 1):
    if i % 7 != 0 and '7' not in str(i):
        s.append(str(i))
print(eval("**2+".join(s))-int(s[-1])+int(s[-1])**2)

