'''

List and Tuples in Python:

    A built-in data type that stores set of values.
    It can store elements of different types(integer, float, string, etc.)
     
    #In python string are immutable and list are mutable
    '''
marks = [60, 87, 95, 66, 45]  #list

print(type(marks), marks)

print(marks[0])
print(len(marks))

'''
list slicing is same as the string slicing

'''

'''
List methods:-

    1) list.append() : adds element at the end
    2) list.sort()   : sorts in asending order
    3) list.sort(reverse = True) : sorts in desending order
    4) list.reverse() :  reverses list
    5) list.insert(index, element) : inserting the element at the perticular index.
    6) list.remove(index): removes a perticular occerence element
    7) list.pop(index) : removes element at index

'''

#example

list = [ 2, 1, 3, 5]

print(list.append(7))
print(list)
print(list.sort())
print(list)
print(list.sort(reverse=True))
print(list)
print(list.reverse())
print(list)
print(list.insert(1,0))
print(list)
print(list.remove(5))
print(list)
print(list.pop(2))
print(list)


''''
Tuples in Python ->

    - A built-in data type that lets us create immutable sequences of values.
    
    - we uses for the tuple is ( )

    '''

''' 

    Methods of Tuples:
        1) tup.index(element) # returns index of perticular occurance
        2) tup.count(element) # counts total occurences
    
        
    '''

#example

tup = (2, 1, 3, 4)

print(tup.count(2))
print(tup.index(2))

#example

usr_input1 = input("Enter name of movie: ")
usr_input2 = input("Enter name of movie: ")
usr_input3 = input("Enter name of movie: ")
movies = []

movies.append(usr_input2)
movies.append(usr_input3)

print(movies)

#example #list is pelindrome or not

list = ["r","a","c","e","c","a","r"]

list1 = list.copy()
print(list1)
list1.reverse()

if (list1 == list) :
    print("palandrom")

else:
    print("not pelendrom")


#example

grade = ("C","D","A","A","B","A")

print(grade.count("A"))

#example
grade = ["C","D","A","A","B","A"]

grade.sort()
print(grade)