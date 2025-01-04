# set: unordered, no duplicate values
numbers = {1, 2, 3, 4, 4}  # duplicates are removed automatically
numbers.add(5)  # adding an element
numbers.remove(2)  # removing an element
print("set:", numbers)

#union of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # or set1 | set2
print("union:", union_set)

