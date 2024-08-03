# def rotation(string):
#     n=len(string)
#     temp=string+string
#     for i in range(0,n):
#         for j in range(0,n):
#             print(temp[i+j],end='')
#         print()
# string='PRASSU'
# rotation(string)




#checking str is substring of rotated string
def check(str1,str2):
    if(len(str1)!=len(str2)):
        return False
    n=len(str1)
    s=str1+str1
    if(str2 in s):
        print(str1, "is matching with " ,str2)
    else:
        print(str1 ,"is not matching with ",str2)
check('anu','nur')
