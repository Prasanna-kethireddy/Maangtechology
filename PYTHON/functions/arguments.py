 #4 types of arguments in python ....positional , keyword , default and variable length
 
# def person(name,age):
#     print(name)                     
#     print(age)

# person('prassu',21)                   #positional arguments



# def person(name,age):
#     print(name,age)
    

# person(name='prassu',age=21)              #keyword argument



# def person(name,age=18):
#     print(name,age)
    
# person('prassu',21)
# person('usha')                          #default argumemts


# def add(a,b):
#     c=a+b
#     print(c)
    
# add(2,4)                               #variable length

# def sum(a, *b):
#     c=a
#     for i in b:
#         c=c+i
#     print(c)

# sum(14,24,34,44)                          #variable length


def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum(14,24,34,44)