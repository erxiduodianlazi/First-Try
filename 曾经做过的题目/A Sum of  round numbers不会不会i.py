n = int(input())  # 读取n，表示有n个测试案例
for _ in range(n):
    s = input()  # 读取每个测试案例中的数字字符串
    cnt = 0  # 用于记录分解出来的 round numbers 的个数
    res = []  # 存储分解出来的 round numbers
    i = 0  # 用来记录当前处理的是第几位数字
    for c in s:  # 遍历数字字符串中的每一位
        i += 1  # 记录当前是第几位（1-indexed）
        if c != '0':  # 如果这一位不是0
            cnt += 1  # 说明这是一个非零的有效位，计数加一
            # 将这一位对应的 round number 计算出来
            res.append(int(c) * (10 ** (len(s) - i)))
    print(cnt)  # 输出 round numbers 的个数
    print(*res)  # 输出具体的 round numbers，用空格分隔
