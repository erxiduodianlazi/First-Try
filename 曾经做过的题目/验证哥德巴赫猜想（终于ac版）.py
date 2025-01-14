def is_prime(n):
    if n <=1:
        return False
    if n ==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i =5
    w =2
    while i*i <=n:
        if n %i == 0:
            return False
        i += w
        w = 6-w
    return True

x = int(input())
if x< 6 or x %2 !=0:
    print("Error!")
else:
    for i in range(2,x//2+1):
        b = x-i
        if is_prime(i) and is_prime(b):
            print(f'{x}={i}+{b}')
