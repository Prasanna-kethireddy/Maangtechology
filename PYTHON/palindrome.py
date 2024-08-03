def palindrome(string):
    return string==string[::-1]
string=str(input("Enter the string : "))
s=palindrome(string)
if s:
    print("{0} is a palindrome".format(string))
else:
    print("{0} is not a palindrome".format(string))