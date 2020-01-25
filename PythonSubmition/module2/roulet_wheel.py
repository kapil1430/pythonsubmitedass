kb=int(input("Enter NO 0 to  36"))

color=kb%2

if kb==0:
    print("GREEN")
elif kb>=1 and kb<=10:
    if color==0:
        print("Black")
    else:
        print("Red")
elif kb>=11 and kb<=18:
    if color==0:
        print("Red")
    else:
        print("Black")
elif kb>=19 and kb<=28:
    if color==0:
        print("Black")
    else:
        print("Red")

elif kb>=29 and kb<=36:
    if color==0:
        print("Red")
    else:
        print("Black")
else:
    print("Invalid")

    
