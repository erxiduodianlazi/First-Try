def ok(t):
    if 360%(180-a)==0 and 360/(180-a)!=2:
        return True
    return False
t = int(input())
for i in range(t):
    a = int(input())
    if ok(t) is True:
        print("YES")
    else:
        print("NO")