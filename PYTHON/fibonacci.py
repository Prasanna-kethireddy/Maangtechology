# def fibonacci(a,b):
#     sum=0
#     for i in range(1,10):
#         sum=a+b
#         print(sum)
#         a=b
#         b=sum
# a=int(input("Enter the number :"))
# b=int(input("enter the number : "))
# print(fibonacci(a,b))
        
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))