# ! Полиндром для числа
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        rev=0
        while(x>0):
            dig=x%10
            rev=rev*10+dig
            x=x//10
        if(temp==rev):
            return True
        else:
            return False


# ! Палиндром для строки
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")