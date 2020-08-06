#find the sum of all natural numbers upto N
num=int(input("Enter the number"))
sum=0
while(num>0):
    sum+=num
    num-=1
print(f"The sum is {sum}")