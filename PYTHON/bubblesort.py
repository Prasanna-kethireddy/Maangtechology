# def bubble(arr):
#     n=len(arr)
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#             arr[j]>arr[j+1]
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# input=input("enter the elements : ")
# arr=list(map(int,input.split()))
# print("Before sorting " ,arr)
# result=bubble(arr)
# print("After sorting ",result)

def bubble(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[90,89,78,67,56,45,34,23,12,98,87,76,65,54,43,32,21]
print("Before sorting ",arr)
result=bubble(arr)
print("after sorting " ,result)

