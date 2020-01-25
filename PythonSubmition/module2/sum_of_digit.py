keyboard=int(input("Enter 5 Digit Number"))
sumv=0
temp=keyboard
while(temp>0):
    rem=temp%10
    sumv=sumv+rem
    temp=temp//10

print(sumv)
    
