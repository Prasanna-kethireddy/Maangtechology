# list=[12,23,345,56,7,8,89]
# r=list[::-1]
# print(r)

# list.reverse()
# print(list)

# def reversing(list):
#     reverse_list=[]
#     n=len(list)
#     for i in range(n-1,-1,-1):
#         reverse_list.append(list[i])
#     return reverse_list
# input=input("enter the numbers with space : ")
# list=tuple(map(int,input.split()))
# print(reversing(list))

# def reverse(s):
#     result=' '
#     for i in s:
#         result=i+result
#     return result
# s='python'
# print("original string : ",s)
# print("reversed string :",reverse(s))

# str='prasanna'
# str=str[::-1]
# print(str)

str='prasanna'
result=''.join(reversed(str))
print(result)