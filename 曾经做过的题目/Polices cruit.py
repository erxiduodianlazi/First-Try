n = int(input())
a = list(map(int,input().split()))
num = 0
office = 0
for i in range(n):
    if a[i]==-1 and office ==0:
        num += 1
        continue
    if a[i]>0:
        office+=a[i]
        continue
    office-=1
print(num)




n = int(input())
m = map(int,input().split())
police = 0
crime = 0
for i in m:
    if i == -1:
        if police==0:
            crime+=1
        else:
            police-=1
    else:
        police+=int(i)
print(crime)
