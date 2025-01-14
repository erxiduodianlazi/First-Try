H,L,n=map(int,input().split())
speed=list(map(int,input().split()))
speed.sort()
v=speed[n//2]
t=L/v
h=H-(0.5*10*(t**2))
print(f'{h:.2f}')