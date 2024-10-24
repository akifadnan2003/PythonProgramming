#Sets are unordered collections of unique elements. We can construct them by using the set() function. Let's go ahead and create a set to see how it works.

#Creating a simple set

numbers={1,2,3,4,5}
print(f"Set:{numbers}")

#Adding an element to the set
numbers.add(6)
print(f"After adding 6;{numbers}")

#Removing an element from the set
numbers.remove(2)
print(f"After removing 2: {numbers}")

#Intersection and union of two sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
intersection=set1.intersection(set2)
print(f"Intersection:{intersection}")
union=set1.union(set2)
print(f"Union:{union}")