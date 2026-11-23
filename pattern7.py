#Question 7: Star Pyramid
for i in range(1,6):#loop runs 5 times
    for j in range(5-i):#print spaces before star.
        print("_",end = " ")#space in same line where star is printed, end to print space in same libe
    for k in range(2*i-1):#print star in increasing order 
        print("*",end = " ")#print star
    print()#moves to next lines after printing pattern in each line