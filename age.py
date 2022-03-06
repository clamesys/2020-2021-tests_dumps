a = ["n","N","y","Y"]
for x in a:
    age = input("What's Your Age? :: ")
    print()
    if '.' in age:
        age = float(age)
    else:
        age = int(age)
    if age <=9 : 
        print ("Small")
    elif age <= 18 :
        print ("Medium")
    else:
        print ("Big")
    print()
    x=input("wanna do again? (y/n) :: ")
    if x == "N":
        break
    elif x == "n":
        break
    elif x == 'Y':
        continue
    elif x == 'y':
        continue
    else:
        print("invalid input")
        break
    