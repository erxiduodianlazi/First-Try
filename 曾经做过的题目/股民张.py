a=list(map(int,input().split()))
min_num=a[0]
max_num=0
for i in a:
    if i < min_num:
        min_num=i
    max_num=max(max_num,i-min_num)
print(max_num)