# convert kilometers into miles

kilometers=float(input("Enter the kilometers"))
def convert(x):
    return x*0.621371
val=convert(kilometers)
print("%0.2f kilometers is equal to %0.2f miles"%(kilometers,val))
    