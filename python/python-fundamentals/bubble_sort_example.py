arr=[8,1,5,3,2,0]

def bubbleSort (arr):
	for y in range(len(arr)-1):
		print ("\n\n", "-"*60, "iteration", y)
		for x in range(len(arr)-1-y):
			print ("\n", "*"*80, "\ncomparing", arr[x], arr[x+1])
			if arr[x]>arr[x+1]:
				arr[x], arr[x+1]=arr[x+1], arr[x]
				print ("swapped", arr[x], arr[x+1])
				print ("array is now", arr)
			else:
				print ("no need to swap", arr[x], arr[x+1])	
bubbleSort (arr)		


arr=[8,1,5,3,2,0]

def bubbleSort (arr):
	for y in range(len(arr)-1):
		for x in range(len(arr)-1-y):
			if arr[x]>arr[x+1]:
				arr[x], arr[x+1]=arr[x+1], arr[x]
		return arr	
print (bubbleSort(arr))	


arr=[8,1,5,3,2,0]

def bubbleSort (arr):
	for y in range(len(arr)-1):
		for x in range(len(arr)-1-y):
			if arr[x]>arr[x+1]:
				arr[x], arr[x+1]=arr[x+1], arr[x]
	return arr						
print(bubbleSort (arr))		