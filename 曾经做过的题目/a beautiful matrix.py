for i in range(1,6):
    a =input().split()
    if "1" in a:
        print((abs(i-3)+abs(a.index("1")-2)))