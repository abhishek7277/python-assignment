with open("original_file.txt", "r") as orig_file, open("new_file.txt", "w") as new_file:
    for i, line in enumerate(orig_file):
	if i != 4:
	     new_file.write(line)
