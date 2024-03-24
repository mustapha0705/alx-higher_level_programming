#!/usr/bin/python3
def max_integer(my_list=[]):
	if len(my_list) == 0:
		return None

	max_num = my_list[0]
	for element in my_list:
		if element > max_num:
			max_num = element
	return max_num
