# def myfunction(a: int, b: int):
#    c = a+b
#    return c
   
# print (myfunction(10,20))
# print (myfunction("Hello ", "Python"))      # function annotation


# def myfunction(a: int, b: int) -> int:
#    c = a+b
#    return c

# def myfunction(a: "physics", b:"Maths" = 20) -> int:
#    c = a+b
#    return c
# print (myfunction(10))                        #function with default arguments
 
# def myfunction(a: "physics", b:"Maths" = 20) -> int:
#    c = a+b
#    return c
# print (myfunction.__annotations__)


def division(num: dict(type=float, msg='numerator'), den: dict(type=float, msg='denominator')) -> float:
   return num/den
print (division.__annotations__)