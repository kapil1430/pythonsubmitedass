#nested compresion for list 1 st way to create a nestef list within list same output
matrix=[]
d=1
for i in range(5):
    matrix.append([])
    for j in range(5):
        matrix[i].append(d)
        d+=1
print(matrix)
print()
#nested compresion for list 2nd way to create a nestef list within list same output
matrix=[[d for j in range(5)]for i in range(5)]
print(matrix)

#flatternd the 2 D list flat
flatm=[]
for sublist in matrix:
    for val in sublist:
        flatm.append(val)
print(flatm)

#flattern the list  using direct
fmatrix=[value for sublist in flatm for value in sublist if value<6]
print(fmatrix)
