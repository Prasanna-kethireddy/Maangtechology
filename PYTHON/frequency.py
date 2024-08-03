# def frequency(str):
#     str=input("Enter the string : ")
#     l=str.split()
#     d={}
#     for i in l:
#         if i not in d.keys():
#             d[i]=0
#         d[i]=d[i]+1
#     print(d)
# frequency(str)



#character frequency ina a string
def frequency(str):
    str=input("Enter the string : ")
    li=list(str)
    d={}
    for i in li:
        if i not in d.keys():
            d[i]=0
        d[i]+=1
    print(d)
frequency(str)