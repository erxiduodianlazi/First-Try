#自己写的蠢版
s=input()
num=1
previous=s[0]
c=[]
for i in s:
    if i !=previous:
        num+=1
        previous=i
    else:
        c.append(num)
        num=1
if num!=1:
    c.append(num)
print(max(c))

#不用创建列表比较
s= input()
num=1
max_result=1
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        num+=1
        max_result=max(max_result,num)
    else:
        num=1
print(num)