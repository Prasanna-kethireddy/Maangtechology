#find the largest number among the three input numbers
#l=[22,45,67]
#print(max(l));
num1=float(input("Enter the number 1:"));
num2=float(input("Enter the number 2:"));
num3=float(input("Enter the Number 3:"));
if (num1>=num2) and (num1>=num3):
    largest=num1;
elif(num2>=num1) and (num2>=num3):
    largest=num2;
else:
    largest=num3;
print("Largest number is",largest);