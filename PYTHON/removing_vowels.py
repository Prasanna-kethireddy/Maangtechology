# def vowels_remove(str):
#     vowels='aeiouAEIOU'
#     for c in str:
#         if c in vowels:
#             str=str.replace(c,'')
#     return str
# str='prasanna'
# result=vowels_remove(str)
# print(result)


def vowels_remove(str):
    vowels='aeiouAEIOU'
    s=''
    for c in str:
        if c not in vowels:
            s=s+c
    return str
str='prasanna'
result=vowels_remove(str)
print(result)