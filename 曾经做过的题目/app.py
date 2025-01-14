i, j = 0, 1
count = 0  

while i < 100:
	count += 1
	print(i)  # 假设这里只用于计数，实际运行时可注释掉以避免大量输出
	i += 1
	j += 1
	i += j
print(j)

print("最后一次打印的i值为:", i - j - 1)  # 因为最后一次增加使i>=100，所以我们需要减去这次增加
print("print语句执行次数:", count)