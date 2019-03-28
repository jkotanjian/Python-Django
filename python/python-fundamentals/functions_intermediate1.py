# Functions Intermediate I

# Create beCheerful().  Within it, print string "good morning!" 98 times.
def beCheerful (name='', repeat=98):
	print (f"Good morning {name}\n"*repeat)

beCheerful()
beCheerful(name="john")
beCheerful(name="michael", repeat=5)
beCheerful(repeat=5, name="kb")
beCheerful(name="aa")


# As part of this assignment, please create a function randInt() where:
# randInt() returns a random integer between 0 to 100

def randInt():
    from random import random
    print (int(random()*100))
    
randInt()

def randInt():
    from random import uniform
    print (int(uniform(0,100)))

randInt()

def randInt():
	from random import randint
	print (randint(0,100))

randInt()


# randInt(max=50) returns a random integer between 0 to 50
def randInt():
	from random import random
	print (int(random()*50))

randInt()	

def randInt():
    from random import uniform
    print (int(uniform(0,50)))

randInt()

def randInt ():
	from random import randint
	print (randint(0,50))

randInt ()	


# randInt(min=50) returns a random integer between 50 to 100
def randInt():
    from random import randrange
    print (randrange(50, 100))

randInt()

def randInt():
    from random import uniform
    print (int(uniform(50,100)))

randInt()

def randInt ():
	from random import randint
	print (randint(50,101))

randInt ()


# randInt(min=50, max=500) returns a random integer between 50 and 500
def randInt():
    from random import randrange
    print (randrange(50, 500))

randInt()

def randInt():
    from random import uniform
    print (int(uniform(50,500)))

randInt()

def randInt ():
	from random import randint
	print (randint(50,501))

randInt ()