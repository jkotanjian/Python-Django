def insertion_sort (sorted_list):

   for i in range(1, len(sorted_list)):
		x=sorted_list[i]
    	slot=i
	    while slot>0 and sorted_list[slot-1]>x:
         sorted_list[slot]=sorted_list[slot-1]
         slot=slot-1

     sorted_list[position]=x

insertion_sort(sorted_list)

sorted_list=[54,26,93,17,77,31,44,55,20]
print(sorted_list)


def insertion_sort(list):

    for i in range (1,len (list)):
        value = list[i]
        position = i
        while position > 0 and list[position-1] > value:
         list[position]=list[position-1]
         position = position-1

    list[position]=value

insertion_sort(list)

list = [54,26,93,17,77,31,44,55,20]
print(list)


def insertion_sort(sort_list):

    for i in range (1,len (sort_list)):
        value = sort_list[i]
        position = i
        if value < sort_list[position-1]
            sort_list[position]=sort_list[position-1]
         position = position+1

    sort_list[position]=value

sort_list = [54,26,93,17,77,31,44,55,20]
insertion_sort(sort_list)
print(sort_list)


def insertion_sort(sort_list):

    for i in range (1,len (sort_list)):
        value = sort_list[i]
        position = i
        while position > 0 and sort_list[position-1] > value:
         sort_list[position]=sort_list[position-1]
         position = position-1

    sort_list[position]=value

sort_list = [54,26,93,17,77,31,44,55,20]
insertion_sort(sort_list)
print(sort_list)