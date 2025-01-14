n=int(input())
print(n)
dic1={"pop":0, 'no': 20,'zip':40, 'zotz':60, 'tzec':80, 'xul':100, 'yoxkin':120,'mol':140, 'chen':160, 'yax':180, 'zac':200, 'ceh':220, 'mac':240, 'kankin':260,'muan':280, 'pax':300, 'koyab':320, 'cumhu':340,'uayet':360}
dic2={1:'imix',2: 'ik',3: 'akbal',4: 'kan',5: 'chicchan', 6:'cimi', 7:'manik',8:'lamat', 9:'muluk', 10:'ok',11:'chuen', 12:'eb',13:'ben', 14:'ix',15:'mem', 16:'cib', 17:'caban', 18:'eznab', 19:'canac',0: 'ahau'}
for _ in range(n):
    d,MY = input().split(". ")
    m,y = MY.split(" ")
    num=int(y)*365+dic1[m]+int(d)+1
    Y=num//260
    if num%260==0:
        Y-=1
    D=num%13
    if D==0:
        D=13
    name = dic2[num%20]
    print(D,name,Y)