p={1:{'name':'kapil','age':21,'sex':'male'},2:{'name':'Praveen','age':20,'sex':'male'},3:{'name':'Maynak','age':21,'sex':'male'}}
print(p)
print(p[1]['name'])
print(p[1]['age'])
print(p[1]['sex'])
#addd element using create a new dictionary
p[3]={}
p[3]['name']='Bhavesh'
p[3]['age']=20
p[3]['sex']='male'
p[3]['married']='NO'
print(p[3])
#add elemet in dict using non empty dict create
p[4]={'name':'kapilsharma','age':22,'sex':'male','married':'no'}
print(p[4])
print(p)

#delete an element from nested dictionary using del
del p[3]['married']
del p[4]['married']
print(p[3])
print(p[4])
print(p)
#Iterating Through a nested dictionary
for p_id,p_info in p.items(): #both item and key
    print('Person _ID',p_id)
    for key in p_info:
       print(key+":",p_info[key])
