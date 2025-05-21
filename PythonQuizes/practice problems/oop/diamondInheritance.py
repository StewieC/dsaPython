class Class1:
    def m(self):
        print("in class 1")

class Class2(Class1):
    def m(self):
        print("in class 2")
        
class Class3(Class1):
    def m(self):
        print("in class 3")
        
class Class4(Class3, Class2):
    # def m(self):
    #     print("in class 4")
    pass
        
see = Class4()
see.m()

# when method is overridden in one of the classes

class Animal:
    def m(self):
        print("i could be any animal")
        
class Dog(Animal):
    pass

class Cat(Animal):
    def m(self):
        print("i am a cat")
        
class pets(Cat, Dog):
    def m(self):
        print("i am a home pet")
        
obj = pets()
obj.m()  # Output: i am a home pet