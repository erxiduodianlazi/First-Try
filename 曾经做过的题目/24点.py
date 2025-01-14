from itertools import permutations

def success(numbers):
    for per in permutations(numbers):
        a,b,c,d=per
        if a+b+c+d ==24or a+b+c-d ==24 or a+b-c-d==24 or a+b-c-d ==24:
            return True
    return False

m = int(input())
for i in range(m):
    numbers = list(map(int,input().split()))
    if success(numbers):
       print('YES')
    else:
        print("NO")

m = int(input())
for i in range(m):
    a,b,c,d=list(map(int,input().split()))
    found = False
    for j in[a,-a]:
        for k in [b,-b]:
            for e in [c,-c]:
                for f in [d,-d]:
                    if j+k+f+e==24:
                        found=True
    print("YES" if found else"NO")