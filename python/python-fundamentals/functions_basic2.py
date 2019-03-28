#Countdown - Create a function that accepts a number as an input.  Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).  For example countDown(5) should return [5,4,3,2,1,0].
def countDown (x):
	for integers in range (x,-1,-1):
		print (integers)

countDown (5)


#Print and Return - Your function will receive a list with two numbers. Print the first value, and return the second.
def printReturn (x,y):
	print (x)
		return (y)

printReturn (1,2)	


#First Plus Length - Given a list, return the sum of the first value in the list, plus the list's length.
def firstPlus (list):
	print (len(list)+list[0])
	
firstPlus ([1,2,3,4,5])	


#Values Greater than Second - Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.  Print how many values this is.  If the list is only one element long, have the function return False
def greaterThan (list):
	x=0
  	count=0

  	for integers in list:
		if len(list)<2:
			print ("False")
	  	if list[x]>list[1]:
			print (list[x])
		  	count=count+1
		x=x+1
  	print (count)

greaterThan ([11,10,2,12])		
			

#This Length, That Value - Write a function called lengthAndValue which accepts two parameters, size, and value. This function should take two numbers and return a list of length size containing only the number in value. For example, lengthAndValue(4,7) should return [7,7,7,7].
def lengthAndValue (x,y):

	for x in range(x):
		print (y)

lengthAndValue (4,7)