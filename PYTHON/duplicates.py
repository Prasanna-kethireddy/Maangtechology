def dividing(arr):
    count={}
    for i in arr:
        if i in count:
            count[i]=count[i] +1
        else:
            count[i] =1
    print(count)
    duplicates=[]
    uniques=[]
    for i in arr:
        if count[i] >1:
            if i not in duplicates:
                duplicates.append(i)
        else:
            uniques.append(i)
    return uniques, duplicates
arr=[12,34,56,67,78,90,12,34,78,1,2,6,8,9,94]
duplicates,uniques=dividing(arr)
print("duplicates : ",duplicates)
print("uniques : ",uniques)




# def dividing(arr):
#     count={}
#     for i in arr:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1

#     duplicates=[] 
#     uniques=[]
#     for i in arr:
#         if count[i]>1:
#             if i not in duplicates:
#                 duplicates.append(i)
#         else:
#             uniques.append(i) 
#     return duplicates,uniques
        
# arr=[12,34,12,56,34,65,12,90,45]
# duplicates,uniques=dividing(arr)
# print('duplicates',duplicates)
# print('uniques',uniques)
           
    
        
                