"""

  Write a function that takes in an array of unique integers and returns its
  powerset.

  input = [1,2,3]
  output = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

"""
def powerset(array, index):
	if index is None:
		index = len(array) - 1
	
	if index < 0:
		return [[]]
	
	current_element = array[index]
	sub_set = powerset(array, index - 1)
	
	for num_index in range(len(sub_set)):
		current = sub_set[num_index]
		sub_set.append(current + [current_element])
	return sub_set

powerset([1,2,3], None)