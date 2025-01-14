import heapq

def yao(n,c):
    consumed=[]
    health=0
    for i in range(n):
        health+=c[i]
        heapq.heappush(consumed,c[i])
        if health<0:
            if consumed:
                health-=consumed[0]
                heapq.heappop(consumed)
    return len(consumed)


n=int(input())
c=list(map(int,input().split()))
print(yao(n,c))
