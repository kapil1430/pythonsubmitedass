import pickle
pb={'name':'Kapil','Age':21,'phone':7389370811,'Study':'Btech IT'}
def writingPickel():
    fo=open('PickleFile_f1.dat','wb')
    pickle.dump(pb,fo)
    fo.close()
    print("Complete....")

def readFromPickle():
    fo=open('PickleFile_f1.dat','rb')
    pb=pickle.load(fo)
    print(pb)
    fo.close()
    print("Complete....")
#writingPickel()
readFromPickle()
