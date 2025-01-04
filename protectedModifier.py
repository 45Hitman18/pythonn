class Parent:
    def __init__(self, name, age):
        self.name = name          # public variable
        self._age = age           # protected variable  ( define by (_var))

    def display_info(self):
        print(f"name: {self.name}, age: {self._age}")


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name, age)

  
# create an instance of the parent class
parent = Parent("john", 50)
print(parent.name)  # public 
print(parent._age)  # protected 

# create an instance of the child class
child = Child("emma", 25)
child.display_info()            # accessing parent class method

