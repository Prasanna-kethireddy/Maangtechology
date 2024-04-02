#removing punctuations from a string
punctuations="!@#$%^&*()_+-=><,."
string=str(input("Enter the string:"))
new_string=""
for c in string:
    if c not in punctuations:
        new_string=new_string+c
print(new_string)