s=int(input("Enter Size"))
l1=[]
l2=[]
sum1=0
sum2=0
print("Element Of N1")
for i in range(0,s):
    l=int(input())
    l1.append(l)
print("Element Of N2")
for i in range(0,s-1):
    m=int(input())
    l2.append(m)
tot=sum(l1)-sum(l2)
print("Missing value",tot)
