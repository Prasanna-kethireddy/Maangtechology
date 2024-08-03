def quicksort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[len(arr)//2]
        left=[x for x in arr if x < pivot ]
        middle=[x for x in arr if x==pivot]
        right=[x for x in arr if x> pivot]
        return quicksort(left)+middle+quicksort(right)
arr=[12,56,87,43,78,32,90,3]
print(quicksort(arr))