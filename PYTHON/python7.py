#check whether number is armstrong or not
#153, number count =3 , so 1^3+5^3+3^3 = 153 then only it is armstrong number
def is_armstrong(num):
 temp=num
 n=len(str(num))
 sum=0
 while num!=0:
     r=num%10
     sum=sum+(r**n)
     num=num//10
 if temp==sum:
     print("It is arm strong number")
 else:
    print("not an armstrong number")
num=int(input("Enter the number:"))
print(is_armstrong(num))
    