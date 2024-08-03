def anagrams(a,b):
    if len(a)!=len(b):
        print("Not anagrams")
    else:
        if sorted(a)==sorted(b):
            print("Anagrams")
        else:
            print("not anagrams")
a=str(input("Enter the str1 : "))
b=str(input("Enter the str2 : "))
c=anagrams(a,b)
print(c)