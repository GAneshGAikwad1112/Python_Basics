'''
    File  I/O in python

        Python can be used to perform operations on a file.(read and weite data)
        
        Types of all files:
            1. Text files: .txt, .docs, .log etc
            2. Binary Files: .mp4, .mov, .png, .jpeg etc.
            
        syntax: 
                f = open("file_name","mode")
            
'''


f = open("domo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

'''
'r' - open for reading(default)
'w' - open for writing, truncating the file first
'x' - create a new file and open it for writing
'a' - open for writing, appending to the end of the file if it exists 
'b' - binary mode
't' - text mode(default)
'+' - open a disk file for updating(reading and writing)

'''

'''
Reading a file:
    
    data = f.read() #reads entire file
    
    data = f.readline() #reads one line at a time
    
    '''

f = open("domo.txt","r")

line = f.readline()
print(line)

f.close()


'''
Writing to a file:

    f = open("domo.txt","w")
    f.write("this ia a new line") #overwrites the entire file
     
      
    f = open("domo.txt","a")
    f.write("this is a new line") #adds to the files

'''


'''
With syntax:

    with open("demo.txt","r") as f:
        data = f.read()
        print(data)   #using with no required to close the file [f.close()]
'''


'''
Deleting a file:

    using the os module
    module (like a code library) is a file written by another programmer that generally has a functions we can use....

    syntax:
            import os
            os.remove(filename)    
'''


#example

with open("practice.txt","r")as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)


#example #find the word "learning"
word = "learning"
with open("practice.txt","r")as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")

    else:
        print("Not Found")


# example #check_for_line
def check_for_line():
    word = "Python"
    data = True
    line_no = 1
    with open("practice.txt","r")as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no +=1 

    return -1


check_for_line()

#example #number seprated by comma, print the even number from the list of number


count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1
print(count)