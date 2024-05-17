# words=["one","two","three"]
# for x in words:               #for loop
#     print(x)


# i=0                          #while loop
# while i<6:
#     print(i)
#     i=i+1


#jump statements
# x=1
# while x<10:                      #break statement
#     print("x:",x)
#     if x==5:
#         print("breaking")
#         break
#     x+=1
# print("end")

# for letter in "python":                 #continue statement
#     if letter== "h":
#         continue
#     print("current Letter:",letter)

pay=0
amount=1200
if amount >1000:
    pay=amount*10/100
print("discount",amount-pay)