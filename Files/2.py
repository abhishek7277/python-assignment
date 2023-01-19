import os

file_path = "example.txt"

if os.path.getsize(file_path) == 0:
   print("The file is empty.")
else:
   print("The file is not empty.")
