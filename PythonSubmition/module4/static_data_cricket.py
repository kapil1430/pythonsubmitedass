#import pandas as pd
s={1:{'MsDhoni':{'TypeP':'Wk (c)','Matches':100,'Runs':10000,'Average':59.8,'HeighestS':185},
        'ViratK':{'TypeP':'RightHandB (vc)','Matches':85,'Runs':20000,'Average':70.8,'HeighestS':300},
        'Rohit':{'TypeP':'RightHandB','Matches':100,'Runs':10000,'Average':59.8,'HeighestS':200},
        'Yuviraj':{'TypeP':'LeftHandB','Matches':100,'Runs':10000,'Average':59.8,'HeighestS':150}
        }
        }
#df=pd.DataFrame(Sqd[1])
#print(df)
li=[]
mmax=0
for p_id,P_name in s.items():
    #print("Persion Id",p_id)
    for key in P_name.keys():
##        #print(key)
##        li.append(s[p_id][key]['HeighestS'])
##        li.append(key)
        if s[p_id][key]['HeighestS']>mmax:
            mmax=s[p_id][key]['HeighestS']
            name=key
        
        
print("Name::"+name,"HS::",+mmax)
