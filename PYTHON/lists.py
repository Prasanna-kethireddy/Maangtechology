list1=["prassu","sai",12,234]
list2=[1,2,3,4,45]
print(list1[0])
print(list2[0:5])

list=["hello","rgukt",1998,2000]
print("value available in index 2:")
print(list[2])
list[2]=2003
print("new value available at index 2:")
print(list[2])
del list[2]
print("list after deleting")
print(list)

list3 = ["a", "b", "c", "d"]
list4 = [25.50, True, -55, 1+2j]
list5 = ["Rohan", "Physics", 21, 69.75]
list6 = [1, 2, 3, 4, 5]

print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 2 to last in list3", list3[2:-1])
print ("Items from index 0 to index last in list4", list4[:])
