n,m,a = map(int,input().split())
import math
b = math.ceil(n/a)
c = math.ceil(m/a)
print(b*c)