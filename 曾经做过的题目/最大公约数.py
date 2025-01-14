def g(a,b):
    n =1
    for i in range(1,min(a,b)+1):
        if a%i ==0 and b%i ==0:
            n=i
    return n

while True:
    try:
        a,b=map(int,input().split())
    except:
        break
    print(g(a,b))