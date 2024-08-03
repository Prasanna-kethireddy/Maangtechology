# def multiple(numbers):
#     total=1
#     for i in numbers:
#         total*=i
#     return total
# numbers=[1,2,3,5]
# print(multiple(numbers))

#using numpy package
import numpy
list=[1,2,3,5]
result=numpy.prod(list)
print(result)
