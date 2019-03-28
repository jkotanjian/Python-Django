class Node:
    def __init__(self, value):
        self.value=value
        self.next=None
            
class SList:
    def __init__(self, value):
        node=Node(value)
        self.head=node
    
    def addNode(self, value):
        node=Node(value)
        runner=self.head
        while(runner.next!=None):
            runner=runner.next
        runner.next=node
        return self

    def printAllValues(self, msg=""):
        runner = self.head         
        print("Head points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))  

    def removeNode(self, value):
        runner=self.head
        if self.head.value==value:
            temp=self.head.next
            del self.head
            self.head=temp
        else: 
            runner=self.head
            while runner.next.value!=value:
                runner=runner.next     

            temp=runner.next.next
            del runner.next
            runner.next=temp  
            return self                       

              
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues()

list.removeNode(9)
list.removeNode(5)
list.removeNode(1)

list.printAllValues()

# Assignment
# Part 1 - recreate SList and Node.  
# Recreate addNode and printAllValues methods.

# Part 2 - implement removeNode(val)

# Implement removeNode(val) where it removes a node with the value val.  For example list.removeNode(5) will see if there's a node with the value of 5.  If it is, it will remove that from the linked list.  When you do this, you'll need to consider the following cases:
# when the node you want to remove is in the beginning of the linked list
# when the node you want to remove is in the middle of the linked list
# when the node you want to remove is at the end of the linked list
# For each of these cases, you will probably need to have different logics to handle the removal.

# list.removeNode(9) # removes 9, which is one of the middle nodes in the list
# list.removeNode(5) # removes 5, which is the first value in the list
# list.removeNode(1) # removes 1, which is the last node in the list
# list.printAllValues("Attempt 1")
class SLNode:
	def __init__(self, value):
	   	self.value=value
		self.next=None

a=Node(5)		

class Node:
	def __init__(self, value):
		self.value=value
		self.next=None
class SList:
	def __init__(self, value):
		node=Node(value)
		self.head=node

slist=SList(7)	

	def __init__(self, value):
		node=Node(value)
		self.head=node
   
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))


	def addNode (self, value):
		node=Node(value)
		runner=self.head
		while (runner.next!=None):
			runner=runner.next
		runner.next=node	 		

   def removeNode(self, value):
    	runner=self.head
    	while runner:
    		if (runner.getData()==Node(value)):
    			 True
    		runner=crunner.getNextNode()
    	return False	

      
	def printAllValues(self):
		runner=self.head
		while (runner.next!=None):
			print (runner.value)
			runner=runner.next	    		



			    def removeNode(self, value):
        runner=self.head
        if self.head.value==value:
            print (self.head.next.value)
            temp=self.head.next.next
            del self.head.next
            self.head.next=temp
        else: 
            runner=self.head
            while runner.next.value!=value:
                runner=runner.next 
                if runner.next.value==value:
                    print (runner.next.value)
                    temp=runner.next.next
                    del runner.next
                    runner.next=temp
                    print (value)    
                    return self 