class Underscore:
    def map(self, list, num):
        double=[]
        for x in list:
        	double.append(num(x))
        return double	

    def find(self, list, num): 
	    greater_than=[]
	    for x in list:
		    if x>4:
			    greater_than=x
			    return greater_than

    def filter (self, list, num):
    	evens=[]
    	for x in list:
    		if x%2==0:
    			evens.append(x)
    	return evens

    def reject(self, list, num):
    	odds=[]
    	for x in list:
    		if x%2!=0:
    			odds.append(x)
    	return odds		

_=Underscore()         

double=_.map([1,2,3], lambda x: x*2) 
print(double)
greater_than=_.find([1,2,3,4,5,6], lambda x: x>4)
print (greater_than)		
evens=_.filter([1,2,3,4,5,6], lambda x: x%2==0)
print (evens)	    
odds=_.reject([1,2,3,4,5,6], lambda x: x%2!=0)
print (odds)