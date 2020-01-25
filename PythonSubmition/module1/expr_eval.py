#program 1
a,b,x,y=4,2,5,4
result=5*b*b*x-3*a*y*y-8*b*b*x+10*a*y
print(result)

#program 2
a,y,c=2,3,7
cal=4*a*y/c-a*y/c
print(cal)

#program 3
try:
 a,b,c,y=4.4,0.0,4.2,3.0
 ans=c+a*y*y/b
 print(ans)
except:
    print("Cant divide by zero")
