# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>万馨雅 城环</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：



代码：

```python
num = 1
while True:
    p,e,i,d = map(int,input().split())
    if p+e+d+i==-4:
        break
    p=p%23
    e=e%28
    i=i%33
    s=d+1
    while (s-p)%23!=0 or (s-e)%28!=0 or (s-i)%33!=0:
        s+=1

    s-=d
    print(f'Case {num}: the next triple peak occurs in {s} days.')
    num+=1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241025183800756](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241025183800756.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：



代码：

```python
p = int(input())
n = [int(x) for x in input().split()]
n.sort()

cnt=0
i=0
j=len(n)-1

while i<=j:
    if p>=n[i]:
        p-=n[i]
        cnt+=1
        i+=1
    else:
        if j == i:
            break
        if cnt>0:
            p+=n[j]
            cnt-=1
            j-=1
        else:
            break
print(cnt)
```



代码运行截图 ==（至少包含有"Accepted"）== 



![image-20241025125404752](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241025125404752.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：从后往前加



代码：

```python
n = int(input())
t = list(map(int,input().split()))
c=[]
d=[]
num=0
k=1
l=n-2
for i in range(1,n+1):
    c.append((t[i-1],i))
c.sort(key = lambda x:(x[0],x[1]))
for j in c:
    d.append(j[1])
while k<n:
    num+=c[l][0]*k
    k+=1
    l-=1
num=num/n
print(" ".join(map(str,d)))
print(format(num,".2f"))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241025193636457](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241025193636457.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：



代码：

```python
n=int(input())
print(n)
dic1={"pop":0, 'no': 20,'zip':40, 'zotz':60, 'tzec':80, 'xul':100, 'yoxkin':120,'mol':140, 'chen':160, 'yax':180, 'zac':200, 'ceh':220, 'mac':240, 'kankin':260,'muan':280, 'pax':300, 'koyab':320, 'cumhu':340,'uayet':360}
dic2={1:'imix',2: 'ik',3: 'akbal',4: 'kan',5: 'chicchan', 6:'cimi', 7:'manik',8:'lamat', 9:'muluk', 10:'ok',11:'chuen', 12:'eb',13:'ben', 14:'ix',15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac',0: 'ahau'}
for _ in range(n):
    d,MY = input().split(". ")
    m,y = MY.split(" ")
    num=int(y)*365+dic1[m]+int(d)+1
    Y=num//260
    if num%260==0:
        Y-=1
    D=num%13
    if D==0:
        D=13
    name = dic2[num%20]
    print(D,name,Y)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241025220627262](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241025220627262.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：



代码：

```python
n = int(input())
c=[]
for _ in range(n):
    c.append(tuple(map(int,input().split())))
i=1
if n>1:
    num=2
else:
    num=1
k=[0]*n
for i in range(1,n-1):
    if c[i][0]-c[i][1]>c[i-1][0]+k[i-1]:
        num+=1
    else:
        if c[i][0]+c[i][1]<c[i+1][0]:
            num+=1
            k[i]=c[i][1]
print(num)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241026233020163](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241026233020163.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：



代码：

```python
import math
num = 0
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break 
    num += 1  
    islands = []
    possible = True
    for _ in range(n):
        x, y = map(int, input().split())
        if y > d: 
            possible = False
        else:
            distance = math.sqrt(d * d - y * y)
            l = x - distance
            r = x + distance
            islands.append((l, r))
    input()
    if not possible:
        print(f'Case {num}: -1')
        continue

    islands.sort(key=lambda x: x[1])

    cnt = 0
    i = 0
    while i < n:
        cnt += 1
        current_radar = islands[i][1]
        while i < len(islands) and islands[i][0] <= current_radar:
            i += 1

    print(f'Case {num}: {cnt}')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241027215453406](C:\Users\kivvii\AppData\Roaming\Typora\typora-user-images\image-20241027215453406.png)



## 2. 学习总结和收获

前两题之前每日选做写到了，后面四道严格来说只有排队做实验是完全自己独立做出来的，其余都看了测试数据或者询问他人or ai（不敢想woodcutters那题要是没有数据会卡多久，完全忘记了n=1的情况，玛雅日历也没有考虑到是260整数的情况。） 感觉难，需要花很多时间，但是现在每题都能有一点点思路能自己写一下（虽然写不对），感觉已经有一点点进步了。

每日选做还是没有跟上啊啊觉得每天写一题都好费劲。感觉完蛋了但还是加油一下吧哈哈

学到了很多包括双指针前缀和等等等等，但还没有能看到题目就能意识到用该方法的敏感度，以及准确编写的能力。



