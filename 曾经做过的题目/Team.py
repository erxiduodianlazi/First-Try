n = int(input())
num = 0
for i in range(n):
    x,y,z=map(int,input().split())
    if x+y+z>=2:
        num+=1
print(num)
