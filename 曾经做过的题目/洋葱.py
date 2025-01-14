n=int(input())
c=[list(map(int,input().split())) for i in range(n)]
d=[]
left=0;right=n-1
top=0;bottom=n-1
while left<right:
    num=0
    for i in range(left,right+1):
        num+=c[top][i]
    top+=1
    for j in range(top,bottom+1):
        num+=c[j][right]
    right-=1
    for l in range(right,left-1,-1):
        num+=c[bottom][l]
    bottom-=1
    for k in range(bottom,top-1,-1):
        num+=c[k][left]
    left+=1
    d.append(num)
if n%2==0:
    print(max(d))
else:
    d.append(c[n//2][n//2])
    print(max(d))
#答案版
from math import ceil
n = int(input())
matrix = [0 for _ in range(n)]
for i in range(n):
    matrix[i] = [int(_) for _ in input().split()]
ans = [0] * ceil(n/2)
for i in range(n):
    for j in range(n):
        ans[min(i, j, n-1-i, n-1-j)] += matrix[i][j]
print(max(ans))