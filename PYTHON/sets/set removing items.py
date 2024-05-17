# lang1 = {"C", "C++", "Java", "Python"}
# print ("Set before removing: ", lang1)
# lang1.remove("Java")
# print ("Set after removing: ", lang1)
# lang1.remove("C")                                  #using remove


# lang1 = {"C", "C++", "Java", "Python"}
# print ("Set before discarding C++: ", lang1)
# lang1.discard("C++")
# print ("Set after discarding C++: ", lang1)
# print ("Set before discarding PHP: ", lang1)
# lang1.discard("PHP")
# print ("Set after discarding PHP: ", lang1)                 #usoing discard



# lang1 = {"C", "C++"}
# print ("Set before popping: ", lang1)
# obj = lang1.pop()
# print ("object popped: ", obj)
# print ("Set after popping: ", lang1)
# obj = lang1.pop()
# obj = lang1.pop()                                            #using pop

# lang1 = {"C", "C++", "Java", "Python"}
# print (lang1)
# print ("After clear() method")
# lang1.clear()
# print (lang1)                                              #using clear

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print ("s1 before running difference_update: ", s1)
# s1.difference_update(s2)
# print ("s1 after running difference_update: ", s1)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print ("s1: ", s1, "s2: ", s2)
# s3 = s1.difference(s2)
# print ("s3 = s1-s2: ", s3)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print ("s1: ", s1, "s2: ", s2)
# s1.intersection_update(s2)
# print ("a1 after intersection: ", s1)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print ("s1: ", s1, "s2: ", s2)
s3 = s1.symmetric_difference(s2)
print ("s1 = s1^s2 ", s3)