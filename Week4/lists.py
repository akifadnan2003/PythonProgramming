#Lists are mutable, meaning they can be changed after they are created.
#They can hold all types od data including other lists

#Creating a simple List

fruits=["apple","banana","cherry"] 
print(f"Fruits:{fruits}") 

#Adding an element to the list
fruits.append("orange")
print("Appending Orange....")
print(f"After append:{fruits}")

#Removing an element from a certain index of the list
fruits[1]="blueberry"
print(f"After change:{fruits}")

#Reversing a llst
fruits.reverse()
print("Reversing the list....")
print(f"Reversed:{fruits}")

#Removing an element from the list
fruits.remove("apple")
print("Removing apple....")
print(f"After removing apple:{fruits}")