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