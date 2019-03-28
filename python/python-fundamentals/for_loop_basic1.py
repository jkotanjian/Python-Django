# Basic - Print all the numbers/integers from 0 to 150.
for integers in range (0,151):
	print (integers)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.
for integers in range (5,1000000,5):
	print (integers)


# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".
for item in range (101):
	if item%5==0:
		print ("Coding")
	elif item%10==0:
		print ("Dojo")
	else:
		print (item)	


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.		
sum=0

for x in range (500000):
	if x%2!=0:
		sum=sum+x	

print ('Final Sum = ', sum)	
	

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).	
for integers in range (2018, 0, -4):
	print (integers)


# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines).
def flexible_countdown (lowNum, highNum, mult):
	for x in range (highNum, lowNum, (-1)):
		if x%mult==0:
			print (x)

flexible_countdown (2,9,3)


# Now, please predict the output for the following codes.

list = [3,5,1,2]
for i in list:
    print(i)

#prediction: [3,5,1,2]
#actual:
#		3
# 		5
#		1
#		2

list = [3,5,1,2]
for i in range(list):
    print(i)

#prediction: error - list is not an integer
#actual: TypeError: 'list' object cannot be interpreted as an integer

list = [3,5,1,2]
for i in range(len(list)):
    print(i)

#prediction: [0,1,2,3]
#actual: 
#		0
#		1
#		2	
#       3    