# s1="WORD"
# print ("original string:", s1)
# l1=list(s1)

# l1.insert(3,"L")

# print (l1)

# s1=''.join(l1)
# print ("Modified string:", s1)

import array as ar

s1="WORD"
print ("original string:", s1)

sar=ar.array('u', s1)
sar.insert(3,"L")
s1=sar.tounicode()

print ("Modified string:", s1)              #array modifying using method (tounicode)


