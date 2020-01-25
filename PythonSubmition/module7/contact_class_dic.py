import pickle
class Information:
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_Email(self):
        return self.email
    def set_Email(self,email):
        self.email=email
    def get_Phone(self):
        return self.phone
    def set_Phone(self,phone):
        self.phone=phone
    def get_Address(self):
        return self.address
    def set_Address(self,address):
        self.address=address
    def __str__(self):
        return f'{self.name} {self.email} {self.phone} {self.address} '
    
def ADDNewDetails():
    name=input('Enter Name')
    email=input('Enter Email')
    phone=input('Enter Phone')
    add=input('Enter Address')
    o=Information(name,email,phone,add)
##    This  Data Moves to File
##    fo=open('Contact InformationList.txt','a+')
##    l= name+" "+phone+" "+email+" "+add
##    pickle.dump(l,fo)
##    fo.close()
    return o
def SearchName(name,objectDict):
    for key,val in objectDict.items():
        if val.get_name()==name:
                print("YOur Search Name Present",name,"Details",objectDict[key].__str__())
                return key
        else:
             print('NO Such Entry Is Available Now Thanks Visit Again')
            
def SearchDATA(name,objectDict):
    for key,val in objectDict.items():
        if val.get_name()==name:
            print("YOur Search Name Present",name)
            print("Details:",objectDict[key].__str__())
        else:
            print('NO Such Entry Is Available Now Thanks Visit Again')

               
def Change_Phone(name,objectDict):
    searchNamed=searchName(name,objectDict)
    print("Your search Name",name)
    print("Its Object Key",searchNamed)
    contact=int(input('Enter New PHONE NUMBER'))
    objectDict[key].set_Phone(contact)
    print(objectDict[key].get_Phone())
    print('Successfull Change Contact Details At',name,objectDict[key].get_Phone())
def DeleteContact(name,objectDict):
    for key,val in objectDict.items():
        if val.get_name()==name:
             del objectDict[key]
             print("This Name",name,"Data Delete Successfuly")
        else:
            print("No such Data Name",name)  
def show(objectDict):
    
    for key,val in objectDict.items():
        print("\t\t KEY NO::",key)
##        for Name in val:
##            print("DATA OF ABOVE KEY")
        print(objectDict[key].__str__())
            
def main():
    objectDict={}
    while(True):
        print('What you Wnat TO Perform Task\n')
        print('\t\t 1 Enter Details\n 2 Change Contact \n 3 Delete The Record \n 4 Search Name Record \n 5 Quit Program')
        val=int(input(">>>>>>"))
        if val==1:
            print("-----------------BEFORE UPDATE DATA-----------------")
            show(objectDict)
            crd=1
            objectDict[crd]=ADDNewDetails()
            crd=crd+1
            print("-----------------AFTER UPDATE DATA",crd,"-----------------")
            show(objectDict)
        elif val==2:
            name=input("Enter Name")
            print('---------------------------------------------------')
            SearchName(name,objectDict)
            Change_Phone(name,objectDict)
            print("-----------------AFTER UPDATE DATA-----------------")
            print(objectDict)
        elif val==3:
            name=input('Enter Name To Delete Data Record Form List')
            print('---------------------------------------------------')
            DeleteContact(name,objectDict)
            print("-----------------AFTER UPDATE DATA-----------------")
            print(objectDict)

        elif val==4:
            name=input('Enter The Name To Search')
            print('---------------------------------------------------')
            SearchDATA(name,objectDict)
            print("-----------------AFTER UPDATE DATA-----------------")
            show(objectDict)
        else:
            break
        
    
main()   
