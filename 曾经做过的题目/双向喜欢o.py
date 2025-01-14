#本人喜欢的浪费时间的嵌套循环法
n,q=map(int,input().split())
c=[]
like = False
for i in range(q):
    c.append(tuple(map(int,input().split())))
for j in range(q):
    for i in range(q):
        if c[j][0]==c[i][1] and c[j][1]==c[i][0]:
            like = True
            break
if like:
    print("Yes")
else:
    print("No")

#高级的矩阵法

def main():
    import sys
    input = sys.stdin.readline
    data = input().split()

    n = int(data[0])
    q = int(data[1])

    exists=[[False]*(n+1) for i in range(n+1)]
    result = False

    index=2
    for _ in range(q):
        a=int(data[index])
        b=int(data[index+1])
        index+=2

        exists[a][b]=True
        if exists[b][a]:
            result = True

    print("Yes" if result else "No")

if __name__ == "__main__":
    main()
