
#冒泡排序
# O(n^2)
n = int(input())
nums = input().split()
for i in range(n - 1):
    for j in range(i+1, n):
        #print(i,j)
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))

#错的错的错的自己写的
n= int(input())
c = input().split()
c.sort(key = lambda x: x[0])
for i in c:
    if len(i)==2 or len(i)==1:
        break
    c.sort(key=lambda x:(x[0],x[1],x[2]))
for i in c:
    if len(i)==1:
        break
    c.sort(key=lambda x:(x[0],x[1]))


c.reverse()
print(''.join(c),end = " ")
c.reverse()
print(''.join(c))

#看答案过后边抄边写的
import functools
def compare(x,y):
    if x+y>y+x:
        return -1
    elif x+y<y+x:
        return 1
    else:
        return 0
n=int(input())
c=list(map(str,input().split()))
c_max = sorted(c,key = functools.cmp_to_key(compare))
c_min= sorted(c,key = functools.cmp_to_key(lambda x,y:compare(y,x)))
print(''.join(map(str,c_max)),end = " ")
print(''.join(map(str,c_min)))

