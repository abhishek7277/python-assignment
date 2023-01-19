def check_first_last(lst):
   if len(lst) >= 1:
	return lst[0] == lst[-1]
   return False

numbers = [1, 2, 3, 4, 1]
result = check_first_last(numbers)
print(result) # True
