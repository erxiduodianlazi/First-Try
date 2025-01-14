def fan_tian(n,fp,wp,tp):
    if n==0:
        return None
    fan_tian(n-1,fp,tp,wp)
    print(f'{fp}->{tp}')
    fan_tian(n-1,wp,fp,tp)


n=int(input())
print(2**n-1)
fan_tian(n,'A','B','C')