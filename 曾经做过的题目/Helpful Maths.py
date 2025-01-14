s = [int(i) for i in input().split("+")]
s.sort()
print("+".join(str(i) for i in s))