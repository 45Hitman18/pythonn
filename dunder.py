
class MyClass:
    
    def __init__(self, items):
        self.items = items  
    
    def __len__(self):    # __len__ allows using len() on the object
        return len(self.items)
    
   
    def __add__(self, other):    # __add__ allows using + to combine two objects

        return MyClass(self.items + other.items)  # combines two lists
    
    
    def __eq__(self, other):     # __eq__ allows using == to compare two objects
        return self.items == other.items


obj1 = MyClass([1, 2, 3])
obj2 = MyClass([4, 5])
obj3 = MyClass([1, 2, 3])

# using __len__
print('Length of obj1:', len(obj1))  # calls __len__

# using __add__
obj4 = obj1 + obj2  # calls __add__
print('Combined items:', obj4.items)

# using __eq__
print('obj1 == obj3:', obj1 == obj3)  # calls __eq__
print('obj1 == obj2:', obj1 == obj2)
