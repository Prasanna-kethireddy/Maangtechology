import array as ar
# a=ar.array('i',[12,34,45,67,89])
# a.append(10)
# print(a)                            #using append method


# a=ar.array("i",[12,23,34,45])
# a.insert(1,89)
# print(a)                             #using insert



a=ar.array("i",[12,23,34,45,56,67])
b= ar.array('i',[12,23,34,45,56,67,78,89])
a.extend(b)
print(a)  