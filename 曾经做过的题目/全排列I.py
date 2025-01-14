#复习itertools 的 permutations 版
from itertools import permutations
n = int(input())
numbers=[]
for i in range(1,n+1):
    numbers.append(i)


for per in permutations(numbers):
    print(' '.join(map(str,per)))

#对对是要学的递归版
def quan(n, path, used, result):
    if len(path) == n:
        result.append(path[:])

    for i in range(1, n+1):
        if used[i]:
            continue

        used[i] = True
        path.append(i)

        quan(n, path, used, result)
        path.pop()
        used[i] = False


def pai(n):
    result = []
    used = [False] * (n + 1)
    quan(n, [], used, result)

    for i in result:
        print(" ".join(map(str, i)))


n = int(input())
pai(n)