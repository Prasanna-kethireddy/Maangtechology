f=open("file.txt",'w+')
print("Name of the file : ",f.name)
print("closed or not : " ,f.closed)
print("opening mode : ",f.mode)
f.close()