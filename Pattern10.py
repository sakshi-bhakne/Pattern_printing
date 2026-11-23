#Question 10: Hollow Square
for i in range(1,6):#loop run to print stars in row
    for j in range(1,6):#loop runs to prints stars in coloumn
        if i == 1 or i == 5 or j == 1 or j == 5:
            print("*",end =" ")
        else:
            print(" ",end=" ")
    print()