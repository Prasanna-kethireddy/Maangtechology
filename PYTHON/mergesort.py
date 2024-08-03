# def merge(left, right):
#     merged = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):  # Fix the condition here
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             j += 1
#     merged += left[i:] + right[j:]
#     return merged

# def mergesort(arr):
#     if len(arr) <= 1:  # Update to handle empty arrays and arrays of length 1
#         return arr
#     mid = len(arr) // 2
#     left = mergesort(arr[:mid])
#     right = mergesort(arr[mid:])
#     return merge(left, right)

# arr = [12, 34, 45, 21, 30, 90, 23, 65, 89, 56]
# print(mergesort(arr))


def merge(left,right):
    merged=[]
    i=0
    j=0
    while i<len(left) and j< len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged+=left[i:]+right[j:]
    return merged
            
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[mid:])
    right=mergesort(arr[:mid])
    return merge(left,right)
arr=[12,90,89,78,23,45,93,56,29,30,51]
print(mergesort(arr))
    