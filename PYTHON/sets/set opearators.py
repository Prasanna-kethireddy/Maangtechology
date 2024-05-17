# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s3 = s1 | s2
# print ("Union of s1 and s2: ", s3)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s3 = s1 & s2
# print ("Intersection of s1 and s2: ", s3)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s3 = s1 - s2
# print ("Difference of s1 - s2: ", s3)
# s3 = s2 - s1
# print ("Difference of s2 - s1: ", s3)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s1 - s2
print ("Difference of s1 - s2: ", s3)
s3 = s2 - s1
print ("Difference of s2 - s1: ", s3)
s3 = s1 ^ s2
print ("Symmetric Difference in s1 and s2: ", s3)