v=3
for i in range(1,5):
    for j in range(0,v):
       print(" ",end="")
    v=v-1
    for k in range(0,2*i-1):
        print("*",end="")
    print()
v=1
for i in range(3,0,-1):
    for j in range(0,v):
       print(" ",end="")
    v=v+1
    for k in range(0,2*i-1):
        print("*",end="")
    print()
