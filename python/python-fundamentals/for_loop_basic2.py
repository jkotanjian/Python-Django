# Biggie Size - Given an array, write a function that changes all positive numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def biggieSize (list):
	x=0
	for integers in list:
	    if list[x]<0:
	  	    print ("Big")
	    if list[x]>0:
	        print (list[x])
	    x=x+1
			
biggieSize ([-1,3,5,-5])


# Count Positives - Given an array of numbers, create a function to replace last value with number of positive values. Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to be a positive number).
def countPositives (list):
	sum=0
  	for x in range (len(list)):
		if list[x]>0:
	    	sum=sum+1
	  	list[-1]=sum  
	print (list)

countPositives ([-1,1,1,1])	
		

# SumTotal - Create a function that takes an array as an argument and returns the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumTotal (list):
	print (sum(list))

sumTotal ([1,2,3,4])		


# Average - Create a function that takes an array as an argument and returns the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def sumAverage (list):
	print (sum(list)/len(list))

sumAverage ([1,2,3,4])	

# Length - Create a function that takes an array as an argument and returns the length of the array.  For example length([1,2,3,4]) should return 4
def returnLength (list):
	print (len(list))

returnLength ([1,2,3,4])


# Minimum - Create a function that takes an array as an argument and returns the minimum value in the array.  If the passed array is empty, have the function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def returnMin (list):
	if len(list)<1:
		return ("false")
	else:	
	  print (min(list))

returnMin ([1,2,3,4])	
returnMin ([-1,-2,-3])
returnMin ([])


# Maximum - Create a function that takes an array as an argument and returns the maximum value in the array.  If the passed array is empty, have the function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.
def returnMax (list):
	if len(list)<1:
		return ("false")
	else:
		print (max(list))

returnMax ([1,2,3,4])
returnMax ([-1,-2,-3])	
returnMax ([])		

# UltimateAnalyze - Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateAnalyze (list):
	dict = {
		"sumTotal": sum(list),
		"average": sum(list)/len(list),
		"minimum": min(list), 
		"maximum": max(list),
		"length": len(list)
		}	
	print (dict)

ultimateAnalyze ([1,2,3,4])


# ReverseList - Create a function that takes an array as an argument and return an array in a reversed order.  Do this without creating an empty temporary array.  For example reverse([1,2,3,4]) should return [4,3,2,1]. This challenge is known to appear during basic technical interviews.
def reverseArray (list):
	list.reverse()
	print (list)

reverseArray ([1,2,3,4])	