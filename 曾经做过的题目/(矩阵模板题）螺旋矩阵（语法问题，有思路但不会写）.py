#老师想让我们会的答案的方法哈哈
n=int(input())
s=[[401]*(n+2)]
c= s+[[401]+[0]*n+[401] for i in range(n)]+s
dirl=[[0,1],[1,0],[0,-1],[-1,0]]
row=1
col=1
N=0
drow,dcol=dirl[0]
for j in range(1,n*n+1):
    c[row][col]=j
    if c[row+drow][col+dcol]:
        N+=1
        drow,dcol=dirl[N%4]
    row+=drow
    col+=dcol

for i in range(1,n+1):
    print(" ".join(map(str,c[i][1:-1])))


#通义千问法
def matrix(n):
    c=[[0]*n for _ in range(n)]
    num=1
    top=0;bottom=n-1;left=0;right=n-1
    while num<=n*n:
        for i in range(left,right+1):
            c[top][i]=num
            num+=1
        top+=1
        for j in range(top,bottom+1):
            c[j][right]=num
            num+=1
        right-=1
        for l in range(right,left-1,-1):
            c[bottom][l]=num
            num+=1
        bottom-=1
        for k in range(bottom,top-1,-1):
            c[k][left]=num
            num+=1
        left+=1
    return c

def xing(c):
    for i in c:
        print(" ".join(map(str,i)))


n= int(input())
p_matrix = matrix(n)
xing(p_matrix)