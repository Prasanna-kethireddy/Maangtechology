def selection(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
                arr[i],arr[min]=arr[min],arr[i]
    return arr      
arr=[12,34,54,6,7,8,344,78]
result=selection(arr)
print(result)
              
#               def selection(arr):
#     n=len(arr)
#     for i in range(n):
#         min=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min]:
#                 min=j
#         arr[i],arr[min]=arr[min],arr[i]
#     return arr
# arr=[12,90,34,67,89,38,18,27,30,80]
# print("Before sorting",arr)
# result=selection(arr)
# print("After sorting ",result)  