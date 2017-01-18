def find_max_min(list):
	#Function Declaration
    my_list=[]
    # Empty list to hold the output
    mn=min(list)
    mx=max(list)
    if max(list)== min(list):
        my_list.append(len(list))
	'''
	Returns the number of elements in the list
	in a new list if the `min` and `max` are equal
	'''
    else:
        my_list.append(mn)
        my_list.append(mx)
    return my_list
