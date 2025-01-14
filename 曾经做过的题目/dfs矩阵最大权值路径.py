#自己写的ai改对的
def dfs(cnt, x, y):
    global e
    global num
    if x == n and y == m:
        num.append((cnt, e.copy()))
        return
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not d[nx][ny] and c[nx][ny] != float('-inf'):
            d[nx][ny] = True
            e.append((nx, ny))
            dfs(cnt + c[nx][ny], nx, ny)
            d[nx][ny] = False
            e.pop()

n, m = map(int, input().split())
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
c = [[float('-inf')] * (m + 2)] + [[float('-inf')] + list(map(int, input().split())) + [float('-inf')] for _ in range(n)] + [[float('-inf')] * (m + 2)]
d = [[False] * (m + 2) for _ in range(n + 2)]
num = []
e = [(1, 1)]

d[1][1] = True
dfs(c[1][1], 1, 1)

num.sort(key=lambda x: x[0], reverse=True)
for x, y in num[0][1]:
    print(x, y)


#模板上的
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
# 定义⽅向
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 右、下、左、上
visited = [[False] * m for _ in range(n)] # 标记访问
max_path = []
max_sum = -float('inf') # 最⼤权值初始化为负⽆穷
# 深度优先搜索
def dfs(x, y, current_path, current_sum):
    global max_path, max_sum
# 到达终点，更新结果
    if (x, y) == (n - 1, m - 1):
        if current_sum > max_sum:
            max_sum = current_sum
            max_path = current_path[:]
        return
# 遍历四个⽅向
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
# 检查边界和是否访问过
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
# 标记访问
            visited[nx][ny] = True
            current_path.append((nx, ny))
# 递归搜索
            dfs(nx, ny, current_path, current_sum + maze[nx][ny])
# 回溯
            current_path.pop()
            visited[nx][ny] = False
# 初始化起点
visited[0][0] = True
dfs(0, 0, [(0, 0)], maze[0][0])
# 输出结果
for x, y in max_path:
    print(x + 1, y + 1)




def dfs(cnt,x,y):
    global e
    global num
    if x==n and y==m:
        num.append((cnt,e))
        e=[(1,1)]
        return
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<n+2 and 0<ny<=m+2 and not d[nx][ny]:
            d[nx][ny]=True
            e.append((nx,ny))
            cnt+=c[nx][ny]
            dfs(cnt,nx,ny)
            d[nx][ny]=False


n,m=map(int,input().split())
directions=[(1,0),(-1,0),(0,1),(0,-1)]
c=[[float('-inf')] * (m+2)]+[[float('-inf')]+list(map(int,input().split())) +[float('-inf')] for _ in range(n)]+[[float('-inf')] * (m+2)]
d=[[False]*(m+2) for _ in range(n+2)]
num=[]
e=[(1,1)]
dfs(c[1][1],1,1)
num.sort(key=lambda x:x[0],reverse=True)
for x,y in num[0][1]:
    print(x,y)



