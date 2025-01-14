def is_leap_year(year):
    """判断是否是闰年"""
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False


def add_days_to_date(y, m, d, n):
    """给定一个日期 y-m-d 和天数 n，返回增加 n 天后的日期"""
    # 将字符串转换为整数
    year = int(y)
    month = int(m)
    day = int(d)
    days_to_add = int(n)

    # 每个月的天数
    month_days = [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 增加天数
    while days_to_add > 0:
        # 当前月的天数
        max_days_in_month = month_days[month - 1]

        if day + days_to_add <= max_days_in_month:
            day += days_to_add
            days_to_add = 0
        else:
            days_to_add -= (max_days_in_month - day + 1)
            day = 1
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1

    # 格式化输出
    return f"{year:04d}-{month:02d}-{day:02d}"


# 读取输入
y, m, d = map(str, input().split("-"))
n = int(input())

# 计算并输出结果
result = add_days_to_date(y, m, d, n)
print(result)