n,m,k = map(int,input().split())
c=[]
for t in range(n):
    c.append([0]*m)

num=0

for _ in range(k):
    i,j = map(int,input().split())
    i -= 1
    j -= 1
    c[i][j]=1
    num+=1
    if i<n-1 and j<m-1 and  c[i+1][j+1]+c[i+1][j]+c[i][j+1]+c[i][j]==4:
        print(num)
        break
    elif i<n-1 and j>0and c[i+1][j]+c[i+1][j-1]+c[i][j-1]+c[i][j]==4:
        print(num)
        break
    elif j<m-1 and i>0and c[i-1][j+1]+c[i-1][j]+c[i][j+1]+c[i][j]==4:
        print(num)
        break
    elif i>0 and j>0 and c[i-1][j-1]+c[i][j-1]+c[i-1][j]+c[i][j]==4:
        print(num)
        break
else:
    print(0)


#答案版，保护圈，不用担心多加的一行，因为加黑色永远加不到那里
# http://codeforces.com/contest/508/submission/44603553
n,m,k = map(int, input().split())
mx = [(m+2)*[0] for i in range(n+2)]

# if square 2 × 2 formed from black cells appears, and
# cell (i, j) will upper-left, upper-right, bottom-left
# or bottom-right of this squares.

def square_check(i,j):
    if mx[i][j+1] and mx[i+1][j] and mx[i+1][j+1]:
        return True
    if mx[i][j-1] and mx[i+1][j-1] and mx[i+1][j]:
        return True
    if mx[i-1][j] and mx[i-1][j+1] and mx[i][j+1]:
        return True
    if mx[i-1][j-1] and mx[i-1][j] and mx[i][j-1]:
        return True
    return False

for i in range(k):
    x,y = map(int, input().split())
    mx[x][y] = 1
    if square_check(x,y):
        print(i+1)
        break
else:
    print(0)
