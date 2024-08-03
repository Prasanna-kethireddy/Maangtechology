# list=['prassu','sai','sai','prasanna']
# word='sai'
# count=0
# for i in range(1,len(list)-1):
#     if (list[i]==word):
#         count+=1
#         if (count>1):
#             del list[i]
#             print(list)

def occurence(list,element):
    count=0
    for i in range(len(list)):
        if list[i]==element:
            count+=1
            if count>1:
                del list[i]
                return list
    return list
list=['prassu','sai','prassu']
element='prassu'
updated_list=occurence(list,element)
print(updated_list)