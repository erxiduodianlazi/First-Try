N = int(input())
m=0
for i in range(N):
    s = input()
    s = s.replace("### ###"," ")
    m += s.count("###")//2
print(m)
