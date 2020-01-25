s=int(input("size Selles"))
wholes=0
for i in range(0,s):
    while(True):
        wcos=int(input("Cost"))
        if wcos>0:
            wholes+=wcos
            break;
        else:
            pass
retail=wholes*0.5
print("Retail Price",retail)
