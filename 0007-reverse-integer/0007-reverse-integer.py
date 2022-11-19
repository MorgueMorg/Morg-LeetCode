class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        
        if x[0] == "-":
            sign = -1
        else:
            sign = 1
            
        x = x.lstrip("-")
        x = x.lstrip("+")
        
        x = x[::-1]
        
        int_x = int(x) * sign
        
        if int_x > 2**31-1:
            return 0
        elif int_x < -2**31:
            return 0
        else:
            return int_x
        
