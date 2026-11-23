#Question 12: Butterfly Pattern
for i in range(1,6):#loop run 5 times to print 5 rows
    for j in range(1,i+1):#loop prints stars in each row
        print("*",end = " ")
    for k in range(1,2*(5-i)+1):#loop prints spaces
        print(" ",end = " ")
    for l in range(1,i+1):#loop prints stars on the right side of butterfly
        print("*",end = " ")
    print()
for i in range(5-1,0,-1):#loops runs from 4 to 1 to print stars in downward 
    for j in range(1,i+1):#print stars in decreasing order in each row
        print("*",end=" ")
    for j in range(1,2*(5-i)+1):#prints spaces
        print(" ",end = " ")
    for l in range(1,i+1):
        print("*",end = " ")
    print()

