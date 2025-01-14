t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    a = list(map(int,input().split()))
    min_time =[]
    max_time =[]
    for i in a:
        if i<m/2:
            min_time.append(i)
        else:
            min_time.append(m-i)
    print(max(min_time),end = " ")
    a.sort()

    print(max(m-a[0],a[-1]))