# super() method 

#1
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal named {self.name} created")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call the parent class's __init__
        self.breed = breed
        print(f"Dog of breed {self.breed} created")

# creating an instance of Dog
dog = Dog("Buddy", "Golden Retriever")



#2
class Animal:
    def speak(self):
        print("animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # calls speak from Animal
        print("dog barks")

# creating a Dog instance
dog = Dog()
dog.speak()
