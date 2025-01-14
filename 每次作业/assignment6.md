# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>城环 万馨雅



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：



代码：

```python
def fan_tian(n,fp,wp,tp):
    if n==0:
        return None
    fan_tian(n-1,fp,tp,wp)
    print(f'{fp}->{tp}')
    fan_tian(n-1,wp,fp,tp)


n=int(input())
print(2**n-1)
fan_tian(n,'A','B','C')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241031174350196](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241031174350196.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：怎么样也看不懂递归是怎么写的，，先复习了一下用permutations怎么写



代码：

```python
from itertools import permutations
n = int(input())
numbers=[]
for i in range(1,n+1):
    numbers.append(i)


for per in permutations(numbers):
    print(' '.join(map(str,per)))
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241102114824713](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241102114824713.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：



代码：

```python
k = int(input())
m=list(map(int,input().split()))
dp =[1]*k
for i in range(1,k):
    for j in range(i):
        if m[i]<=m[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241101110330570](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241101110330570.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：



代码：

```python
N,B = map(int,input().split())
prices=list(map(int,input().split()))
weights=list(map(int,input().split()))
dp = [0] * (B+1)
for i in range(N):
    for j in range(B,weights[i]-1,-1):
        dp[j]=max(dp[j],dp[j-weights[i]]+prices[i])
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102114439110](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241102114439110.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：



代码：

```python
def safe(row,col,path):
    for i in range(row):
        if path[i] == col or abs(path[i]-col)==abs(i-row):
            return False
    return True


def queen(row,path,used,result):
    if len(path)==8:
        result.append(path[:])
        return

    for col in range(1,9):
        if used[col]:
            continue
        if safe(row,col,path):
            path.append(col)
            used[col]= True
            queen(row+1,path,used,result)

            path.pop()
            used[col]=False


def eight(n):
    used=[False]* 9
    result=[]
    path=[]
    queen(0,path,used,result)
    print(''.join(map(str,result[n-1])))


T=int(input())
for _ in range(T):
    n = int(input())
    eight(n)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241102211208210](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241102211208210.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：



代码：

```python
n,a,b,c = map(int,input().split())
dp=[0]+[float('-inf')]*n
for i in range(1,n+1):
    for j in (a,b,c):
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)

print(dp[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241103161948000](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241103161948000.png)



## 2. 学习总结和收获

根本不会。好难好难好难好难，，，，递归好难，没有老师推荐的网站我根本不能靠自己贫瘠的大脑模拟这个过程，汉诺塔多看了几次python tutor 终于能看懂一点点了（真的只有一点点），，好崩溃，其实那个回溯我还是没怎么看懂。这次的题目全都是看了答案写的，感觉有些题目比较相似，但是我就是照葫芦画瓢都写不出来。。。好想死呵呵。。dp也好难，cut ribbon看了那个最简单的答案，稍微看懂了就自己打了一次。这一周每日选做都没怎么推进，做作业也特别吃力。哈哈好崩溃，等期中过后再努力补补。

