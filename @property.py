class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value

obj = MyClass(10)
print(obj.value)  # access without parentheses



#the @property decorator makes a method behave like an attribute. it allows you to access a method without parentheses.