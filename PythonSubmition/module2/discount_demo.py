pk=int(input("Enter The Packae Qty"))
t=99*pk
dis=0
if pk>=10:
    dis=10
elif pk>=20:
    dis=20
elif pk>=50:
    dis=30
elif pk>=100:
    dis=40
else:
    print("NO Discount Amount")
    print("Total Amount OF Purchased",t)
totd=(dis/100)*t
print("Discount",totd)
print('Total Amount OF purchased',t-totd)
