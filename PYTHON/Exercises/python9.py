# write a python  function to  sum of numbers in a list
# s=[1,2,3,4]
# print
def sum(numbers):
    total=0
    for x in numbers:
        total=total+x;
    return total
numbers=[10,20,30,40]
print(sum(numbers))
        