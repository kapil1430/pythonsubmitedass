i=int(input("Enter Row"))
j=int(input("Enter Col"))
for r in range(0,i):
    for c in range(r,j):
        print('*',end="")   
    print()
for r in range(1,i+1):
    for c in range(0,r):
        print("*",end="")
    print()
