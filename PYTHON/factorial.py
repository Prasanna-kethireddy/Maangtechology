# def factorial(num):
#     if num<0:
#         print('factorail does not exist')
#     elif num==0 or num==1:
#         print('factorial is 1')
#     else:
#         result=1
#         for i in range(1,num+1):
#             result=result*i
#         return result
# num=int(input("Enter the number : "))
# print(factorial(num))


def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
n=5
print(factorial(n))