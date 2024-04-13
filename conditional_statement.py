# if-elif-else statements

#syntax

'''

if (condition):
    statement 1

elif(condition):
    statement 2

else:
    statement N
    
    '''

# Example

# light = input("light: ")

# if (light == "red"):
#     print("stop")

# elif(light == "yellow"):
#     print("look")

# elif(light == "green"):
#     print("go")

# else:
#     print("light is broken")


# Example

# marks =  int(input("marks: "))

# if (marks >= 90):
#     print("A")

# elif (marks >= 80):
#     print("B")

# elif (marks >= 70):
#     print("C")

# else:
#     print("D")


# Example

"""
print output for:

A = 5 & G = M
A = 2 & G = F

"""

# A = int(input("A: "))

# G = input("M/F: ")

# if((A ==1 or A == 2) and G == "M"):
#     print("fee is 100")

# elif(A == 3 or A == 4 or G == "F"):
#     print("fee is 200")

# elif(A == 5 and G == "M"):
#     print("fee is 300")

# else:
#     print("No fee")
    
    
'''
    Nested statement:

        conditions under the conditions called nested statement

 
'''

age = 80

if (age >= 18):
    if(age >= 60):
        print("can't drive")
    else:
        print("can drive")

else:
    print("can't drive")    