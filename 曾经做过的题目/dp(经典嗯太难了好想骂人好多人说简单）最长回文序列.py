#双指针，中心扩散法，不是指从最中心扩散，而是把每个锚点当作最中心去处理，去向两侧扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<2:
            return(s)
        else:
            start = 0;max_len=1
            def kuosan(x,y):
                while x>=0 and y<n and s[x]==s[y]:
                    x-=1
                    y+=1
                return x+1,y-1
            for i in range(n):
                x1,y1=kuosan(i,i)
                x2,y2=kuosan(i,i+1)
                if y1-x1+1>max_len:
                    start,max_len=x1,y1-x1+1
                if y2-x2+1>max_len:
                    start,max_len=x2,y2-x2+1
            return s[start:start+max_len]

#dp


#题解逆天单指针
class Solution(object):
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            start = max(i - len(res) -1, 0)
            temp = s[start: i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res

