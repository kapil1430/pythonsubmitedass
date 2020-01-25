s=int(input("Enter The Size"))
li=[]
nli=[]
nli2=[]
print("Enter Element")
for i in range(0,s):
    ele=int(input())
    li.append(ele)
li.sort()
for i in range(0,len(li)):
    c=li[i]
    c1=li.count(c)
    nli.append(c1)
for i in range(0,len(nli)):
    v=nli.index(max(nli))
    d=li[v]
    nli2.append(d)
    nli[v]=0
print(nli2)
