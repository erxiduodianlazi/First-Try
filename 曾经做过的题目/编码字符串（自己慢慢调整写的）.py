n = input().lower()
num = 1
for i in range(1,len(n)):
    if n[i]== n[i-1]:
        num+=1
    else:
        print(f'({n[i-1]},{num})',end="")
        num=1

print(f'({n[-1]},{num})')