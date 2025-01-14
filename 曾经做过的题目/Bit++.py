n = input()
m = 0
for i in range(int(n)):
    x = input()
    if "++"  in x:
        m += 1
    elif "--"  in x:
        m -= 1
print(m)
