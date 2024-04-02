#check whether the given word is palindrome or not
#input= mom , malayalam
#output=mom , malayalam
def is_palindrome(string):
    return string==string[::-1]
string=str(input("Enter the word:"))
yes=is_palindrome(string)
if yes:
    print("{0}  is a palindrome".format(string))
else:
    print("{0} is not a palindrome ".format(string))