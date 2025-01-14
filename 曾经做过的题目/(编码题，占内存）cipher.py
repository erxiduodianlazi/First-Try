

#还是超时了，不能用这个方法
from functools import lru_cache
@lru_cache(maxsize=None)

def yunzhuan(n):
    while True:
        if n==0:
            break
        m=list(map(int,input().split()))
        while True:
            c=input()
            d=''
            message=''
            if int(c[0])==0:
                break
            for i in range(len(c)):
                if c[i].isdigit():
                    d=d+c[i]
                else:
                    message+=c[i+1:]
                    break
            k=int(d)
            while k!=0:
                f=[]
                while len(message)<n:
                    message+=' '
                for i in range(n):
                    f.append((m[i],message[i]))
                f.sort(key = lambda x:x[0])
                message=''
                for i in range(n):
                    message+=f[i][1]
                k-=1
            print(message)


n=int(input())
yunzhuan(n)

