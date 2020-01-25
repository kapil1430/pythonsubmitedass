n=5
for i in range(1,11):
    if i>=1 and i<=5:
        print("*"*n)
    n=n-1
    if i>=6 and i<=10:
        print("*"*(i%5))
    print()
