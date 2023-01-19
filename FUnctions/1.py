def outer_function(a, b):
   def inner_function():
       return a + b
    return inner_function() + 5

result = outer_function(2, 3)
print(result)
