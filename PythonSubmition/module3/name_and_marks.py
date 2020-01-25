nm=input("NAME AND MARKS")
l=nm.split(",")
th,pr=0,0
thm=l[1:6]
prm=l[6:8]
for mkTh in range(0,len(thm)):
    th+=int(thm[mkTh])
    
for mkp in range(0,len(prm)):
    pr+=int(prm[mkp])

tot=th+pr
agg=(tot/500)*100;
print(l[0],"obtained",th,"marks out of 460 in theory and",pr,"marks out of 40 in the Practical and successfully Passed the Exam with",agg,"aggregate, May Congratulation to",l[0])
