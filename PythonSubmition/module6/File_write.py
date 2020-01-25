def writeToFile():
    #file handling implementation to write a data in files
    fopen=open('Writing_F1.txt','w')
    fopen.write('HEllo World Mr Python USer its a file Handling COncept to Write'+'\n to TO writing The Data uisng Python'+'\n')
    fopen.write("This Is Kapil Sharma Write Data to File")
    fopen.close()
    print('successfully writing done ..... Thanks Come Again')
def ReadFromFile():
    #implement the data read from file using python
    fopen=open('Writing_F1.txt','r')
    print(fopen.read())
    fopen.close()
    print('success fully Read done...')
def ReadFromLine():
    fopen=open('Writing_F1.txt','r')
    line=fopen.readline()
    while line!='':
        #amount=float(line)
        print(line)
        line=fopen.readline()
        
    fopen.close()
    print('success fully Read done...')

