# marks=int(input("Enter the marks:"))
# result=""               
# if marks<30:                  #if elif else statement
#     result="failed"
# elif marks>70:
#     result="passed with distinction"
# else:
#     result="passed"
# print(result)


# def checkvowel(n):
#     match n:                         #match-case statement which is also used for decision making
#         case "a":return "vowel"
#         case "e":return "vowel"
#         case "i":return "vowel"
#         case "o":return "vowel"
#         case "u":return "vowel"
#         case _ :return "consonant"
# print(checkvowel("a"))
# print(checkvowel("p"))
# print(checkvowel("e"))

# age=int(input("enter the age:"))
# if age >=18:
#     print("You are eligible to vote") 
# else:
#     print("you are not eligible to vote")
    

# discount=0
# amount=int(input("Enter the amount:"))
# if amount>10000:
#     discount=amount*20/100
# elif amount>5000:
#     discount=amount*10/100
# elif amount>1000:
#     discount=amount*5/100
# else:
#     discount=0
# print("payable amount is ",amount-discount)


num=int(input("Enter the number:"))
print('num=',num)
if num%2==0:
    if num%3==0:
        print("num is divisible by both 2 and 3")
    else:
        print("Divisible by 2 not 3")
else:
    if num%3==0:
        print("divisible by 3 not 2")
    else:
        print("not divisible by both the numbers")
