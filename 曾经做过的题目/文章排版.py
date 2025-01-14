n = int(input())
m = map(str,input().split())
num=0
s = []
for i in m:
    num+=len(i) #空格也算字符，经过了一下ai
    if s:
        num+=1
    if num<= 80:
        s.append(i)
    if num>80:
        print(" ".join(map(str,s)))
        num = len(i)
        s = [i]
if s:
    print(" ".join(map(str,s)))
