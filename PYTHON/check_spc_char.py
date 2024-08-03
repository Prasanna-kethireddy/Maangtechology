punctuations='!@#$%^&*()_+-=[]{}|:;<>,./?'
string=str(input("Enter the String :"))
new_string=''
for c in string:
    if c not in punctuations:
        new_string+=c
print(new_string)