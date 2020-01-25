import pickle

def DumpToFile():
    try:
        fo=open('DataStoreDicdata.txt','wb')
        pickle.dump(ds,fo)
    except exception as e:
        print(e)
    finally:
        fo.close()
        print('Completed... Dump File')
def showData():
    fo=open('DataStoreDicdata.txt','rb')
    ds=pickle.load(fo)
    for company,company_val in ds.items():
        print ("...........................")
        print("            ",company,"            ")
        print ("...........................")
        for office,office_val in company_val.items():
            print(office,"---------------")
            for rooms_list in office_val:
                for attr,val in rooms_list.items():
                    print (attr,":",val,end="    ||")
                print()
    fo.close()
    
    
#funtion find all the DataId Keys have within them like office have medical and parking keys
def FindKey():
    for D_id,Dval in ds.items():
        print(D_id)
        for val in Dval.keys():
            print(val)
#create A New Office and develop them
def CreateNewOffice():
    fo=open('DataStoreDicdata.txt','wb')
    ds=pickle.load(fo)

    ofname=input("Enter The New Office Block")
    ds[ofname]={}
    while(True):
        print("create YOur New Office block")
        ##    for i in range(n):
        dep1=input('Enter')
        ds[ofname][dep1]={}
##    for ke,va in ds.item():
        
        k=int(input('How many keys and values in your in your block')) 
        print('Data key and values of ',ds[ofname][dep1])
        for j in range(k):
            key=input('Enter key in office DeptBlock')
            val=input('Enter val in office DeptBlock')
            ds[ofname][dep1][key]=val
        print("Do you wnat to put more block")
        vl=input("YES/NO")
        if vl=='NO':
            break
    fo.close()
    wfo=open('DataStoreDicdata.txt','wb')
    pickle.dump(ds,wfo)
    wfo.close()
    print('New Office Created....AFTER')
    showData()
    
def change_roomTOMedical():
        fo=open('DataStoreDicdata.txt','rb')
        ds=pickle.load(fo)

        operation=False
        old=int(input("Enter the room no to be changed: "));
        new=int(input("Enter the new room no: "));
        for i in range(0,len(ds["office1"]["medical"])):
            if(ds["office1"]["medical"][i]["roomNumber"]==old):
                ds["office1"]["medical"][i]["roomNumber"]=new
                operation=True
                break;
        if(operation): print("changed Successfully----------------")
        else:print("Can not find this room-----------")

        fo.close()
        wfo=open('DataStoreDicdata.txt','wb')
        pickle.dump(ds,wfo)
        wfo.close()
    
        print("Final Change Room Dumped....AFTER")
        print(ds)

def addroomTOMedical():
    fo=open('DataStoreDicdata.txt','rb')
    ds=pickle.load(fo)
    fo.close()

    company=input("Enter the name of company: ")
    building=input("Enter the building name of the company: ")
    room_no=int(input("Enter the room_no to add to this building: "))
    use=input("Enter the use of this room: ")
    sq_ft=int(input("Enter the sq-ft of this room: "))
    price=int(input("Enter the price of this room: "))
    ds[company][building].append({"roomNumber":room_no,"use":use,"sq-ft":sq_ft,"price":price})
    
    wfo=open('DataStoreDicdata.txt','wb')
    pickle.dump(ds,wfo)
    wfo.close()
    print("ADD ROOM DUMPED SUCCESS ....AFTER")
    print(ds)
addroomTOMedical()
