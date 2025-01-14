# Assignment #1: 自主学习

Updated 0110 GMT+8 Sep 10, 2024

2024 fall, Complied by ==同学的姓名、院系==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02733: 判断闰年

http://cs101.openjudge.cn/practice/02733/



思路：根据题目所给提示，先在小的方面排除不是闰年的情况，再在大的方面排除不是闰年的情况



##### 代码

```python
# a = int(input())
if (a%3200 == 0) or ((a%100 == 0) and (a%400!= 0)):
    print('N')
elif a%4 == 0:
    print('Y')
else:
    print('N')

```



代码运行截图 ==（至少包含有"Accepted"）==

![联想截图_20240920043317](C:\Users\kivvii\Desktop\联想截图_20240920043317.png)

### 02750: 鸡兔同笼

http://cs101.openjudge.cn/practice/02750/



思路：先假设全是兔子



##### 代码

```python
# a = int(input())
if a%4 == 0:
    m =a//4
    n =a//2
elif a%4 != 0 and a%2 == 0:
    m =a//4+(a%4)//2
    n = a//2
else:
    m =0
    n =0
print(m,n)

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20240920043619824](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20240920043619824.png)



### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：先竖着摆再横着摆



##### 代码

```python
# M,N =map(int, input().split())
if N % 2 == 0:
    print(N//2*M)
else:
    print(N//2*M + M//2)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920044535221](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20240920044535221.png)



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：分别求长，宽至少需要块数，再相乘



##### 代码

```python
# n,m,a = map(int,input().split())
import math
b = math.ceil(n/a)
c = math.ceil(m/a)
print(b*c)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920045755465](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20240920045755465.png)



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：搞清楚字典顺序



##### 代码

```python
# s = input().lower()
m = input().lower()
if s > m:
    print(1)
elif m > s:
    print(-1)
else:
    print(0)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920050632111](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20240920050632111.png)



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：1，0的数量，可借助相加之和判断



##### 代码

```python
# n = int(input())
num = 0
for i in range(n):
    x,y,z=map(int,input().split())
    if x+y+z>=2:
        num+=1
print(num)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20240920051459299](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20240920051459299.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

额外练习：目前完成了0831日之前的大部分选做，也完成了中秋节期间的选做任务。

总结：作为一名0基础的新手小白，从最开始接触各种代码时的完全懵圈，到现在借助ai和答案，慢慢学习了少量基本语法，这个过程还是挺痛苦的。但是看到自己独立完成的题目（虽然非常简单）得到ac还是很开心的。现在感觉是知识懂了一点但不多，遇到题目往往还是难以下手，语法方面还有很多要学习的地方，征途漫漫，继续加油吧。

一些具体收获：map(int(input().split())的用法，引入math向上取整，加减乘除运算，字符串大小比较依靠字典顺序，集合不能出现相同元素，join()等等







