n, k, l, c, d, p, nl, np = list(map(int, input().split()))
a = k * l // nl
b = c * d
c = p // np
s = [a, b, c] #更简单的答案的解法
s.sort()#print(min(a,b,c)//n)
e = s[0]
print(e//n)