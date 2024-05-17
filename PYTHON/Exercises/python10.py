#adding or sum of two lists by using map and lamda function
#example: [1,2,3]+[1,2,3]=[2,4,6]
l1=[1,2,3]
l2=[1,2,3]
print("Original list")
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2) #has no.of parameters but having only one equation or(expression)
print("sum of 2 lists")
print(list(result)) # map value converting in to a list