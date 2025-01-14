#自己写的超时版
s=input()
m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    num = 0
    for j in range(a,b):
        if s[j] == s[j-1]:#遍历很慢很缓慢
            num+=1
    print(num)
#结合了一下的动态规划版
s= input()
m = int(input())
num = 0
ans = [0] #为什么这么写具体看typaro
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        num+=1
    ans.append(num)
for j in range(m):
    a,b =map(int,input().split())
    print(ans[b-1]-ans[a-1])
