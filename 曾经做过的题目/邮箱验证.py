while True:
    try:
        n = input()
        if n.count("@") ==1:
            if n[0] != "@" and n[0]!="."and n[-1]!="@" and n[-1]!=".":
                a=n.index("@")
                b = n.find(".",a)
                if b>a and b!= a+1 and n[a-1] != ".":
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")
        else:
            print("NO")
    except EOFError:
        break
