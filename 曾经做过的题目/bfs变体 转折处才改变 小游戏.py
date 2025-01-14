#







#不知道为什么是错的，，，但是就是一直不对呵呵
directions=[(1,-1,0),(2,1,0),(3,0,-1),(4,0,1)]
from collections import deque
def bfs(x1,y1,x2,y2,c):
    q=deque()
    q.append((y1,x1,0,-1))
    iq[y1][x1]=True
    ans=[]
    while q:
        y,x,seg,pre_direction,=q.popleft()
        if y == y2 and x == x2:
            ans.append(seg)
            break
        for direction,dy,dx in directions:
            ny = y+dy; nx = x+dx
            if 0<=ny<h+2 and  0<=nx<w+2  and not iq[ny][nx]:
                new_direction=direction
                new_seg = seg if new_direction==pre_direction else seg+1
                if ny==y2 and nx==x2:
                    ans.append(new_seg)
                    continue
                if c[ny][nx]!='X':
                    iq[ny][nx]=True
                    q.append((ny,nx,new_seg,new_direction))
    if len(ans)==0:
        return -1
    else:
        return min(ans)

num1=0
while True:
    w,h = map(int,input().split())
    if w==h==0:
        break

    num1+=1
    print(f'Board #{num1}:')
    c = [' '*(w+2)]+[' '+input()+' 'for i in range(h)]+[' '*(w+2)]
    iq=[[False] * (w+2) for i in range(h+2) ]
    num2=0
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==x2==y1==y2==0:
            break
        num2+=1
        result=bfs(x1,y1,x2,y2,c)
        if result !=-1:
            print(f'Pair {num2}: {result} segments.')
        else:
            print(f'Pair {num2}: impossible.')
    print()