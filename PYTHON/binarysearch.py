# def binary(arr,x,low,high):
#     while low<=high:
#         mid=low +(high-low)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             low=mid-1
#         else:
#             low=mid+1
#     return -1
# arr=[1,3,34,56,34,2,3,6,7,6,8]
# x=6
# result=binary(arr,x,0,len(arr)-1)
# print(result)
# if result==-1:
#     print("element not found ")
# else:
#     print("element at index",{result})


def binary(arr,x,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            return binary(arr,x,mid+1,high)
        else:
            return binary(arr,x,mid-1,high)
    return -1
arr=[12,34,56,78,90]
x=78
result=binary(arr,x,0,len(arr)-1)
print(result)
if result==-1:
    print("element not found")
else:
    print("Element at index ",{result})
