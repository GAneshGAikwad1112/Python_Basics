"""
Input in Python

input() statement is used to accept values(using keyboard) from user

input() #result for input() is always a str 

int(input()) # int

float(input()) # float

"""

#Example

val = input("Enter value: ") #by-default takes the type as string
print(type(val), val)



# Example

name = input("Enter a name: ")
age = input("Enter a age: ")
marks = input("Enter a marks: ")

print(type(name), type(age), type(marks),)
print(name,age,marks) 