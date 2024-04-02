#check if a given number is prime or not
#prime numbers are a positive numbers that are greater than 1 that also have no other factors except for 1 and the number itself.
def is_prime(number):
    if number>1:
        for num in range(2,number): #(2,2,3,4)
            if number%num==0:
                print("{0} is not a prime number".format(number))
        return "prime number"
    return "not a prime number"
number=int(input("Enter the number:"))#5
print(is_prime(number))