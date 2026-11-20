#Question 6: Right-Aligned Triangle
for i in range(1,6):#loop runs 5 times
    for j in range(5-i):#prints spaces before printing star
        print(" ",end = " ")
    for k in range(1,i+1):#prints star
        print("*",end = " ")
    print()#move to next line after printing a pattern in each row