#Question 11: Hollow Right-Angled Triangle
for i in range(1,6):
    for j in range(1,i + 1):
        if i == 5 or j == i or j == 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()