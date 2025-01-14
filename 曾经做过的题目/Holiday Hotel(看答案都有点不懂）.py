while True:
    N = int(input())
    v = []
    num = 1
    if N ==0:
        break
    for _ in range(N):
        D,C = map(int,input().split())
        v.append((D,C))
    v.sort(key = lambda x :(x[0],x[1]))

    max_cost = v[0][1]

    for i in range(N):
        if v[i][1] < max_cost:
            max_cost = v[i][1]
            num+=1


    print(num)

    # 错误版，排序问题，也不能一边遍历一边删除,madeoj题永远都不会写
    while True:
        N = int(input())
        v = []
        num = 0
        if N == 0:
            break
        for _ in range(N):
            a, b = map(int, input().split())
            v.append((a, b))
        v.sort()
        for i in range(N):
            for j in range(i + 1, N):
                if v[i][1] > v[j][1]:
                    num += 1
        print(num)


