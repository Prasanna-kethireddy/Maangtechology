# from array import *

# vals=array('i',[5,4,34,-5,45])
# vals.reverse()
# # print(vals[0])
# # for i in range(5)
# for i in range(len(vals)):
#     print(vals[i])



# import array as ar
# a=ar.array("i",[12,233,434,56,565])
# b=ar.array("i")
# for i in range(len(a)-1,-1,-1):
#     b.append(a[i])
# print(a,b)



import array as ar
a=ar.array("i",[12,32,34,556,676,78])
print("frist array",a)
b=a.tolist()
print("array into a list",b)
b.reverse()
print("Reversed list",b)
a=ar.array("i")
a.fromlist(b)
print(a)

