L, n, m = map(int, input().split())  # L: 河流长度, n: 石头数量, m: 最多允许移除的石头数量
rock = [0]  # 起点位置
for i in range(n):
    rock.append(int(input()))  # 逐个输入石头的位置
rock.append(L)  # 终点位置
def check(x):
    num = 0  # 统计需要移除的石头数量
    now = 0  # 当前所在石头的位置
    for i in range(1, n + 2):  # 遍历每块石头
        if rock[i] - now < x:  # 如果两石头间的距离小于 x，则移除当前石头
            num += 1
        else:  # 如果距离大于等于 x，更新当前所在的位置
            now = rock[i]
    return num > m  # 如果移除的石头数量超过 m，则返回 True（此 x 不可行）
lo, hi = 0, L + 1  # 初始二分查找的范围
ans = -1  # 用于记录最终结果
while lo < hi:
    mid = (lo + hi) // 2  # 取中间值作为当前猜测的最小距离

    if check(mid):  # 如果当前距离不可行（需要移除的石头超过限制）
        hi = mid  # 缩小范围到左半部分
    else:  # 如果当前距离可行
        ans = mid  # 更新答案为当前的 mid
        lo = mid + 1  # 缩小范围到右半部分
