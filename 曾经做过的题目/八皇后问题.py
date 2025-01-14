def safe(row,col,path):
    for i in range(row):
        if path[i] == col or abs(path[i]-col)==abs(i-row):
            return False
    return True
def queen(row,path,used,result):
    if len(path)==8:
        result.append(path[:])
        return

    for col in range(1,9):
        if used[col]:
            continue
        if safe(row,col,path):
            path.append(col)
            used[col]= True
            queen(row+1,path,used,result)

            path.pop()
            used[col]=False

def eight(n):
    used=[False]* 9
    result=[]
    path=[]
    queen(0,path,used,result)
    print(''.join(map(str,result[n-1])))
T=int(input())
for _ in range(T):
    n = int(input())
    eight(n)



