s = input()
s=s.lower()
m = [0]*5
index =0
target='hello'
for i in s:
    if i == target[index]:
        m[index]=1
        index+=1
    if index==5:
        break
if sum(m)==5:
    print('YES')
else:
    print("NO")


#正则表达式
import re
s=input()
r = re.search("h.*e.*l.*l.*o",s)
print(['YES',"NO"][r==None])