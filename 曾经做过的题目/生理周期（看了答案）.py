#用遍历乘起来相加超时，那为什么不除呢


#周期取模取模,wocao少一个.一直WA
num = 1
while True:
    p,e,i,d = map(int,input().split())
    if p+e+d+i==-4:
        break
    p=p%23
    e=e%28
    i=i%33
    s=d+1
    while (s-p)%23!=0 or (s-e)%28!=0 or (s-i)%33!=0:
        s+=1

    s-=d
    print(f'Case {num}: the next triple peak occurs in {s} days.')
    num+=1
