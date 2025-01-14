n,K = map(int,input().split())
num = 0
output = []
g = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
while n>0:
    numm = n%K
    n=n//K

    if numm in g:
        output.append(g[numm])
    else:
        output.append(numm)
output.reverse()
print(''.join(map(str,output)))


