tup = (10,20,30)
x, y, z = tup
print ("x: ", x, "y: ", "z: ",z)

tup1= (10,20,30)
x, *y = tup1
print ("x: ", "y: ", y)

tup2= (10,20,30, 40, 50, 60)
*x, y, z = tup2
print ("x: ",x, "y: ", y, "z: ", z)
