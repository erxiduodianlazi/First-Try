n,m = [int(x) for x in input().split()]
s =list(map(int,input().split()))
s.sort()
a = s[0:m]
price = 0
for i in a:
    if i<0:
        price+=i
print(abs(price))


n,m =map(int,input().split())
p = list(map(int,input().split()))
p.sort()
num=0
for i in p:
    if i<0:
        num+=1
price=sum(p[:min(num,m)])

print(abs(price))
