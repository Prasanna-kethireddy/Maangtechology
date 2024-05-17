#python program to check leap year
#condition leap year must be divided by 4 , if it is divided
# then check if it is divided by 100 or not , not divided 100 only  leap year 
# if it is divided by 100 then check if it is divided by 400 0r not
def checkyear(year):
    return(((year % 4==0) and (year % 100 !=0)) or (year % 400==0))
year=int(input("Enter the year:"))
if checkyear(year):
    print("{0} is a leap year".format(year))
else:
    print("{0} is Not a leap year".format(year))