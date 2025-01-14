while True:
    try:
        n=int(input())
        m=list(map(int,input().split()))
        m.sort()
        l=m.pop()
        if l >sum(m):
            num=sum(m)
        else:
            num=(l+sum(m))/2
        print(f'{num:.1f}')
    except EOFError:
        break