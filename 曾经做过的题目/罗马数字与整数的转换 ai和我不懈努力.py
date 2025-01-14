#自己思路加ai
n = input()
c=[]
a={1:'I',4:'IV',5:"V",9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
b={'I':1,'V':5,'X':10,"L":50,"C":100,"D":500,"M":1000}
if n[0] in ['1','2','3','4','5','6','7','8','9']:
    n = int(n)
    while n>0:
        if n>=1000:
            c.append(a[1000]*(n//1000))
            n-=(n//1000)*1000
        elif  n>=900:
            c.append(a[900])
            n-=900
        elif n>=500:
            c.append(a[500])
            n-=500
        elif n>=400:
            c.append(a[400])
            n-=400
        elif n>=100:
            c.append(a[100]*(n//100))
            n-=(n//100)*100
        elif n >=90:
            c.append(a[90])
            n-=90
        elif n>=50:
            c.append(a[50])
            n-=50
        elif n>=40:
            c.append(a[40])
            n-=40
        elif n>=10:
            c.append(a[10]*(n//10))
            n-=(n//10)*10

        elif n==9:
            c.append(a[9])
            n-=9
        elif n>=5:
            c.append(a[5])
            n-=5
        elif n==4:
            c.append(a[4])
            n-=4
        else:
            c.append(n*a[1])
            n=0

    print(''.join(c))
else:
    num=0
    i=0
    while i <len(n):
        if i+1<len(n) and b[n[i]]<b[n[i+1]]:
            num+=b[n[i+1]]-b[n[i]]
            i+=2
        else:
            num+=b[n[i]]
            i+=1
    print(num)

#答案版
# 定义罗马数字和整数的映射关系
roman_to_int_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

# 定义整数到罗马数字的映射列表 (从大到小顺序)
int_to_roman_map = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]


# 罗马数字转整数
def roman_to_int(s):
    total = 0
    prev_value = 0
    for char in s:
        value = roman_to_int_map[char]
        if value > prev_value:
            total += value - 2 * prev_value  # 处理特殊情况，如IV, IX
        else:
            total += value
        prev_value = value
    return total


# 整数转罗马数字
def int_to_roman(num):
    result = []
    for value, symbol in int_to_roman_map:
        while num >= value:
            result.append(symbol)
            num -= value
    return ''.join(result)


# 主函数，判断输入是罗马数字还是整数
def main():
    # 输入处理
    input_data = input().strip()

    # 判断输入是整数还是罗马数字
    if input_data.isdigit():
        # 输入是整数
        num = int(input_data)
        print(int_to_roman(num))
    else:
        # 输入是罗马数字
        print(roman_to_int(input_data))


# 调用主函数
if __name__ == "__main__":
    main()