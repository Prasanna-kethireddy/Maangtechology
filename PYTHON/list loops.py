lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')
   
   
lst1= [25, 12, 10, -21, 10, 100]
indices = range(len(lst1))
for i in indices:
   print ("lst[{}]: ".format(i), lst1[i])