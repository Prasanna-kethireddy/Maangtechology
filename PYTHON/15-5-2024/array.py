from array import *

vals=array("i",[1,2,3,4,5])
# #vals = array("f",[2.23,34.4,45.56])  #float values
# #vals=array("I",[1,2,4,5])          #signed int
# print(vals.buffer_info())          #it is a tuple of address and size of an array 
newarr=array(vals.typecode,(a for a in vals))

for e in newarr:
    print(e)