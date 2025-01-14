# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>万馨雅 城环</mark>



**说明：**

1）⽉考： AC6<mark>（2）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：



代码：

```python
n = int(input())
c=[]
d=[]
for i in range(n):
    m,n=map(str,input().split())
    if int(n)>= 60:
        d.append((m,n))
    else:
        c.append((m,n))
d.sort(key=lambda x: -int(x[1]))
for i in d:
    print(i[0])
for j in c:
    print(j[0])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107175032552](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241107175032552.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：



代码：

```python
n,m1,m2=map(int,input().split())
x=[[0]*n for i in range(n)]
y=[[0]*n for j in range(n)]
z=[[0]*n for k in range(n)]
for i in range(m1):
    a,b,c = map(int,input().split())
    x[a][b]=c
for j in range(m2):
    d,e,f = map(int,input().split())
    y[d][e]=f
for i in range(n):
    for j in range(n):
        for l in range(n):
            z[i][j]+=x[i][l]*y[l][j]
        if z[i][j] != 0:
            print(i,j,z[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241107175419341](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241107175419341.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：



代码：

```python
N=int(input())
for _ in range(N):
    n,m,b=map(int,input().split())
    d={}
    tl=[]
    for i in range(n):
        ti,xi=map(int,input().split())
        if ti not in tl:
            tl.append(ti)
            d[ti]=[xi]
        else:
            d[ti].append(xi)
    tl.sort()
    for j in tl:
        k=sum(sorted(d[j],key = lambda x:-x)[:m])
        b-=k
        if b<=0:
            print(j)
            break
    else:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108181106054](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241108181106054.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：



代码：

```python
n,m= map(int,input().split())
zhi = list(map(int,input().split()))
dp=[float('inf')]*(m+1)
dp[0]=0
for i in range(1,m+1):
    for j in zhi:
        if j<=i:
             dp[i]=min(dp[i-j]+1,dp[i])
if dp[m] != float('inf'):
    print(dp[m])
else:
    print(-1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107194601528](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241107194601528.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：



代码：

```python
dic = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
           'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
           'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
           'fifty': 50, 'sixty': 60, 'seventy':70, 'eighty':80, 'ninety':90, 'hundred':100, 'thousand':1000, 'million':1000000}


c=list(map(str,input().split()))
num=0
r_num=0
for i in range(len(c)):
    if c[i] in dic:
        if c[i]=='million':
            num+=r_num*1000000
            r_num=0
        elif c[i]=='thousand':
            num+=r_num*1000
            r_num=0
        elif c[i]== 'hundred':
            r_num*=100
        else:
            r_num+=dic[c[i]]
    else:
        continue
num+=r_num
if c[0] == 'negative':
    print(num*(-1))
else:
    print(num)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108143916816](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241108143916816.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：找不相交区间



代码：

```python
n = int(input())
c=[]
num=1
for _ in range(n):
    c.append(tuple(map(int,input().split())))
c.sort(key = lambda x:x[1])
end_line=c[0][1]
for i in range(1,n):
    if c[i][0] > end_line:
        num+=1
        end_line=c[i][1]
print(num)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241107172658833](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241107172658833.png)

## 2. 学习总结和收获

早上考了高数，中午一点到三点又有课，太累了所以没去机房月考。先休息了一下才写的。AC了两个Easy哈哈完蛋咯。在结束过后写出来了最后一题。还是有很多很多不会的，dp看着很眼熟但是自己独立写还是不会写，字典的应用还没有完全搞懂。这个星期在看数学都没有做编程题，考完了要速速补上，继续加油,挂科什么的补药啊！！！



