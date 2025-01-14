n = int(input())
m = list(map(int,input().split()))
num = 1
for i in range(1,n):
    if m[i]>=m[i-1]:
        num+=1
    if m[i]<m[i-1]:
        print("NO")
        break
if num==n:
    print("YES")
    #蠢办法，们换一个简洁一点的

#for else 的应用
n = int(input())
m = list(map(int,input().split()))
for i in range(1,n):
    if m[i]<m[i-1]:
        print("NO")
        break
else:
    print("YES")

#也很高级的每次都忘记的True和False
n = int(input())
m = list(map(int,input().split()))
a = True
for i in range(1,n):
    if m[i]<m[i-1]:
        a=False
print(["NO","YES"][a])
print("YES" if a else "NO" )