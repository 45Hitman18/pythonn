class Student:
    def __init__(self, name, age):
        self.__name = name  # private variable, this need to define by (__var)
        self.__age = age    # private variable

    def display_info(self):
        print(f"student name: {self.__name}, age: {self.__age}")

student = Student("john", 20)

print(student._Student__name)  # john
print(student._Student__age)   # 20

 

