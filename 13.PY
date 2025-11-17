Creating a dictionary student = {
 "name": "John", "age": 21,
 "course": "Computer Science"
 }
 Displaying the dictionary print("Student Dictionary:", student)
 Accessing values using keys print("Name:", student["name"])
 print("Age:", student["age"])
 Adding a new key-value pair student["grade"] = "A"
 print("After adding 'grade':", student)
 Updating a value student["age"] = 22
 print("After updating age:", student)
 Removing a key-value pair del student["course"]
 print("After removing 'course':", student)
 Iterating through dictionary print("Dictionary Items:")
 for key, value in student.items(): print(key, ":", value)
