#超时版
import math
num=0
while True:
    n,d=map(int,input().split())
    c=[]
    if n+d == 0:
        break
    num+=1
    possible = True
    for _ in range(n):
        c.append(tuple(map(int,input().split())))
        if c[_][1] > d:
            possible = False
    input()
    if not possible:
        print(f'Case {num}: -1')
        continue
    c.sort(key = lambda x:(x[0],x[1]))
    i=0
    cnt=0
    while i < n:
        cnt+=1
        point = c[i][0]+math.sqrt(d*d-c[i][1]*c[i][1])


        while i<n and math.pow(c[i][0]-point,2) +math.pow(c[i][1],2) <= math.pow(d,2):
            i+=1
        continue
    print(f'Case {num}: {cnt}')

#为什么不超时，因为提前预处理了雷达的范围
import math

num = 0
while True:
    # 读取 n 和 d
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break  # 输入为 0 0 时结束
    num += 1  # 记录 case 号

    # 输入岛屿坐标
    islands = []
    possible = True
    for _ in range(n):
        x, y = map(int, input().split())
        if y > d:  # 如果 y 坐标大于 d，无法覆盖
            possible = False
        else:
            # 计算每个岛屿的覆盖范围
            distance = math.sqrt(d * d - y * y)
            l = x - distance
            r = x + distance
            islands.append((l, r))
    input()
    if not possible:
        print(f'Case {num}: -1')
        continue

    # 按右边界排序
    islands.sort(key=lambda x: x[1])

    cnt = 0
    i = 0
    while i < n:
        cnt += 1
        current_radar = islands[i][1]
        while i < len(islands) and islands[i][0] <= current_radar:
            i += 1

    print(f'Case {num}: {cnt}')
