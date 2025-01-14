#答案简洁版，出现次数最多的小盒子必然没有地方放
from collections import *
n = int(input())
print(max(Counter(input().split()).values()))

