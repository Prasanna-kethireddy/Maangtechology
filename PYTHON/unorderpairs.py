def unordered_pairs(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(str(array[i] )+ ',' + str(array[j]))
array=[12,12,3,45,565,67,90]
unordered_pairs(array)