def common():
    str1=input("enter the string 1 : ")
    str2=input("Enter the string 2  : ")
    s1=set(str1)
    s2=set(str2)
    li=s1 & s2
    print(li)
    print(len(li))
common()