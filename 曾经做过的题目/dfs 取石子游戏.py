while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    else:
        x,y=a,b
        a=max(x,y)
        b=min(x,y)

        num=1

        while a>0 and b>0:
            if a//b>=2 or a==b :
                break
            a-=b
            a,b=b,a
            num += 1
        if num%2==0:
            print('lose')
        else:
            print('win')

#dfs翻转
def pd(a, b):
    """
    判断是否满足先手必赢的条件
    """
    if a // b >= 2 or a == b:  # 如果 a 是 b 的两倍及以上，或者两数相等
        return True
    else:
        return not pd(b, a - b)  # 否则继续判断下一轮

def main():
    while True:
        # 输入两堆石子的数量
        a, b = map(int, input().split())
        if a == 0 or b == 0:  # 结束条件
            break
        if b > a:  # 确保 a >= b
            a, b = b, a
        # 输出结果
        if pd(a, b):
            print("win")
        else:
            print("lose")

if __name__ == "__main__":
    main()

