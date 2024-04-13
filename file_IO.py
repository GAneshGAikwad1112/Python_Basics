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