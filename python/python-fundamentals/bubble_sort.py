arr=[8,1,5,3,2,0]

def bubbleSort (arr):
	for y in range(len(arr)-1):
		for x in range(len(arr)-1-y):
			if arr[x]>arr[x+1]:
				arr[x], arr[x+1]=arr[x+1], arr[x]
	return arr						
print(bubbleSort (arr))	


def selectionSort(arr):
    for x in range(len(arr)):
        minPosition = x
        for y in range(x+1, len(arr)):
            if arr[minPosition] > arr[y]:
               minPosition = y 
        temp = arr[x]
        arr[x] = arr[minPosition]
        arr[minPosition] = temp

    return arr

print(selectionSort([5,2,1,9,0,4,6]))