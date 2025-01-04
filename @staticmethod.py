class MyClass:
    @staticmethod
    def add(a, b):
        return a + b

print(MyClass.add(5, 3))  # no instance needed


#the @staticmethod decorator defines a method that does not depend on the instance or class. it works like a regular function.