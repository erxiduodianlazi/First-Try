s = input()
if s[0].islower():
    s[0].upper()
print(s)
#Python 中的字符串是不可变的，这意味着你不能直接修改字符串中的某个字符。你需要创建一个新的字符串来包含更改后的值


s = input()
if s[0].islower():
    s = s[0].upper() + s[1:]
print(s)