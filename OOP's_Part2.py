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
    
    def __init__(self, Acc_no, Acc_pass):
        self.Acc_no = Acc_no
        self.__Acc_pass = Acc_pass

    def reset_pass(self):
        print(self.__Acc_pass)

acc1 = Account(" 12578 ", "abc")

print(acc1.Acc_no)
#print(acc1.Acc_pass)  #private veriable is not accessible outside the class
