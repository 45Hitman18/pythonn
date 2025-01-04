class Student:

    college_name = "ABC College"  #this line remain same in every object, 
                                  #when we pass collage.name because we declare it outside the constructor

    def __init__(self, name, marks): # if there is only self then it is called default constructor
                                     # but we pass parameter so its called parameterised constructor
        self.name = name             
        self.marks = marks

    def get_marks(self):   # its called method
        return self.marks
    
s1 = Student("karan", 97)  # s1 is called object

print(s1.get_marks())


