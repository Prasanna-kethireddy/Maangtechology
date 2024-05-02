list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)

list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)

list3 = ["a", "b", "c", "d"]
print ("Original list: ", list3)
del list3[2]
print ("List after deleting: ", list3)

list4= [25.50, True, -55, 1+2j]
print ("List before deleting: ", list4)
del list4[0:2]
print ("List after deleting: ", list4)