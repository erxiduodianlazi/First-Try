n = int(input())
m = [x for x in range(1,10**1000000000,2)]
for i in range(n):
    a = int(input())
    for j in m:
        if a % j ==0:
            print("Yes")
            break
        print("No")
#错误的，超时的

#奇数乘奇数等于奇数，偶数一只除二直到最后为奇数，
n = int(input())
for i in range(n):
    a = int(input())
    while a%2 ==0:
        a//=2
    if a ==1:
        print("No")
        continue
    print("Yes")