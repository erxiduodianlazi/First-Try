a = int(input())
if a%4 == 0:
    m =a//4
    n =a//2
elif a%4 != 0 and a%2 == 0:
    m =a//4+(a%4)//2
    n = a//2
else:
    m =0
    n =0
print(m,n)