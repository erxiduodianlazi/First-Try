n = int(input())
n = bin(n)
x = True
b = n.replace(n[0:2],"")
j = len(b)
m = b[::-1]
for i in range(j):
    if b[i] != m[i]:
        x = False
        break
print(["No","Yes"][x])