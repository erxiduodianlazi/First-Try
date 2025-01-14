# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>万馨雅 城环</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：



代码：

```python
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    else:
        x,y=a,b
        a=max(x,y)
        b=min(x,y)

        num=1

        while a>0 and b>0:
            if a//b>=2 or a==b :
                break
            a-=b
            a,b=b,a
            num += 1
        if num%2==0:
            print('lose')
        else:
            print('win')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241211153423096](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241211153423096.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：



代码：

```python
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
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241211193630592](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241211193630592.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：



代码：

```python
import heapq

def yao(n,c):
    consumed=[]
    health=0
    for i in range(n):
        health+=c[i]
        heapq.heappush(consumed,c[i])
        if health<0:
            if consumed:
                health-=consumed[0]
                heapq.heappop(consumed)
    return len(consumed)


n=int(input())
c=list(map(int,input().split()))
print(yao(n,c))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241211202242956](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241211202242956.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：



代码：

```python
a=[]
m=[]
while True:
    try:
        s=input().split()
        if s[0]=='pop':
            if a:
                a.pop()
                if m:
                    m.pop()
        elif s[0]=='min':
            if m:
                print(m[-1])
        else:
            num=int(s[1])
            a.append(num)
            if not m:
                m.append(num)
            else:
                m.append(min(num,m[-1]))
    except EOFError:
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241212133318464](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241212133318464.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：



代码：

```python
import heapq
m,n,p = map(int,input().split())
c=[list(map(str,input().split())) for _ in range(m)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def tili(x,y,a,b):
    pos=[]
    dist = [[float('inf')] * n for _ in range(m)]
    heapq.heappush(pos, (0, x, y))
    dist[x][y]=0
    while pos:
        strength,x,y=heapq.heappop(pos)
        if x==a and y==b :
            return strength
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and c[nx][ny]!='#':
                if dist[nx][ny]>strength+abs(int(c[nx][ny])-int(c[x][y])):
                    dist[nx][ny]=strength+abs(int(c[nx][ny])-int(c[x][y]))
                    heapq.heappush(pos,(dist[nx][ny],nx,ny))
    return 'NO'
for _ in range(p):
    x,y,a,b=map(int,input().split())
    if c[x][y]=='#' or c[a][b]=='#':
        print('NO')
        continue
    result=tili(x,y,a,b)
    print(result)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241212175039008](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241212175039008.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：



代码：

```python
from collections import deque
def bfs(x,y):
    visited=set()
    visited.add((0,x,y))
    q=deque([(0,x,y)])
    while q:
        time,x,y=q.popleft()
        if m[x][y]=="E":
            return time
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c  and ((time+1)%k,nx,ny) not in visited:
                if m[nx][ny]!='#' or (time+1)%k==0:
                    q.append((time+1,nx,ny))
                    visited.add(((time+1)%k,nx,ny))
    return "Oop!"


directions=[(1,0),(-1,0),(0,1),(0,-1)]
t=int(input())
for _ in range(t):
    r,c,k=map(int,input().split())
    m=[list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if m[i][j]=='S':
                print(bfs(i,j))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241213175030284](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241213175030284.png)



## 2. 学习总结和收获

比上周好写，好理解一点点了！但还是不太懂。做了去年的机考题的E和M题，发现还是可以做出来的，继续加油





