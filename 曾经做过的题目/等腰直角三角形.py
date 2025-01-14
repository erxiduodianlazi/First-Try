n = int(input())
for i in range(1,n+1):
    if i<=2 or i ==n:
        print('*'*i)
    else:
        print("*",end="")
        print(" "*(i-2),end="")
        print("*")
