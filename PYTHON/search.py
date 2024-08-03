# list=[1,23,34,12,45,65,76]
# n=23
# flag=0
# for i in range(len(list)):
#     if list[i]==n:
#         print("Element found")
#         flag=1
#         break
# if(flag==0):
#     print("element not found")
    
        
# list=[12,34,56,78,934,34]
# n=100
# if(n in list):
#     print("element found")
# else:
#     print("element not found")


def search(numbers,n):
    flag=0
    for i in range(len(numbers)):
        if numbers[i]==n:
            return 'element found'
            flag=1
    if flag==0:
        return 'not found'
numbers=[12,23,34,45,66]
n=34
list=search(numbers,n)
print(list)