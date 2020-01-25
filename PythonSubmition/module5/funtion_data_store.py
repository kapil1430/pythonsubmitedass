ds={'office1':{'medical':[{'roomNumber':100,'use':'reception','sqft':50,'price':75},
                         {'roomNumber':101,'use':'waiting','sqft':250,'price':75},
                         {'roomNumber':102,'use':'examination','sqft':125,'price':150},
                         {'roomNumber':103,'use':'examination','sqft':125,'price':150},
                         {'roomNumber':104,'use':'office','sqft':150,'price':100}
                         ],
              'parking':{'location':'premium','style':'covered','price':750}
              }
    }
#funtion find all the DataId Keys have within them like office have medical and parking keys
def FindKey():
    for D_id,Dval in ds.items():
        print(D_id)
        for val in Dval.keys():
            print(val)
#create A New Office and develop them
def CreateNewOffice():
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
    print(ds)    
CreateNewOffice()

def addRoom():
    print("Enter New Room In office Medical Block")
    rno=input("Enter Room NUmber")
    use=input('Enter For USwe')

