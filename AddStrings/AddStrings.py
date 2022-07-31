class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str_to_int(n):
            integer = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
            num = 0
            for i in n:
                num = num * 10 + integer[i]
            return num
        res = str_to_int(num1) + str_to_int(num2)
        return str(res)