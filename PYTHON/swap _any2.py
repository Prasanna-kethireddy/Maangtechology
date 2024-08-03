list=[12,34,45,56,87,78]
#approch1
# pos1,pos2=1,3
# list[pos1],list[pos2]=list[pos2],list[pos1]
# print(list)

#approach 2
# pos1,pos2=1,3
# f=list.pop(pos1)
# s=list.pop(pos2-1)
# list.insert(pos1,s)
# list.insert(pos2,f)
# print(list)

#approac 3
pos1,pos2=1,3
get=(list[pos1],list[pos2])
list[pos2],list[pos1]=get
print(list)