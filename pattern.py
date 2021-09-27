#PROGRAM TO PRINT HALF PYRAMID USING *
rows= int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end=" ")
    print("\r")

'''     OUTPUT  
                Enter number of rows: 4
                *  
                *  *  
                *  *  *  
                *  *  *  *  
'''

#PROGRAM TO PRINT HALF PYRAMID USING NUMBERS
rows= int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\r")
'''
        OUTPUT  
                Enter number of rows: 4
                1 
                1 2 
                1 2 3 
                1 2 3 4 
'''

#PROGRAM TO PRINT HALF PYRAMID USING ALPHABATES
rows= int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabate = chr(ascii_value)
        print(alphabate, end=" ")

    ascii_value += 1
    print("\r")

'''
            OUTPUT 
                    Enter number of rows: 4
                    A 
                    B B 
                    C C C 
                    D D D D 

'''

#INVERTED HALF PYRAMID USING *
rows= int(input("Enter number of rows: "))

for i in range(rows,0,-1):
    for j in range(0,i):
        print("* ", end=" ")

    print("\r")

'''
                OUTPUT
                        Enter number of rows: 4
                        *  *  *  *  
                        *  *  *  
                        *  *  
                        *  

'''
#INVERTED HALF PYRAMID USING NUMBERS
rows= int(input("Enter number of rows: "))

for i in range(rows,0,-1):
    for j in range(1, i+1):
        print(j, end=" ")

    print("\r")
'''
                OUTPUT
                        Enter number of rows: 4
                        1 2 3 4 
                        1 2 3 
                        1 2 
                        1 

'''
#program to print full pyramid using*
rows= int(input("Enter number of rows: "))
k=0


for i in range(1, rows+1):
    for j in range(1, (rows-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("*", end="")
        k += 1

    k = 0
    print()
'''         OUTPUT 
                    Enter number of rows: 4
                       *
                      ***
                     *****
                    *******
'''


# inverted pyramid using *
rows= int(input("Enter number of rows"))

for i in range (rows, 1,-1):
    for space in range (0, rows-i):
        print(" ", end=" ")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

''' OUTPUT
                Enter number of rows5
                    * * * * * * * 
                      * * * * * 
                        * * * 
                          * 
'''
