#Adding multiple numbers

a=[] #list
Entry=str(input("Do you want to add the numbers "))
while (Entry=="yes" or Entry=="Yes"): 
    ask=input("Are you add the numbers ")
    if(ask=="yes" or ask=="Yes"):
        cal=int(input("Enter the number: "))
        a.append(cal)
        continue
    elif(ask=="no" or ask=="No"):
        break
    else:
        print("you pressing the wrong key")
        continue
            
else:
    print('program has been stop')
total=sum(a)    
print("\n ******The Total values are*****",total)