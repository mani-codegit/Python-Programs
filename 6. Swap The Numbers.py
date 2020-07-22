#swap the numbers
#inputs
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))


#1.Swap numbers using temporary variables
temp=num1
num1=num2
num2=temp

"""
#2.swap the numbers without using temporary variables
num1=num1+num2
num2=num1-num2
num1=num1-num2

"""
print(f"\n***Using  temp***\nNow The First number is {num1}\nThe Second number is {num2}")
#print(f"\n***Without temp***\nNow The First number is {num1}\nThe Second number is {num2}")