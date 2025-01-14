# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==万馨雅 城市与环境学院==



**说明：**

1）Oct⽉考： AC6== 3 == 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：



代码

```python
k = int(input())
s = input()
b='abcdefghijklmnopqrstuvwxyz'
c=[]
for i in s:
    t = i.lower()
    d = int(b.index(t))-k
    if i.isupper():
        c.append(b[d%26].upper())
    else:
        c.append(b[d%26])
print(''.join(c))

```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241013170344185](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241013170344185.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：



代码

```python
m, n = input().split()
m = m.replace(m[2], '')
n = n.replace(n[2], '')
print(int(m)+int(n))

```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20241013171203737](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241013171203737.png)

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：



代码

```python
n = int(input())
t = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
g = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

for j in range(n):
    m = str(input())
    num = 0
    for i in range(17):
        num += int(m[i]) * t[i]
    num = num % 11
    if g[num] == m[-1]:
        print("YES")
    else:
        print("NO")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241013170913925](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241013170913925.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：



代码

```python
n = int(input())

while n > 1:
    if n % 2 != 0:
        print(f'{n}*3+1={n*3+1}')
        n=n*3+1
    else:
        print(f'{n}/2={n//2}')
        n=n//2
print("End")

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241013171511460](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241013171511460.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：



##### 代码

```python
# n = input()
c=[]
a={1:'I',4:'IV',5:"V",9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
b={'I':1,'V':5,'X':10,"L":50,"C":100,"D":500,"M":1000}
if n[0] in ['1','2','3','4','5','6','7','8','9']:
    n = int(n)
    while n>0:
        if n>=1000:
            c.append(a[1000]*(n//1000))
            n-=(n//1000)*1000
        elif  n>=900:
            c.append(a[900])
            n-=900
        elif n>=500:
            c.append(a[500])
            n-=500
        elif n>=400:
            c.append(a[400])
            n-=400
        elif n>=100:
            c.append(a[100]*(n//100))
            n-=(n//100)*100
        elif n >=90:
            c.append(a[90])
            n-=90
        elif n>=50:
            c.append(a[50])
            n-=50
        elif n>=40:
            c.append(a[40])
            n-=40
        elif n>=10:
            c.append(a[10]*(n//10))
            n-=(n//10)*10

        elif n==9:
            c.append(a[9])
            n-=9
        elif n>=5:
            c.append(a[5])
            n-=5
        elif n==4:
            c.append(a[4])
            n-=4
        else:
            c.append(n*a[1])
            n=0

    print(''.join(c))
else:
    num=0
    i=0
    while i <len(n):
        if i+1<len(n) and b[n[i]]<b[n[i+1]]:
            num+=b[n[i+1]]-b[n[i]]
            i+=2
        else:
            num+=b[n[i]]
            i+=1
    print(num)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241013171634422](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241013171634422.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：



代码

```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==





## 2. 学习总结和收获

考试的时候只写出来三题，大崩溃。第一题写半天一直编译错误，也不知道负数可以取模，搞来搞去搞了半天没写出来。罗马数字和数字互换那题也写了很久，不会把数字转成罗马数字。排队看很多大佬也没写出来，自己还没到那个水平就不尝试了。

还有很容易出现一些小错误，比如写for i in range(n)时忘记写range（），.upper()写掉后面的括号等等，导致程序错误。还有没带草稿纸没有地方推算。

收获也挺多，学到了ord和chr的转换，体会到了字典的好处。

每日选做写到十月初了，感觉大家已经会很多了，我还在地上爬哈哈。加油吧。











