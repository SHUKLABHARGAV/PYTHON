
#                TASK-2

""" 1) user input a character
	a->"you have enter a"
	b->"you have enter b"
	c->"you have enter c"
	->Invalid character
"""
#    Solution:
x = input("Enter a character : ")
#'a' <= x <='z':
if x =='a' :
    print(" you have enter ",(x))
elif x == 'b':
    print(" you have enter ",(x))
elif x == 'c':
    print(" you have enter ",(x))
else :
    print("Invalid Character",(x))

# OUTPUT     Enter a character : b
#            you have enter  b



'''2)user input a number
	positive number
		odd number
			perform addition with an integer constant

		even number
			perform multiplication with an floating point constant

	negative number
		odd number
			perform subtraction with an integer constant

		even number
			perform division with an floating point constant
'''
# Solution

x= int (input("Enter any number : "))

if x>0 :
    if x % 2 != 0 :
        print("You have entered positive odd number",x + 5)
    if x>0 :
        if x % 2 == 0 :
            print("You have entered positive even number",x * 2.3)
if x<0 :
    if x % 2 != 0 :
        print("You have entered Negative odd number",x - 5)
    if x<0 :
        if x % 2 == 0 :
            print("You have entered Negative even number",x / 2.3)

# OUTPUT      Enter any number : 6
#             You have entered positive even number 13.799999999999999


'''3)user input marks

	90 to 100->A grade

	80 to 90->B grade

	60 to 80->C grade

	40 to 60->D grade

	< 40     ->Fail

	>100 	->Invalid Marks
'''

#solution

x= int(input("Enter your Marks : "))

if 90 <= x <= 100 :
    print("You Scored A Grade.")
if 80 <= x <= 90 :
    print("You Scored B Grade.")
if 60 <= x <= 80:
        print("You Scored C Grade.")
if 40 <= x <= 60:
        print("You Scored D Grade.")
if 40 < x <= 0:
        print("Sorry You can't clear the exam.")
else :
    print ("Invalid Marks")

# OUTPUT    Enter your Marks : 67
#           You Scored C Grade.

