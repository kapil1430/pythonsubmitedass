i=input("Subject And Marks")
summ,per=0,0
j=0
l=i.split(" ")
nli=[]
for i in range(0,len(l)):
    if l[i]!='=':
        nli=l.append(l[i])
        
for k in range(0,len(nli)):
    summ+=int(nli[k])
    j=j+1
per=summ/j
print("Sum::",summ)
print("Percentage",per)

        
