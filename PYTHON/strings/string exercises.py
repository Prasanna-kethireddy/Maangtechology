# string=' welcome to rgukt nuzvid , ab block cse'
# vowels='aeiou'
# count=0
# for x in string:
#     if x in vowels:
#         count+=1
# # print("number of vowels",count) 


string="10101"

def strtoint(string):
    for x in string:
        if x not in string:
            return "error , string with  non-binary characters"
        num=int(string,2)
        return num
print("binary :{} to integer :{}".format(string,strtoint(string)))
    
        