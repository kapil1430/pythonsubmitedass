n,v,s,t=3,0,1,0
for i in range(1,9):
    if i>=1 and i<=3:
        print(" "*n,end="")
        print("*"*(i+v))
    elif i==4  :
        print("#"*0,end="")
        print("*"*(i*2-1))
    else :
        print(" "*(s*1),end="")
        print("*"*(i*1-t))
        s=s+1
        t=t+3
    n=n-1
    v=v+1


        
        
