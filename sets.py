''' 
Set in python

    set is the collection of the unorderd items.
    Each element in the set must be unique & immutable
    
    ''' 

# set = { 1, 2} 
# print(type(set), set)
# print(len(set)) # total items in the set


hello =set() #empty set
print(type(hello))


'''
    Set methods:
    
       1) set.add(element) # adds an element
       2) set.remove(element) #removes the element
       3) set.clear #empties the set
       4) set.pop() #removes a random value
       5) set.union(set2) #cinbines both set values and returns new
       6) set.intersection(set2) #combines common values and returns new

        '''


# practic que1

dic = {
    "table":["a piece of furnituere","list of facts and figures"],
    "cat": "a small animal"
}

print(dic)

# practic que2

dec1 = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(dec1))

# practic que3

marks = {}
 
a = int(input("enter a vlaue: "))
marks.update({"phy":a})

a = int(input("enter a vlaue: "))
marks.update({"eng":a})

a = int(input("enter a vlaue: "))
marks.update({"math":a})

a = int(input("enter a vlaue: "))
marks.update({"sci":a})

print(marks)