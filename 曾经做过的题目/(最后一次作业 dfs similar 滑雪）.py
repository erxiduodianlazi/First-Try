#直接用表来记录，就不需要反复递归看有没有不能进行了
R, C = map(int, input().split())  # 输入行数和列数
c = [list(map(int, input().split())) for _ in range(R)]  # 输入矩阵

# 初始化记忆化表
memo = [[-1] * C for _ in range(R)]

# 定义四个方向
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(x, y):
    # 如果已经计算过，直接返回记忆化的结果
    if memo[x][y] != -1:
        return memo[x][y]

    max_length = 1  # 每个点至少有路径长度为1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 检查是否可以滑向更低的高度
        if 0 <= nx < R and 0 <= ny < C and c[nx][ny] < c[x][y]:
            max_length = max(max_length, 1 + dfs(nx, ny))  # 更新路径长度

    memo[x][y] = max_length  # 保存结果到记忆化表
    return max_length


# 遍历所有点，找出最长路径
result = 0
for i in range(R):
    for j in range(C):
        result = max(result, dfs(i, j))

print(result)

#自己隔了一天又写了一遍
r,c=map(int,input().split())
m=[list(map(int,input().split())) for _ in range(r)]
dp=[[-1]*c for _ in range(r)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    max_length=1
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and m[nx][ny]<m[x][y]:
            max_length=max(dfs(nx,ny)+1,max_length)
    dp[x][y]=max_length
    return max_length
result=0
for i in range(r):
    for j in range(c):
        result=max(result,dfs(i,j))
print(result)

#就算修改了也是tle
R,C=map(int,input().split())
visited=[[False]*C for i in range(R)]
c=[list(map(int,input().split())) for i in range(R)]
max_distance=0
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y,distance):
    global max_distance
    you = False
    for dx,dy in directions:
        nx,ny=x+dx,y+dy

        if 0<=nx<R and 0<=ny<C and not visited[nx][ny] and c[nx][ny]<c[x][y]:
            you=True
            visited[nx][ny]=True
            dfs(nx,ny,distance+c[x][y]-c[nx][ny])
            visited[nx][ny]=False

    if not you:
        if distance>max_distance:
            max_distance=distance
            return max_distance #又错了全局变量不可以代表一切！！但它并不意味着 dfs 函数能够自动整合所有递归调用的结果。
            # 递归的核心在于其返回值。如果你的递归逻辑只通过全局变量来记录结果，
            # 而没有返回值，其他递归分支不会感知到更新后的 max_distance。
for i in range(R):
    for j in range(C):
        dfs(i,j,0)
print(max_distance+1)