'''user will input no of rows
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
'''
n=5
for i in range(0,n):
    for j in range(0, i + 1):
        print("1", end=" ")
    print("\r")

num=1
n=4
for i in range(0,n):
    for j in range(0, i + 1):
        print(num ,end=" ")
        num= num + 1
    print("\r")

'''
Enter number of rows4
* * * * 
* * * 
* * 
* 
'''

rows = int(input("Enter number of rows"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print("\r")


'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

n=5
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ", end="")

    print("\r")


#user will input number
#factorial program -> while loop'''

num = int(input("enter a number: "))

fac = 1

while num > 0:
    fac = fac * num
    num = num - 1

print("factorial is: ", fac)

# OUTPUT    enter a number: 4     factorial is: 24
