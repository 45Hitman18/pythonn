# defining a dictionary
student = {
    "name": "John",
    "age": 21,
    "major": "Computer Science"
}

# accessing values by key
print("name:", student["name"])  # output: John
print("age:", student["age"])  # output: 21

# adding a new key-value pair
student["graduation_year"] = 2025
print("updated student dictionary:", student)

# updating a value
student["age"] = 22
print("updated age:", student["age"])
