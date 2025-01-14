#tuple可以版
n = int(input())
b=[]
num=0
for _ in range(n):
    a=input()
    b.append((a,len(a)))
b.sort(key = lambda x : x[1])
for i in range(b[0][1]):
    for j in range(n):
        if b[0][0][i]!=b[j][0][i]:
            break
    else:
        num+=1
if num:
    print(b[0][0][:num])
else:
    print()


n = int(input())
b=[]
num=0
for _ in range(n):
    a=input()
    b.append(a)
b.sort(key = lambda x :len(x))
for i in range(b[0][1]):
    for j in range(1,n):
        if b[j][i]!=b[0][i]:
            break
    else:
        num+=1
        continue# 继续检查下一个字符
    break  # 如果有任何不匹配，退出外循环
if num:
    print(b[0][0][:num])
else:
    print()
#为什么不行版
    n = int(input())
    b = []
    num = 0
    for _ in range(n):
        a = input()
        b.append((a, len(a)))
    b.sort(key=lambda x: x[1])
    for i in range(b[0][1]):
        for j in range(1, n):
            if b[j][0][i] == b[j - 1][0][i]:
                num += 1
            else:
                break

    print(num)

    if num % (n - 1) != 0:
        print()
    else:
        d = num // (n - 1)
        print(b[0][0][0:d])

