while True:
    m = input()
    if m == "0.00":
        break
    else:
        m = float(m)
        s = 0.00
        n = 1
        while s<m:
            n+=1
            s+=1/n
        else:
            print(f"{n-1} card(s)")