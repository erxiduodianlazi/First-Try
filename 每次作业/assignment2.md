# Assignment #2: 语法练习

Updated 0126 GMT+8 Sep 24, 2024

2024 fall, Complied by ==万馨雅 城市与环境学院==



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 263A. Beautiful Matrix

https://codeforces.com/problemset/problem/263/A



思路：



##### 代码

```python
# for i in range(1,6):
    m = input().split()
    if "1" in m:
        print(abs(i-3)+abs(m.index("1")-2))
    

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241002155303396](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241002155303396.png)



### 1328A. Divisibility Problem

https://codeforces.com/problemset/problem/1328/A



思路：



##### 代码

```python
# n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    num = 0
    if a%b != 0:
        num =b- a%b
    print(num)
 

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241002160525200](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241002160525200.png)



### 427A. Police Recruits

https://codeforces.com/problemset/problem/427/A



思路：



##### 代码

```python
# n = int(input())
m = map(int,input().split())
police = 0
crime = 0
for i in m:
    if i == -1:
        if police==0:
            crime+=1
        else:
            police-=1
    else:
        police+=int(i)
print(crime)


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241002162102195](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241002162102195.png)



### 02808: 校门外的树

http://cs101.openjudge.cn/practice/02808/



思路：



##### 代码

```python
# L,M=[int(x)for x in input().split()]
s = set()
for i in range(M):
    a,b = map(int,input().split())
    s.update(range(a,b+1))
print(L+1-len(s))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241002162906725](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241002162906725.png)



### sy60: 水仙花数II

https://sunnywhy.com/sfbj/3/1/60



思路：



##### 代码

```python
# a,b = map(int,input().split())
s =[]
x=True
for i in range(a,b+1):
    j = str(i)
    if int(j[0])**3+int(j[1])**3+int(j[2])**3==i:
        s.append(j)
        x = False
if x:
    print("NO")
else:
    print(" ".join(s))

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241002164348434](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241002164348434.png)



### 01922: Ride to School

http://cs101.openjudge.cn/practice/01922/



思路：



##### 代码

```python
# import math
while True:
    try:
        n = int(input())
        if n == 0:
            break
        m =[]
        for i in range(n):
            V,T = map(int,input().split(   ))
            if T<0:
                continue

            ti =math.ceil( T+(4500/(V*5/18)))
            m.append(ti)

        print(min(m))
    except EOFError:
        break

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241003202926335](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241003202926335.png)



## 2. 学习总结和收获

这次作业题目有点难，最后一题看了半天没有看懂觉得挺难，就去看了答案，感觉实际上代码不是很难写，关键是思路问题，自己的数学思维不太行，希望以后能够加强。以及感觉自己有点畏难情绪，看不懂的题不是很有钻研精神，容易放弃，希望能改进吧。

在做每日选做的题目，赶到了九月二十六号，装箱问题之前那几天的题目写得还蛮顺利的，还以为自己终于进步了，结果从装箱问题开始就不会了，举步维艰啊啊啊。感觉没什么信心了哈哈。但是还是再坚持做题吧，加油吧。





