n = int(input())
p = [0]*21
p[0]=1
p[1]=1
for i in range(2,21):
    p[i]=p[i-1]+p[i-2]

for j in range(n):
    a = int(input())
    if a ==1 :
        print("1")
    else:
        print(p[a]-p[a-2])


#函数法
from functools import lru_cache

@lru_cache(maxsize = 128)
def f(n):
    if n <= 2:
        return 1
    else:
        return f(n-1)+f(n-2)


n = int(input())
list_1 = []
for i in range(n):
    num = int(input())
    list_1.append(f(num))
for i in list_1:
    print(i)