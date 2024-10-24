#String is an immutable data type that is used to store text data

#Creating a simple string
greeting="Hello World"
print(greeting)

#Checking the length of the string
x=len(greeting)
print(f"The length of the string 'greeting' is {x}")

#Accessing a word in the string
print(greeting.find("World"))

#Spllitting the string
words=greeting.split()
print(f"Split worlds:{words}")