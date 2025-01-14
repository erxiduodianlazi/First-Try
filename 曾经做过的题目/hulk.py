n = int(input())
m = ""
for i in range(1,n):
    if i % 2 ==0:
        m += " that I love"
    else:
        m += " that I love"
print("I hate" , m , "it")

m = int(input())
s=[]
for i in range(m):
    s.append(["I hate","I love"][i % 2])
print('that'.join(s),end='it\n')
