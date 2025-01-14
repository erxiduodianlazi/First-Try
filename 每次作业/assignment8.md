# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：看到最外层全是水就意识到要加保护圈了，周长则是数每个1旁边有多少0再相加，终于有一个顺利做出来的题目了我哭死



代码：

```python
dic={0:4,1:3,2:2,3:1,4:0}
def zhou(n,m,d):
    c=[[0]*(m+2) for _ in range(n+2)]
    num=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            c[i][j]=d[i-1][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if c[i][j]==1:
                num+=dic[c[i-1][j]+c[i][j-1]+c[i][j+1]+c[i+1][j]]
    return num


n,m = map(int,input().split())
d=[]
for _ in range(n):
    d.append(list(map(int,input().split())))
print(zhou(n,m,d))dic={0:4,1:3,2:2,3:1,4:0}

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241112145852540](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241112145852540.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：



代码：

```python
def matrix(n):
    c=[[0]*n for _ in range(n)]
    num=1
    top=0;bottom=n-1;left=0;right=n-1
    while num<=n*n:
        for i in range(left,right+1):
            c[top][i]=num
            num+=1
        top+=1
        for j in range(top,bottom+1):
            c[j][right]=num
            num+=1
        right-=1
        for l in range(right,left-1,-1):
            c[bottom][l]=num
            num+=1
        bottom-=1
        for k in range(bottom,top-1,-1):
            c[k][left]=num
            num+=1
        left+=1
    return c

def xing(c):
    for i in c:
        print(" ".join(map(str,i)))


n= int(input())
p_matrix = matrix(n)
xing(p_matrix)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241114164435328](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241114164435328.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：



代码：

```python
d = int(input())
n = int(input())
c=[[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,k=map(int,input().split())
    for i in range(max(0,x-d),min(x+d+1,1025)):
        for j in range(max(0,y-d),min(y+d+1,1025)):
            c[i][j]+=k
max_number=0  
shu=0
for i in range(1025):
    for j in range(1025):
        if c[i][j]>max_number:
            shu=1
            max_number=c[i][j]
        elif c[i][j]==max_number:
            shu+=1
print(shu,max_number)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241112164733830](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241112164733830.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：



代码：

```python
n=int(input())
m=list(map(int,input().split()))
if n==1:
    print(1)
elif n==2:
    if m[0]!=m[1]:
        print(2)
    else:
        print(1)
else:
    up=1
    down=1
    for i in range(1,n):
        if m[i]>m[i-1]:
            up=down+1
        elif m[i]<m[i-1]:
            down=up+1
    print(max(up,down))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114164254161](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241114164254161.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：



代码：

```python
n = int(input())
c=[0]*100001
for m in map(int,input().split()):
    c[m]+=1
dp=[0]*100001
dp[1]=c[1]
for i in range(2,100001):
    dp[i]=max(dp[i-1],dp[i-2]+c[i]*i)

print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241115142025683](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241115142025683.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241117221627555](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241117221627555.png)



## 2. 学习总结和收获

好难，除了第一题其他都不是自己独立写出来的
