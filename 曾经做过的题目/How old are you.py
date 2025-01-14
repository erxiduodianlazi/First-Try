x = int(input())
while x != 1:
    if x%2 != 0:
        print(f"{x}*3+1={x*3+1}")
        x = x*3+1
    else:
        print(f"{x}/2={x//2}")
        x = x//2
#答案有占位符的用法 ”{}/2={}"。format(x,y)