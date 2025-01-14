import math
rest = [0, 5, 3, 1]  # 这个列表表示在不同数量的 3*3 产品时，可以与 4*4 产品一起放置的 2*2 产品的数量

while True:
    a, b, c, d, e, f = map(int, input().split())  # 读取输入的六个整数，分别表示 1*1, 2*2, 3*3, 4*4, 5*5, 6*6 的数量
    if a + b + c + d + e + f == 0:
        break  # 如果所有数量都是 0，则退出循环

    boxes = d + e + f  # 计算需要的包裹数，首先考虑 4*4, 5*5, 6*6 的产品
    boxes += math.ceil(c / 4)  # 计算 3*3 产品需要的包裹数，每个包裹最多放 4 个 3*3 产品

    spaceforb = 5 * d + rest[c % 4]  # 计算可以和 4*4、3*3 产品一起放置的 2*2 产品的数量
    if b > spaceforb:
        boxes += math.ceil((b - spaceforb) / 9)  # 如果 2*2 产品多于可以一起放置的数量，计算额外需要的包裹数

    spacefora = boxes * 36 - (36 * f + 25 * e + 16 * d + 9 * c + 4 * b)  # 计算剩余的空间，用于放置 1*1 产品
    if a > spacefora:
        boxes += math.ceil((a - spacefora) / 36)  # 如果 1*1 产品多于剩余空间，计算额外需要的包裹数

    print(boxes)  # 输出所需的最小包裹数