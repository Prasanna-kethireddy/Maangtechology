#taking values from user
from array import *
arr=array('i',[])

n=int(input("Enter the size of array :"))

for i in range(n):
    x=int(input("enter the values :"))
    arr.append(x)

print(arr)


