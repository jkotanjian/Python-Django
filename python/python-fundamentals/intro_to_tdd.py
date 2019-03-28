import unittest

def reverseArray (list):
	list.reverse()
	print (list)
	return (list)

reverseArray ([1,2,3,4])

def reverse (str):
  return str [::-1]

def isPalindrome (str):
	palindrome=reverse(str)
	if (str==palindrome):
		return True
	return False	

z=isPalindrome ("car")
print (z)

def coin (num):
    amount=num
    leftover=num

    numq=(amount/25)
    leftover=(amount-(round(numq)*25))
    numd=(leftover/10)
    leftover=(leftover-(round(numd)*10))
    numn=(leftover/5)
    if numn<5:
      numn=0
    leftover=(leftover-(round(numn)*5))
    nump=(leftover/1)
    leftover=(leftover-(round(nump)*1))
    return [round(numq), round(numd), round(numn), round(nump)]    

print (coin(87))

def factorial (num):
	if (num==1):
		return num
	else:	
		return (num*factorial(num-1))

z=factorial(5)
print (z)

def fibonacci (num):
	if (num<=1):
		return num	
	else: 
		return (fibonacci(num-1)+fibonacci(num-2))
	
z=fibonacci(7)
print (z)

class reverseArrayTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseArray([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseArray([2,4,-3]), [-3,4,2])
class isPalindromeTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
       return self.assertEqual(isPalindrome("rabbit"), False)
class coinsTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(coin(87), [3,1,0,2])
    def test2(self):
       return self.assertEqual(coin(53), [2,0,0,3])   
class factorialTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(factorial(5), 120)
    def test2(self):
       return self.assertEqual(factorial(3), 6)       
class fibonacciTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(fibonacci(3), 2)
    def test2(self):
       return self.assertEqual(fibonacci(7), 13)   


    def setUp(self):
        print("running setUp")

    def tearDown(self):
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()          

# reverseList - Write a function that reverses the values in the list (without creating a temporary array).  For example, reverseList([1,3,5]) should return [5,3,1].  In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  Create at least 3 other test cases before you implement the functionality.
def reverseArray (list):
	reverse(list)
	print (list)

reverseArray ([1,2,3,4])

# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).  For example, isPalindrome("racecar") should return true.  Another way to say this is assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar")).  Similarly, assertFalse( isPalindrome("rabcr") ).  Add at least 5 other test cases before you implement the functionality.  Remember that you need to write the tests first, make sure the tests fail, and then write the functionality within the function, to now make all the tests pass.  (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').
def isPalindrome (str):
	reverse(str)
	return str[::-1]
	palindrome=reverse(str)
		if (str==palindrome):
			return True
		return False	

z=isPalindrome ("racecar")
print (z)

# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.  For example, if you need to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel and 2 pennies.  If you need to give the customer 92 cents, you can give 3 quarters, 1 dime, 1 nickel, and 2 pennies.  Write the function such that for example, coin(87) returns [3,1,0,2].  coin(92) should return [3,1,1,2].  Add at least 5 other test cases first, before you fill in the codes inside function coin().
def coin (num):
    amount=num
    leftover=num

    numq=(amount/25)
    leftover=(amount-(round(numq)*25))
    numd=(leftover/10)
    leftover=(leftover-(round(numd)*10))
    numn=(leftover/5)
    if numn<5:
        numn=0
    leftover=(leftover-(round(numn)*5))
    nump=(leftover/1)
    leftover=(leftover-(round(nump)*1))
    return [round(numq), round(numd), round(numn), round(nump)]     
print (coin(87))

# Factorial (hacker challenge).  Write a function factorial() that returns the factorial of the given number.  For example, factorial(5) should return 120.  Do this using recursion; remember that factorial(n) = n * factorial(n-1).
def factorial (num):
	if (num==1):
		return num
	else:	
		return (num*factorial(num-1))

z=factorial(5)
print (z)

# Fib (hacker challenge). Write a function fib() in Python that returns the appropriate Fibonacci number.  Do this using recursion.  Let's say that the first two Fibonacci numbers are 0 and 1.  Remember that fib(n) = fib(n-2) + fib(n-1).
def fibonacci (num):
	if (num<=1):
		return num	
	else: 
		return (fibonacci(num-1)+fibonacci(num-2))
	
z=fibonacci(7)
print (z)