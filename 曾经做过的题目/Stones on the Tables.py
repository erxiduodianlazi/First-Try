n =int(input())
m =input()
output=0
p = m[0]
for i in range(1,n):
    if m[i] == p:
        output+=1
    else:
        p = m[i]
print(output)

n =int(input())
m =input()
output=0
for i in range(1,n):
    if m[i] == m[i-1]:
        output+=1
print(output)
