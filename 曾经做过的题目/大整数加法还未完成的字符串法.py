m = input()
n = input()
c = []
if len(m) == len(n):
    print(int(m) + int(n))
else:
    if len(m) > len(n):

        n=n.zfill(len(m))

    else:
        m=m.zfill(len(n))

    n = [i for i in n]
    n.reverse()

    m = [j for j in m]
    m.reverse()

    carry=0
    for i in range(len(m)):
        d = int(m[i]) + int(n[i])
        total = d+carry

        if total >=10:
            carry=1
            c.append(total-10)

        else:

            c.append(total)
            carry = 0
    if carry !=0:
        c.append(carry)

    c.reverse()

    result=''.join(map(str, c))
    result =result.lstrip('0')


    print(result)