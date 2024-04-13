'''
Dictionary in Python:- 

    Dictionaries are used to store data values in key:values pairs 
    
    they are unordered, mutable(changeable) and don't allow duplicate keys
    
    '''

info = { 
    "key": "value",
    "name":"Ganesh",
    "language":"Python",
    "age" : 23,
    "is_adults" : True,
    "subjects" : ["python","c","jave"],
    "topics" : ("dict", "set"),
    12 : 32
}

null_dict = {} # to create a empty dictionary

print(info["name"])
info["name"] = "Akash"
print(info)


'''
#     Nested Dictionaries:- 
    

#         '''

info = { 
    "key": "value",
    "name":"Ganesh",
    "language":{"1st lan" : "python",
                "2nd lan " : "java"},
    "age" : 23,
}

'''Dictionary Methods:- 

    myDict.keys()  #returns all keys 
    myDict.values() #returns all values
    myDict.items() #returns all (key, val) pairs as tuples
    myDict.get("key") #returns the key according to value
    myDict.update(newDict) #inserts the specified items to the dictonary'''


myDict = {
    "name":"Ganesh",
    "roll": 14,
    "lan":"python",
    "marks": 95
}
newDict ={
    "age":23,
}
myDict.keys()  #returns all keys 
print(myDict)
print(" ")
myDict.values() #returns all values
print(myDict)
print(" ")
myDict.items() #returns all (key, val) pairs as tuples
print(myDict)
print(" ")
myDict.get("key") #returns the key according to value
print(myDict)
print(" ")
myDict.update(newDict) #inserts the specified items to the dictonary'''
print(myDict)


