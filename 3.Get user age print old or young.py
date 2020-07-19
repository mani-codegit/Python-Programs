#Get the user age print old or young"

# str function
def strinput():
    name=str(input("Enter your name "))
    return name

#call the functions
name=strinput()

#try catch
while True:
    try:
        age=int(input("Enter your age: "))
    except ValueError:
        print("please enter your age correcly")
    else:
        break


if age<20:
    print(f" Hello {name} you are kid")
elif age>=20 and age<=35:
    print(f" Hello {name} you are young")
elif age>35 and age<=60 :
    print(f" Hello {name} you are  nearest to old")
else:
    print(f" Hello {name} you are old")