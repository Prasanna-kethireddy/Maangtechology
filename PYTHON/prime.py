#check if a given number is prime or not
#prime numbers are a positive numbers that are greater than 1 that also have no other factors except for 1 and the number itself.
def prime(number):
    if number >1:
        for i in range(2,number):
            if number%i==0:
                return 'not a prime'
        return 'its prime'
    return 'not a prime'
number=int(input("Enter the number: "))
print(prime(number))

# def prime(number):
#     count=0
#     if number>1:
#         for i in range(1,number+1):
#             if (number%i)==0:
#                 count=count+1
#         if count==2:
#             print('prime')
#         else:
#             print('not a prime ')
# number=int(input("enter the number: "))
# print(prime(number))