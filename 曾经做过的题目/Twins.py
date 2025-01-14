n = int(input())
a = list(map(int,input().split()))
a.sort()
a.reverse()
s =[]
num =0
for i in a:
    s.append(i)
    num+=1
    if sum(s)>sum(a)/2:
        print(num)
        break
#自己写对的

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = 0
c = sum(a)
k = 0
for i in a:
    b += i
    k += 1
    if b > c/2:
        break
print(k)