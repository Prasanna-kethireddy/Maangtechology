# n=int(input("Enter the number:"))
# temp=n
# l=len(str(n))
# sum=0
# while n!=0:
#     r=n%10
#     sum=sum+(r**l)
#     n=n//10
# if temp==sum:
#     print("{0} is an armstrong".format(n))
# else:
#     print("{0}is not an armstrong".format(n))       
    
    

def armstrong(num):
    temp=num
    n=len(str(num))
    sum=0
    while num>0:
        digit=num%10
        sum=sum+digit**n
        num=num//10
    if temp==sum:
        print("armstrong number")
    else:
        print("not an armstrong number")
num=int(input("enter the number : "))
print(armstrong(num))

# n=125
# d=n//1000
# print(d)