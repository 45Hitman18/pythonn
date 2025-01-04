# single inheritance
class Parent:
    def speak(self):
        print("Parent speaks")

class Child(Parent):
    pass

A = Child()
A.speak()


# multiple inheritance
class Father:
    def speak_father(self):
        print("Father speaks")

class Mother:
    def speak_mother(self):
        print("Mother speaks")

class Child(Father, Mother):
    pass

A = Child()
A.speak_father()
A.speak_mother()


# multilevel inheritance
class Grandparent:
    def speak_grandparent(self):
        print("Grandparent speaks")

class Parent(Grandparent):
    def speak_parent(self):
        print("Parent speaks")

class Child(Parent):
    pass

A = Child()
A.speak_grandparent()
A.speak_parent()


# hierarchical inheritance
class Parent:
    def speak(self):
        print("Parent run")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

A1 = Child1()
A2 = Child2()
A1.speak()
A2.speak()


# hybrid inheritance
class A:
    def speak_a(self):
        print("A speaks")

class B(A):
    def speak_b(self):
        print("B speaks")

class C(A):
    def speak_c(self):
        print("C speaks")

class D(B, C):
    pass

d = D()
d.speak_a()
d.speak_b()
d.speak_c()
