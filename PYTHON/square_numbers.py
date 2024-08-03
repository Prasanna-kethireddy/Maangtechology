# def square(num):
#     squared_no=[]
#     for n in num:
#         squared_no.append(n**2)
#     return squared_no
# input = input("enter the numbers with space : ")
# num=list(map(int,input.split()))
# print(square(num))


def square(n):
    if n==0 or n==1:
        return 1 
    else:
        return n**2
n=2
print(square(n))



# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n * n)
#     return squared_numbers

# # Prompt the user for input
# input_numbers = input("Enter numbers separated by spaces: ")

# # Split the input string into a list of strings and convert each to an integer
# numbers = list(map(int, input_numbers.split()))

# # Call the function and print the result
# print(get_squared_numbers(numbers))
