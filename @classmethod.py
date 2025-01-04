class MyClass:
    count = 2
    
    @classmethod
    def show_count(cls):
        print(f"Count is: {cls.count}")

MyClass.show_count()  # works without an instance


#the @classmethod decorator makes a method act on the class itself, not the instance. it uses cls as its first parameter.