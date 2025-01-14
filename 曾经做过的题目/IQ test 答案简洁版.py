useless = input()  # 读取并忽略输入的第一个值
a = [int(x)%2 for x in input().split()]  # 将输入的数字转换为奇偶性（偶数为0，奇数为1）
print(a.index(sum(a)==1)+1)  # 根据数组的奇偶性，若==1则为奇数，返回1，若》1则false，返回0，输出与其他不同的数字的索引


n = int(input())
a = list(map(int, input().split()))
a = [i % 2 for i in a]
sum_val = sum(a)
if sum_val == 1:
    print(a.index(1) + 1)
else:
    print(a.index(0) + 1)