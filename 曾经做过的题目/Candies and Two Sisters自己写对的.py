t = int(input())
for i in range(t):
    a = int(input())
    if a <= 2:
        print(0)
    elif a>2 and a%2 ==0:
        print(a//2-1)
    else:
        print(a//2)