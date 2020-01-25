#Name Pattern value Matrix list
k=[[1,0,0,1,0],[1,0,1,0,0],[1,1,0,0,0],[1,0,1,0,0],[1,0,0,1,0]]
a=[[0,1,1,1,0],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]]
p=[[1,1,1,1,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,0],[1,0,0,0,0]]
Is=[[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]]
l=[[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]]
for i in range(0,5):
    for j in range(0,5):
        if k[i][j]==1:
            print("*",end="")
        else:
            print(" ",end="")

    for s in range(0,5):
        if a[i][j]==1:
            print("@",end="")
        else:
            print(" ",end="")

    for t in range(0,5):
        if p[i][j]==1:
            print("#",end="")
        else:
            print(" ",end="")

    for t in range(0,5):
        if Is[i][j]==1:
            print("&",end="")
        else:
            print(" ",end="")

    for v in range(0,5):
        if l[i][j]==1:
            print("!",end="")
        else:
            print(" ",end="")

    print()
