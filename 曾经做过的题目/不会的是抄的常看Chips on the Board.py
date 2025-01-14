t = int(input())
for i in range(t):
    n = int(input())
    a =list(map(int,input().split()))
    b =list(map(int,input().split()))
    min_a = min(a)
    min_b = min(b)

    ansa=sum(min_a+i for i in b)
    ansb=sum(min_b+i for i in a)

    print(min(ansa,ansb))

