n = int(input())
for i in range(n):
    x=input()
    if len(x)>10:
        print(f'{x[0]}{len(x)-2}{x[-1]}')
    else:
        print(x)

for _ in range(int(input())):
	a = input()
	l = len(a)
	print(a if l<11 else a[0]+str(l-2)+a[l-1])
