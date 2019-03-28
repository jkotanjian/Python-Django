class mathDojo:
	def __init__(self, list):
		self.result=0
		print (self.result)

	def add (list):
		sum=sum(list)
		print (sum)
		return self
	
	def subtract (list):
		self.result=sum(self.args)
		self.result=add()-sum(self.args)
		print (self.result)
		return self

md=mathDojo()		
x=md.add(2).add(2,5,1).subtract(3,2).result()

# HINT: To do this exercise, you will probably have to use 'return self'. If the method returns itself (an instance of itself), we can chain methods.

# Create a Python class called MathDojo that has the methods add and subtract. Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. It should be able to do the following task:

# x = md.add(2).add(2,5,1).subtract(3,2).result()
# print(x) # should print 5
# which should perform 0+2+(2+5+1)-(3+2) and print 5.