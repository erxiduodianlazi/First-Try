n = int(input())
m = list(map(int,input().split()))
m.sort()
wait = 0
happy = 0
for i in m:
    if i>=wait:
        happy+=1
        wait+=i
print(happy)

#不知道为啥不对,知道了，greedy，不服条件直接摆在后面就行
n =int(input())
m =list(map(int,input().split()))
m.sort()
print(m)
j = [0]*n
j[0]=m[0]
for i in range(1,n):
    j[i]=j[i-1]+m[i]
    print(j)
num = 1
for i in range(1,n):
    if m[i]>=j[i-1]:
        num+=1
print(num)