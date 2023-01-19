def create_new_list(list1, list2):
   new_list = []
   for num in list1:
       if num % 2 != 0:
	 new_list.append(num)
   for num in list2:
        if num % 2 == 0:
	 new_list.append(num)
   return new_list
