#双指针法
while True:
    n = int(input())
    if n == 0:
        break
    t = list(map(int, input().split()))
    w = list(map(int, input().split()))
    t.sort(reverse=True)
    w.sort(reverse=True)
    num = 0
    i = 0
    j = 0
    end1 = n - 1
    end2 = n - 1
    while i <= end1:
        if t[i] > w[j]:
            num += 1
            i += 1
            j += 1
        elif t[end1] > w[end2]:
            num += 1
            end1 -= 1
            end2 -= 1
        else:
            if t[end1]<w[j]:
                num -= 1
            end1 -= 1
            j += 1
    print(num*200)

#dp的方法
while True:
    n = int(input())
    if n == 0:
        break
    a = sorted([int(x) for x in input().split()], reverse=True)
    b = sorted([int(x) for x in input().split()], reverse=True)
    c = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if a[i-1] > b[j-1]:
                c[i][j] = max(c[i-1][j], c[i][j-1], c[i-1][j-1]+2)
            elif a[i-1] == b[j-1]:
                c[i][j] = max(c[i-1][j], c[i][j-1], c[i-1][j-1]+1)
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1], c[i-1][j-1])
    print((c[n][n]-n)*200)



