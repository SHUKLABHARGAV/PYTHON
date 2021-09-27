
  #                TASK-1

            #(1)reverse the string

str = "The Best Example of String"
print(str[::-1])
#  OUTPUT : gnirtS fo elpmaxE tseB ehT


            #(2)word wise reverse
str ="The Best Example of String"
ls = str.split( )
ls.reverse()
print(' '.join(ls))
#  OUTPUT : String of Example Best The

            #(3) 2 character inter change

str = "This is string example"
ls =   str.split(' ')
print(ls[0][0:2][::-1] + ls[0][2:4][::-1],  ls[1][0:2][::-1],
      ls[2][0:2][::-1] + ls[2][2:4][::-1] + ls[2][4:6][::-1],
      ls[3][0:2][::-1] + ls[3][2:4][::-1] + ls[3][4:6][::-1] + ls[3][6])

            # (4)space split          join the string with *
str= "The Best Example of String"
string= str.split( )
print("*".join(string))
# OUTPUT = The*Best*Example*of*String

str= "The Best Example of String"
print("*".join(str))
# OUTPUT =T*h*e* *B*e*s*t* *E*x*a*m*p*l*e* *o*f* *S*t*r*i*n*g

            #(5)replace is-> was
            # substring -> this==>this   is==> was
str = "this is string example"
print(str.replace(' is ', ' was '))

# OUTPUT = this was string example


n=5
k=n-1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("* ", end="")

    print("\r")
rows = int(input("Enter number of rows"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("* ",end="")
    print("\r")

