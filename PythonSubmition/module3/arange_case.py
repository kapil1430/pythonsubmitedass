i=input("Enter String")
tp=tuple(i)
lo=""
up=""
for l in range(0,len(tp)):
    if tp[l].islower():
        lo +=tp[l]
    else:
        up+=tp[l]
print(lo+up)
