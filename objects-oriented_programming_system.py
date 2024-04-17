'''  
OOP in python: 

    To map with real world scenarios, we started using objects in code.
    This is called object oriented programming


    Class and object in python:
        class is a blueprint for creating objects.

        #creating class

            class Student:
                name : "Ganesh"
        
        #creating object (instance)

            s1 = Student()
            print(s1.name)

            
'''
 

class Student:
    name = "Ganesh"


s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


# #example

class Car:
    color = "Blue"
    Brand = "MG"

car1 = Car()
print(car1.Brand)


'''
    __init__ function:
    
        Constructor: All classes have a function called __init__(), which is always executed when the object is being initiated.
        
            #creating class
            
            class Student:
                def __init__(self, fullname):
                    self.name =  fullname 
                    
                    
            #creating object

            s1 = Student("Ganesh")
            print(s1.name)

                    
'''

#example

class Student:
    college_name = " ABC college "
    name = "Gan's"
    #default constructors
    def __init__(self):
        pass

    #parameterized constructor
    def __init__(self, name, marks):
        print("adding new student in Database...")
        self.name = name
        self.marks = marks
        

        
s1 = Student("Ganesh", 90)

print(s1.name)
print(s1.marks)

print(s1.college_name)


#................The self parameter is a refrence to the current instance of the class, and is used to access variables that belongs to the class....

'''

Class Attributes and Instance Attributes: 

    -self is reference of object
'''


'''

Methods:
    
    methods are functions that belong to objects.
    
    
    
    '''
#Example

#crating a class 
    
class Student:
    def __init__(self, fullname):
        self.name = fullname
            
    def hello(self):
        print("hello",self.name)
            
    #creating object
    
s1 = Student("Ganesh")
s1.hello()


#Let's Practice

#create student class that takes name and marks of 3 subjects as arguments in constructor.
#then create a method to print the average....

class Student:
    
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi" , self.name, "Your average score is : ", sum / 3)

s1 = Student("Ganesh",[99,88,70])
s1.get_avg()

s1.name = " Jon "

s1.get_avg()



'''

Static Methods:

    methods that don't use the self parameter(work at class level)

    class Student:
    
    @staticmethod   #decorator
    def college():
    paint("ABC college")


'''

#..........Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it ....


#example

class Student:

    def __init__(self):
        pass

    @staticmethod

    def college():
        print("ABC college")

s1 = Student()
s1.college()



''''
Important
        
        Abstraction:
            Hiding the implementation details of a class and only showing the essential features to the user..
            
            
            
        Encapsulation:
            Wrapping data and functions into a single unit(object).
            

'''

#example #Abstraction

class Car:

    def __init__(self):
        self. acc = False
        self. brk = False
        self. clutch = False


    def start(self):
        self. clutch = True
        self. acc = True
        print("car started......")
      

car1 = Car()
car1.start()


#Let's Practice

#create Account class with 2 attributes - balance and account no.
#create methods for debit, credit and printing the balance....


class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited. ")
        print("Total Balance:",self.get_balance())
        
    #Credit method

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount, "was credited. ")
        print("Total Balance:",self.get_balance())    
    
    #Total balance
    
    def get_balance(self):
        return self.balance

acc1 = Account(50000, 445246)
acc1.debit(5000)
acc1.credit(10000)


