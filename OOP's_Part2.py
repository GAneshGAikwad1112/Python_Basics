'''
del keyword
    used to delete object properties or object itself.
    
    del s1.name
    del s1 

'''

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Ganesh")
print(s1.name)
del s1.name
print(s1.name)



'''
Private(like) attributes and methods:
    
    Conceptual Implementations in python
        Private attributes and methods are meant to be used only within the class and are not accessible form outside the class. 

'''
#example

class Account:
    
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12578s", "abc")

print(acc1.acc_no)
print(acc1.reset_pass())
#print(acc1.Acc_pass)  #private veriable is not accessible outside the class



#Example

class Person:
    __name = "Ganesh"


    def __hello(self):
        print("Hello Person!")

    def welcome(self):
        self.__hello()

p1 = Person()

print(p1.welcome())



'''
Inharitance:
    when one class(child/derived) derives the properties and methods of another class(parent/base).

    
    syntax:

    class Car:
    .
    .
    .
    class ToyotaCar(Car):
    .
    .
    .

    
    
'''

#Example

class Car:

    color = "Black"

    @staticmethod
    def start():
        print("car has been started!")

    @staticmethod
    def stop():
        print("car has been stoped!")

class toyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = toyotaCar("Fortuner")
car2 = toyotaCar("prius")

print(car1.start())



'''

Types of Inheritance:
    1. Single Inheritance
    2. Multi-level Inheritance 
    3. Multiple Inheritance  #multiple base class single derived class
    
'''


'''

Super Method:
    super() method is used to access methods of the parent class.
    
'''

#example

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car has been started!")

    @staticmethod
    def stop():
        print("car has been stoped!")

class toyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type) 
        super().start() 


car1 = toyotaCar("electric")
print(car1.type)


'''
Class method:
    A class method is bound to the class and receives the class as an implicit argument.
    
    note - static method can't access or modify class state and generally for utility.
    
    syntax:

    class Student:
        @classmethod #decorator
        def college(cls):
            pass
        
'''

#example

class Person:
    name = "GAnesh"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("Gaikwad")
print(p1.name)
print(Person.name)


'''
Property:
    we use @property decorator on any method in the class to use the method as a property.
    
'''

#example

class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+ "%"

stu1  = Student(98, 98, 68)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)


'''
Polymorphism: Operator Overloading 
    when the same operator is allowed to have different meaning according to the context...

    Operators and Dunder function

    a + b  #addition         a._ _add_ _(b)
    a - b  #subtraction      a._ _sub_ _(b)
    a * b  #multiplication   a._ _mul_ _ _ _(b)
    a / b  #division         a._ _truediv_ _ _ _(b)
    a % b  #addition         a._ _mod_ _ _ _(b)
 
'''
#example

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num2):
        newReal  = self.real + num2.real
        newImg = self.img + num2.img

        return Complex(newReal, newImg)
    

    def __sub__(self, num2):
        newReal  = self.real - num2.real
        newImg = self.img - num2.img

        return Complex(newReal, newImg)
       

num1 = Complex(1, 3)
num1.showNum()

num2 = Complex(4, 6)
num2.showNum()

num3 = num1 - num2
num3 = num1 + num2


#Let's Practice

'''
1. Define a circle class  to create a circle with radius r using the constructor.
    define an area() method of the class which calculates the area of the circle
    define a perimeter() method of the class which allows you to calculate the perimeter oa the circle

'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return (22/7) *self.radius ** 2

    def Perimeter(self):
        return 2 * (22/7) * self.radius


c1 = Circle(21)

print(c1.Area())
print(c1.Perimeter())


'''
2. Define a Employee class with attributes role, department and salary. This class also have show details.
     '''


class Employee:

    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role : ", self.role)
        print("dept : ", self.dept)
        print("salary : ", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")

engg1 = Employee("GAnesh", 20)
engg1.showDetails()


'''
3. Create a class called order which stores item and its price.
    use dunder function __gt__() to convey that:
        order1>order2 if price of order1>price of order2 '''

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("chips", 20)
ord2 = Order("tea",15)

print(ord1 > ord2) #True