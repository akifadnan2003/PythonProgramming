#Tuples are immutable, meaning they cannot be changed. They are defined using parentheses.

#Creating a simple Tuple
coordinates=(10,20)
print(f"Coordinates:{coordinates}")

#Tuples cannnot be modified but inside a tuple, we can have a list that can be modified
nested_tuple=(10,20,["apple","banana"])
nested_tuple[2].append("cherry")
print(f"Modified Tuple:{nested_tuple}")

#Tuples can be unpacked
x,y=coordinates
print(f"x:{x},y:{y}")

