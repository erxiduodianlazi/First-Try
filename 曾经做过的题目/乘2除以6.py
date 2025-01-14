t = int(input())
for _ in range(t):
    m = int(input())
    num = 0
    while m!=1:
        if m % 6 ==0:
            m = m/6
            num += 1
        elif m % 3 ==0:
            m*=2
            num +=1
        else:
            print("-1")
            break
    else:
        print(num)





