def count_ways_to_split(arr):
    n = len(arr)
    total_sum = sum(arr)

    # 如果总和不能被3整除，返回0
    if total_sum % 3 != 0:
        return 0

    part_sum = total_sum // 3
    prefix_sum = 0
    count_part1 = 0
    ways = 0

    for i in range(n - 1):
        prefix_sum += arr[i]

        if prefix_sum == 2 * part_sum and i < n - 1:
            ways += count_part1

        if prefix_sum == part_sum:
            count_part1 += 1

    return ways


# 读取输入
n = int(input())
arr = list(map(int, input().split()))

# 计算并输出结果
print(count_ways_to_split(arr))
