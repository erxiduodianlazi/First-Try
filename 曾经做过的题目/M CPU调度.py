#答案，写可以并行，先把写的时间长的给用了
n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: (-x[1], x[0]))
ans1 = ans2 = 0
for i in range(n):
    ans1 += l[i][0]
    ans2 = max(ans2, ans1+l[i][1])
print(ans2)


#错误的错误的
n=int(input())
c=[list(tuple(map(int,input().split()))) for i in range(n)]
num=0
min_num=float('inf')
for m,n in c:
    num+=m
    min_num=min(min_num,n)
print(num+min_num)
