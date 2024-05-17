#multiplying 2 non-negative integers as a strings 
class Solution(object):
    def multiply(self, num1, num2):
        ans=int(num1)*int(num2)
        return str(ans)
num1 = "2"
num2 = "3"
s=Solution()
print(s.multiply(num1,num2))
        