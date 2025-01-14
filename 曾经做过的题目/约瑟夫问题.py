#pop = append 可以形成循环法，具体可见答案，现为根据印象写的
while True:
    n,m =map(int,input().split())
    if n+m == 0:
        break
    monkey = [i for i in range(1,n+1)]
    index = 0
    while len(monkey) !=0:
        temp = monkey.pop(0)
        index+=1
        if index ==m:
            index=0
            continue
        monkey.append(temp)
    print(monkey[0])

#递归方法
def func(n,m):
    if n == 1:
        return 1
    return(func(n-1,m) +m-1)%n +1


while True:
    n,m = map(int,input().split())
    if n+m ==0:
        break
    print(func(n,m))

#在遍历中用remove删除副本中的元素！
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    li = list(range(1, n + 1))
    if m == 1:
        print(li[-1])
    else:
        i = 0
        while len(li) > 1:
            for monkey in li.copy():
                i += 1
                if i == m:
                    li.remove(monkey)
                    i = 0
        print(li[0])
