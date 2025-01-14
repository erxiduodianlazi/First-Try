# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>万馨雅 城环</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：



代码：

```python
n=int(input())
if n<2:
    print(1)
else:
    dp=[-1]*(n+1)
    dp[0]=0
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241128144541786](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241128144541786.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：



代码：

```python
n=int(input())
dp=[0]+[1]*n
for i in range(2,n+1):
    for j in range(1,i):
        dp[i]+=dp[i-j]
print(dp[n])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241128153619778](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241128153619778.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：



代码：

```python
t,k=map(int,input().split())
dp=[1]+[0]*100000
s=[0]*100001
chu=1000000007
for i in range(1, 100001):
    if i >= k:
        dp[i] = (dp[i - 1] + dp[i - k]) % chu
    else:
        dp[i] = dp[i - 1] % chu
    s[i] = s[i - 1] + dp[i]
for _ in range(t):
    a,b=map(int,input().split())
    print((s[b]-s[a-1])%chu)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241129095532398](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241129095532398.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路



代码：

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        if n<2:
            return(s)
        else:
            start = 0;max_len=1
            def kuosan(x,y):
                while x>=0 and y<n and s[x]==s[y]:
                    x-=1
                    y+=1
                return x+1,y-1
            for i in range(n):
                x1,y1=kuosan(i,i)
                x2,y2=kuosan(i,i+1)
                if y1-x1+1>max_len:
                    start,max_len=x1,y1-x1+1
                if y2-x2+1>max_len:
                    start,max_len=x2,y2-x2+1
            return s[start:start+max_len]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241130221610253](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241130221610253.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：



代码：

```python
from collections import deque
import sys
input=sys.stdin.read
def bfs(x,y,start_height,m,n,h,water_height):
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    q=deque([(x,y,start_height)])
    water_height[x][y]=start_height
    while q:
        x,y,height=q.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and h[nx][ny]<height:
                if water_height[nx][ny]<height:
                    water_height[nx][ny]=height
                    q.append((nx,ny,height))


def main():
    data = input().split() 
    idx=0
    k = int(data[idx])
    idx += 1
    results = []

    for _ in range(k):
        m,n = map(int, data[idx:idx + 2])
        idx += 2
        h = []
        for i in range(m):
            h.append(list(map(int, data[idx:idx + n])))
            idx += n
        water_height = [[0] * n for _ in range(m)]

        i, j = map(int, data[idx:idx + 2])
        idx += 2
        i, j = i - 1, j - 1

        p = int(data[idx])
        idx += 1

        for _ in range(p):
            x, y = map(int, data[idx:idx + 2])
            idx += 2
            x, y = x - 1, y - 1
            if h[x][y] <= h[i][j]:
                continue
            bfs(x, y, h[x][y], m, n, h, water_height)

        results.append("Yes" if water_height[i][j] > 0 else "No")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241201155541536](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241201155541536.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：自己写的改了很久很久都没有对……



代码：

```python
directions=[(1,-1,0),(2,1,0),(3,0,-1),(4,0,1)]
from collections import deque
def bfs(x1,y1,x2,y2,c):
    q=deque()
    q.append((y1,x1,0,-1))
    iq[y1][x1]=True
    ans=[]
    while q:
        y,x,seg,pre_direction,=q.popleft()
        if y == y2 and x == x2:
            ans.append(seg)
            break
        for direction,dy,dx in directions:
            ny = y+dy; nx = x+dx
            if 0<=ny<h+2 and  0<=nx<w+2  and not iq[ny][nx]:
                new_direction=direction
                new_seg = seg if new_direction==pre_direction else seg+1
                if ny==y2 and nx==x2:
                    ans.append(new_seg)
                    continue
                if c[ny][nx]!='X':
                    iq[ny][nx]=True
                    q.append((ny,nx,new_seg,new_direction))
    if len(ans)==0:
        return -1
    else:
        return min(ans)

num1=0
while True:
    w,h = map(int,input().split())
    if w==h==0:
        break

    num1+=1
    print(f'Board #{num1}:')
    c = [' '*(w+2)]+[' '+input()+' 'for i in range(h)]+[' '*(w+2)]
    iq=[[False] * (w+2) for i in range(h+2) ]
    num2=0
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        num2+=1
        result=bfs(x1,y1,x2,y2,c)
        if result !=-1:
            print(f'Pair {num2}: {result} segments.')
        else:
            print(f'Pair {num2}: impossible.')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241203144932094](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241203144932094.png)



## 2. 学习总结和收获

前面两题还好，后面写得想紫砂，好崩溃，求放过。最后两题自己写的改了很久很久，照着答案改，感觉思路都差不多，但就是WA和RE，没办法先照着答案交上来吧，等下再看看，，，，



