class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {}
        for i in range(10):
            dic[str(i)] = i
        
        a = 0
        deci_pos = 1 
        for i in range(len(num1)-1,-1,-1):
            a += dic[num1[i]]*deci_pos
            deci_pos *= 10
            
        b = 0
        deci_pos = 1
        for i in range(len(num2)-1,-1,-1):
            b += dic[num2[i]]*deci_pos
            deci_pos *= 10
		
        return str(a*b)
        
        
        
        # sum_ = int(num1) * int(num2)
        # return str(sum_)