"""
Strings

    string is data type that stores a sequence of characters.


Basic Operations:

    concatenation:
            -> connecting two strings using +

""" # type: ignore
#example

str1 = "Gan"
str2 = "esh"
finalStr = str1 + str2
print(finalStr)

"""     
    length of string
        -> using length function we find out the total length of the string        
        """

print(len(finalStr))


'''
    Indexing:-
    
        index staring from 0
        '''

a = "Ganesh"
ch = a[5]
print(ch)

'''
    Slicing:-
    
        Accessing parts of the string.

        str[starting_index:ending_index] #ending idx is not included

        '''

str = "Ganesh is a good boy"
print(str[1:len(str)]) #use len(str) for last index.


''' 

Slicing:-

    negative index ->
        
        A  p  p  l  e
       -5 -4 -3 -2 -1

        '''

str = "Ganesh"

print(str[-3:-1])


'''
    String Functions:- 
    
    '''

str = "i am learing python"

print(str.endswith("n")) #returns true if string ends with substr
print(str.capitalize()) #capatilizes 1st char
print(str.replace("python","java"))  #replaces all occurences of old with new
print(str.find("e")) #returns 1st index of 1st occurance
print(str.count("p")) #count the occurance of substring

