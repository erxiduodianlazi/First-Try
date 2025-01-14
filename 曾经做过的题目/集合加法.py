n = int(input())
for _ in range(n):
    s = int(input())
    A = int(input())
    a = list(map(int,input().split()))
    B = int(input())
    b = list(map(int,input().split()))
    x = {}
    for i in a:
       if s-i in x:
           x[s-i] += 1
       else:
           x[s-i]=1
    num = 0
    for j in b:
        if j in x:
            num+=x[j]
    print(num)