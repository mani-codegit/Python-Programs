#Squre roots

#1.squre root using exponent
def squreroot(x):
    result=x**0.5
    return result

""""#2.squre root using math.sqrt method
import math
def sqrtmethod(x):
    result=math.sqrt(x)
    return result
#3.squre root using pow method
def sqrtpow(x):
    result=math.pow(x,0.5)
    return result"""
 
#squre
def squre(x):
    result=x*x
    return result

#input
number=float(input("Enter the number: "))


#calling the functions
print("squre root  value is ",squreroot(number))
print("squre value is ",squre(number))