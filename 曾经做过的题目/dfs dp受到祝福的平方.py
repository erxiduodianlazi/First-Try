import math
def pingfang(B):
    if B==0:
        return False
    elif math.sqrt(B)==int(math.sqrt(B)):
        return True

def dfs(A,start):
    if start==len(A):
        return True
    for i in range(start+1,len(A)+1):
        B=int(A[start:i])
        if pingfang(B):
            if dfs(A,i):
                return True
    return False

A=int(input())
A=str(A)
if dfs(A,0):
    print("Yes")
else:
    print("No")