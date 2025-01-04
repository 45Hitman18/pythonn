# Encapsulation: to control access to private or internal attributes of a class.

class Game:
    def __init__(self, name):
        # private attributes
        self.__name = name
    
    # getter method to access the name
    def get_name(self):
        return self.__name

    # setter method to modify the name
    def set_name(self, name):
        self.__name = name

# example usage
obj = Game("Alice")

# using getter to retrieve the name and age
print("Name:", obj.get_name())  # output: Name: Alice

# using setter to modify the name
obj.set_name("Bob")
print("Updated Name:", obj.get_name())  # output: Updated Name: Bob
