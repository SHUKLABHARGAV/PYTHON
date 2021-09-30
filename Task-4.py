n=int(input("Enter Number of Rows"))

for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for j in range(i):
        print('*', end='')
    for j in range(i+1):
        print('*', end='')
    print()


for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*', end='')
    for j in range(i,n):
        print('*', end='')
    print()

''' OUTPUT 
                        Enter Number of Rows5
                             *
                            ***
                           *****
                          *******
                         *********
                          *******
                           *****
                            ***
                             *
                        '''


ls = [1, 2, 3, ['a', 'b', 'c'], 4, 5.02, 6.33, ['d', 'e', 'f'], 7, 'g', 8, 'h', [9, 10, 'i', 'j'],11,'aansh']

for i in ls:
    if type(i) == list:

        for j in i:

            if type(j) == str:
                print("\t",j)

            else:
                print(j)

    else:
        if type(i) == str:
            print("\t",i)
        else:
            print(i)

'''OUTPUT
                    1
                    2
                    3
                         a
                         b
                         c
                    4
                    5.02
                    6.33
                         d
                         e
                         f
                    7
                         g
                    8
                         h
                    9
                    10
                         i
                         j
                    11
                         aansh
''''
