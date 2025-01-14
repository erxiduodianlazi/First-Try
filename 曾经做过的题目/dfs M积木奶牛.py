n=int(input())
c=[]
for _ in range(4):
    c.append(input())

def dfs(goal,y):
    if y==len(goal):
        return True
    for i in range(4):
        if goal[y] in c[i] and visited[i]==False:
            visited[i]=True
            if dfs(goal,y+1):
                return True
            visited[i]=False
    return False

for j in range(n):
    goal=input()
    visited=[False]*4
    if dfs(goal,0):
        print("YES")
    else:
        print('NO')


from collections import defaultdict
from itertools import permutations

a = defaultdict(int)
b = defaultdict(int)
c = defaultdict(int)
d = defaultdict(int)
n = int(input())

for i in input():
    a[i] += 1
for i in input():
    b[i] += 1
for i in input():
    c[i] += 1
for i in input():
    d[i] += 1

dicts = [a, b, c, d]

def check(word):
    for perm in permutations(dicts, len(word)):
        for i, d in enumerate(perm):
            if word[i] not in d:
                break
        else:
            return 'YES'
    else:
        return 'NO'

for _ in range(n):
    word = input()
    print(check(word))
