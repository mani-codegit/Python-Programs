#Area of the triangle 
b=float(input("Enter the breath :"))
h=float(input("Enter the height :"))
def triangle(b,h):
    result=1/2*b*h
    return result
tri=triangle(b,h)


"""
#area of the triangle
a=float(input("Enter the first side: "))
b=float(input("Enter the second side: "))
c=float(input("Enter the third side: "))

s=(a+b+c)/2

#Heron's Formula
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The are of the triangle is %.2f" %area)
"""



print("Area of the Triangle is: ",tri)