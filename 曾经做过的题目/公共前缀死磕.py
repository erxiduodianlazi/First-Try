n = int(input())
b = []
num = 0
for _ in range(n):
    a = input()
    b.append((a, len(a)))
b.sort(key=lambda x: x[1])
for i in range(b[0][1]):
    for j in range(1, n):
        if b[j][0][i] == b[j - 1][0][i]:
            num+=1
        else:
            break

if num < n-1 and num % (n - 1) != 0:
    print()
else:
    d = num // (n - 1)
    print(b[0][0][0:d])

