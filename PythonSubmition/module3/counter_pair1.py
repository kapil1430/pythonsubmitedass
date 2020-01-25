sum1=input("enter the value of sum:")
sum1=int(sum1)
l=[]
no=int(input("enter the no of elements in array"))
for i in range(no):
    a=int(input())
    l.append(a)
    
for j in range(len(l)):
    for k in range(len(l[1:])):
        sum2=l[j]+l[k]
        if sum2==sum1:
            print(l[j],l[k])
        else:
          pass
