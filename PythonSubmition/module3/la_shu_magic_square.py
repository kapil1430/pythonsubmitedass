l1=[4,9,2]
l2=[3,5,7]
l3=[8,1,6]
for i in range(len(l1)):
    for j in range(len(l1[1:])):
        sum1=l1[i]+l1[j]
for i in range(len(l2)):
    for j in range(len(l2[1:])):
        sum2=l2[i]+l2[j]
for i in range(len(l3)):
    for j in range(len(l3[1:])):
        sum3=l2[i]+l3[j]
if sum1==sum2 and sum2==sum3:
  sum4=l1[0]+l2[0]+l3[0]  
  sum5=l1[1]+l2[1]+l3[1]
  sum6=l1[2]+l2[2]+l3[2]
  if sum4==sum5 and sum5==sum6:
      for i in range(len(l1[0])):
          for k in range(len(l2[1])):
              for j in range(len(l3[2])):
                  sum7=l1[i]+l2[j]+l3[k]
      for i in range(len(l3[1])):
          for k in range(len(l2[-2])):
              for j in range(len(l3[-3])):
                  sum8=l1[i]+l2[j]+l3[k]
                  if sum7==sum8:
                      print("the matrix is equal")
