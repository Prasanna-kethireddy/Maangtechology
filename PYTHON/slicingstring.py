# print the string that takes 1st and last 2 letters then concatenate , if string is less than 2 print empty string
def string_slice(string):
    if len(string) < 2:
        return 'empty'
    return string[0:2]+ string[-2:]
string=str(input("Enter the string : "))
print(string_slice(string))