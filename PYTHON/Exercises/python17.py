n=int(input("Enter the number:"))
temp=n
l=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**l)
    n=n//10
if temp==sum:
    print("{0} is an armstrong".format(n))
else:
    print("{0}is not an armstrong".format(n))       