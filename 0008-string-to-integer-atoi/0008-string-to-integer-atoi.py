class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        if len(s)==0: return 0
        
        if s[0] == "-" or s[0] == "+":
            sign = -1 if s[0]=="-" else 1
            s = s[1:len(s)]
        
            
        num = 0;
        for c in s:
            char = ord(c)-48
            if char in range(0,10):
                num*=10
                num+=char
            else:
                break
        if num*sign >= 2147483647:
            return 2147483647
        if num*sign < -2147483647:
            return -2147483648
        return sign*num
