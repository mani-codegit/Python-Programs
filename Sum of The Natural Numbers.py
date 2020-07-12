#sum of natural numbers
sum=0
number=int(input("Enter the number"))
while number>0:
    sum=sum+number
    print(sum)
    number-=1
print("\nThe Sum of The Natural Number is",sum)