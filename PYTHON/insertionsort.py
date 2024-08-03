def insertion(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
arr=[12,89,90,67,45,23,56,39]
print("before sorting ",arr)
result=insertion(arr)
print("after sorting ",result)

