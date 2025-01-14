t = int(input())
for i in range(t):
    a,b,c = [int(x) for x in input().split()]
    if a+b ==c or a+c==b or b+c==a:
        print("YES")
        continue
    print("NO")



#answer  guanfang
t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] == a[2]:
        print("YES")
    else:
        print("NO")