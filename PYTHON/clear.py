list=[12,34,45,567,68]
print("before clearing the list : ",list)
#approach1  using clear method 
# list.clear()

#approach 2 re intializing
# list=[]

#approach 3
# list[:]=[]

#approach 4
# del list[:]

#approach 5 using loop
# while len(list)>0:
#     list.pop()

#approach 6 using *=
list *=0

print("after clearing the list",list)