n = int(input())
a=0;b=0;c=0
max_number=0
for i in range(2,n+1):
    for j in range(2,n+1):
        for k in range(1,n+1):
            if (i+j)%2==0 and (j+k)%3==0 and(i+j+k)%5==0:
                if i+j+k>max_number:
                    max_number=i+j+k


print(max_number)