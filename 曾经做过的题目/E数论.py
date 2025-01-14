def pfactors(n):
    from math import sqrt
    pfact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pfact.append(check)
            num /= check
    if num > 1:
        pfact.append(num)
    return pfact
n=int(input())
c=pfactors(n)
ok= False
if len(c)>1:
    for i in range(1,len(c)):
        if c[i]==c[i-1]:
            print(0)
            ok=True
            break#这个break少了就过不了啊啊啊
if not ok:
    if len(c)%2==0:
        print(1)
    else:
        print(-1)

#而且有更简单的办法，因为集合不允许出现相同元素，所以
def pfactors(n):
    from math import sqrt
    pfact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pfact.append(check)
            num /= check
    if num > 1:
        pfact.append(num)
    return pfact
n=int(input())
c=pfactors(n)
d=set(c)
if len(c)>len(d):
    print(0)
else:
    if len(c)%2==0:
        print(1)
    else:
        print(-1)
