n=10
for i in range(0,10):
    if i>=1 and i<=4:
        print(" "*(int(n/2)),end="")
        print("*")
    elif i==5:
        print("*"*(n+1))
    else:
        print(" "*(int(n/2)),end="")
        print("*")
print()
