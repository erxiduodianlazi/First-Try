n = int(input())
t = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
g = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

for j in range(n):
    m = str(input())
    num = 0
    for i in range(17):
        num += int(m[i]) * t[i]
    num = num % 11
    if g[num] == m[-1]:
        print("YES")
    else:
        print("NO")
