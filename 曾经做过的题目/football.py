n=str(input())
num =0
for i in range(1,len(n)):
    if n[i-1] == n[i]:
        num +=1
        if num>=6:
            print("YES")
            break
    else:
        num=0
else:
    print("NO")
    #自己写的加修正版

    #通义千问提供的简单版
n = str(input())
m = "0000000"in n or "1111111" in n
print("YES"if m else"NO")