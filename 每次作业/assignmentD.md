# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>万馨雅 城环</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：



代码：

```python
n=int(input())
for _ in range(n):
    dic='ABCDEFGHIJKL'
    g=set()
    light=set()
    heavy=set()
    for _ in range(0,3):
        m,n,zhuangtai=input().split()
        if zhuangtai=='even':
            g.update(m)
            g.update(n)
        elif zhuangtai=='up':
            heavy.update(m)
            light.update(n)
        else:
            light.update(m)
            heavy.update(n)
    for i in dic:
        if i in g:
            continue
        if i in heavy and i not in light:
            print(f'{i} is the counterfeit coin and it is heavy.')
            break
        elif i in light and i not in heavy:
            print(f'{i} is the counterfeit coin and it is light.')
            break

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241218131957352](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241218131957352.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：



代码：

```python
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
dp=[[-1]*c for _ in range(r)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    max_length=1
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and m[nx][ny]<m[x][y]:
            max_length=max(dfs(nx,ny)+1,max_length)
    dp[x][y]=max_length
    return max_length
result=0
for i in range(r):
    for j in range(c):
        result=max(result,dfs(i,j))
print(result)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241219145507136](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241219145507136.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：



代码：

```python
from collections import deque
def bfs(i,j,k,l,c):
    q=deque()
    q.append((i,j,k,l))
    visited.append((i,j,k,l))
    while q:
        i,j,k,l=q.popleft()
        if c[i][j]==9 or c[k][l]==9:
            return True
        for dx,dy in directions:
            ni=i+dx;nj=j+dy
            nk=k+dx;nl=l+dy
            if 0<=ni<n and 0<=nj<n and 0<=nk<n and 0<=nl<n and c[ni][nj] !=1 and c[nk][nl] !=1 and (ni,nj,nk,nl) not in visited:
                q.append((ni,nj,nk,nl))
                visited.append((ni,nj,nk,nl))
    return False


directions=[(1,0),(-1,0),(0,1),(0,-1)]
visited=[]
now=[]
n=int(input())
c=[list(map(int,input().split())) for _ in range(n)]
for a in range(n):
    for b in range(n):
        if c[a][b]==5:
            now.append(a)
            now.append(b)
i,j,k,l=now
if bfs(i,j,k,l,c):
    print('yes')
else:
    print('no')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241220160351192](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241220160351192.png)

### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：



代码：

```python
m=int(input())
n=int(input())
c=list(map(str,input().split()))
for i in range(len(c)-1):
    for j in range(i+1, len(c)):
        #print(i,j)
        if int(c[i] + c[j]) < int(c[j] + c[i]):
            c[i], c[j] = c[j], c[i]
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if j<len(c[i-1]):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],int(str(dp[i-1][j-len(c[i-1])])+c[i-1]))
print(dp[-1][-1])

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241220182513397](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241220182513397.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：



代码：

```python
X = [[0,0,0,0,0,0,0,0]]
Y = [[0,0,0,0,0,0,0,0]]
for _ in range(5):
    X.append([0] + [int(x) for x in input().split()] + [0])
    Y.append([0 for x in range(8)])    
X.append([0,0,0,0,0,0,0,0])
Y.append([0,0,0,0,0,0,0,0])

import copy
for a in range(2):
    Y[1][1] = a
    for b in range(2):
        Y[1][2] = b
        for c in range(2):
            Y[1][3] = c
            for d in range(2):
                Y[1][4] = d
                for e in range(2):
                    Y[1][5] = e
                    for f in range(2):
                        Y[1][6] = f
                        
                        A = copy.deepcopy(X)
                        B = copy.deepcopy(Y)
                        for i in range(1, 7):
                            if B[1][i] == 1:
                                A[1][i] = abs(A[1][i] - 1)
                                A[1][i-1] = abs(A[1][i-1] - 1)
                                A[1][i+1] = abs(A[1][i+1] - 1)
                                A[2][i] = abs(A[2][i] - 1)
                        for i in range(2, 6):
                            for j in range(1, 7):
                                if A[i-1][j] == 1:
                                    B[i][j] = 1
                                    A[i][j] = abs(A[i][j] - 1)
                                    A[i-1][j] = abs(A[i-1][j] - 1)
                                    A[i+1][j] = abs(A[i+1][j] - 1)
                                    A[i][j-1] = abs(A[i][j-1] - 1)
                                    A[i][j+1] = abs(A[i][j+1] - 1)
                        if A[5][1]==0 and A[5][2]==0 and A[5][3]==0 and A[5][4]==0 and A[5][5]==0 and A[5][6]==0:
                            for i in range(1, 6):
                                print(" ".join(repr(y) for y in [B[i][1],B[i][2],B[i][3],B[i][4],B[i][5],B[i][6] ]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224135522164](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241224135522164.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：



代码：

```python
L, n, m = map(int, input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)
def check(x):
    num = 0
    now = 0
    for i in range(1, n + 2):
        if rock[i] - now < x:
            num += 1
        else:
            now = rock[i]

    if num > m:
        return True
    else:
        return False
lo, hi = 0, L + 1
ans = -1
while lo < hi:
    mid = (lo + hi) // 2

    if check(mid):
        hi = mid
    else:
        ans = mid
        lo = mid + 1

print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241224135353161](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241224135353161.png)



## 2. 学习总结和收获

后面难的题目直接放弃了，希望机考能多做对一点简单和中等的题目（祈祷）。



