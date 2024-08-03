# approcah 1
list=[12,23,45,67,78,90]
# n=len(list)
# temp=list[0]
# list[0]=list[n-1]
# list[n-1]=temp
# print("list after swapping",list)

#approach 2
# list[0],list[-1]=list[-1],list[0]

# approach 3
# get=(list[-1],list[0])
# list[0],list[-1]=get

#approach 4
# start,*middle,end=list
# list=[end,*middle,start]

# approach 5 
f=list.pop(0)
l=list.pop(-1)
list.insert(0,l)
# list.insert(-1,f)
list.append(f)
print("list after swapping",list)