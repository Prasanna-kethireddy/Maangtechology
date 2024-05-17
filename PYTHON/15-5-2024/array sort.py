# import array as arr
# a = arr.array('i', [10,5,15,4,6,20,9])
# for i in range(0, len(a)):
#    for j in range(i+1, len(a)):
#       if(a[i] > a[j]):
#          temp = a[i];
#          a[i] = a[j];
#          a[j] = temp;
# print (a)



import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print (a)