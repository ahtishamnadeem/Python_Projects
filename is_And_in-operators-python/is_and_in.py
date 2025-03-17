#About "is" & "in" operators

  #is operator | Checks if two variables refer to the same object in memory.
a = [1, 2, 3]  
b = a  
c = [1, 2, 3]  

print(a is b)  # True (Same object)  
print(a is c)  # False (Different objects with same values)  

   #in operator | Checks if a value exists within an iterable (e.g., list, tuple, string).
numbers = [1, 2, 3, 4, 5]  
print(3 in numbers)  # True (3 exists in the list)  
print(6 in numbers)  # False (6 is not in the list)  



