#check if the input number odd or even 
#a number is even if division by 2 gives remainder 0 
#if the remainder is 1 , it is an odd number
num=int(input("Enter the Number:"));
if num%2==0:
    print("{0}is an even number".format(num));
else:
    print("{0} is an odd number".format(num));