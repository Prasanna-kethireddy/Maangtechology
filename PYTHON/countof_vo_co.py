str=input("Enter the string : ")
vowelslist='aeiouAEIOU'
vowelscount=0
consonantscount=0
for i in str:
    if i in vowelslist:
        vowelscount+=1
    else:
        consonantscount+=1
print("count of vowels : {}".format(vowelscount))
print("count of consonants : {}".format(consonantscount))