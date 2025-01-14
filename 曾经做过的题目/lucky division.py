n = int(input())
m=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
num=0
for i in m:
    if n % i == 0:
        num+=1
        print("YES")
        break
if num ==0:
    print("NO")


n = int(input())

for i in {4,7,47,74,447,474,477,747,774}:
    if n%i == 0:
        print('YES')
        break
else:
    print('NO')

   #another
def check(x):
    s =str(x)
    return[False,True][s.count('4')+s.count('7')==len(s)]
n = int(input())
for i in range(1,1+n):
    if n % i == 0 and check(i)==True:
        print("YES")
        break
else:
    print("NO")