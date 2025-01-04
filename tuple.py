# tuple: immutable (cannot be changed)
colors = ("red", "green", "blue")
# colors[1] = "yellow"  # this will raise an error
print("tuple:", colors)

animals = ("cat", "dog", "bird")
print("length of tuple:", len(animals))# show length 

numbers = (10, 20, 30, 40, 50)
print("slice:", numbers[1:4])  # slicing from index 1 to 3