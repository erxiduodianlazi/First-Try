n = int(input())
c=[]
num=1
for _ in range(n):
    c.append(tuple(map(int,input().split())))
c.sort(key = lambda x:x[1])
end_line=c[0][1]
for i in range(1,n):
    if c[i][0] > end_line:
        num+=1
        end_line=c[i][1]
print(num)