#Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed.

student={"name":"Akif","age":21,"major":"Computer Engineering"}
print(f"Dictionary:{student}")

#Changing/Updating an element in the dictionary

student["age"]=22
print(f"After changing age:{student}")

#Checking a key in the dictionary
if "name" in student:
    print(f"Name:{student['name']}")

#Dictionary  can be looped
for key in student:
    print(f"{key}:{student[key]}")


#A dictionary that hold student information

students={
    101:{"name":"Akif","grades":(90,90,95),"courses":{"Game Programming","Data Structures"}},
    102:{"name":"Ali","grades":(80,85,90),"courses":{"Game Programming","Algorithms"}}
}

#Calculating average grades of 101

avg_grade=sum(students[101]["grades"])/len(students[101]["grades"])
print(f"Average grade of 101:{avg_grade}")

#Checking for common lesson between 101 and 102

common_courses=students[101]["courses"].intersection(students[102]["courses"])
print(f"Common courses:{common_courses}")