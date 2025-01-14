s = set()
s.update(input())
if len(s)%2 == 1:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')


a = set(input())
b = len(a)
if b %2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')