'''
Loops in python:-

        loops are used to repeat instructions.
        
        types:  1) while loop
                2) for loop
                
                '''

#example #print the number from 1 to 5

# i = 1 
# while i <= 5:
#     print("hello")
#     i += 1


#example2:

# n = int(input("Enter a num: "))
# i = 1

# while i <= 10:
#     print(n * i)
#     i += 1

#example:

# indx = 0
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# while indx < len(nums):
#     print(nums[indx])
#     indx +=1 

#example:

# search = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = int(input("Enter a num: "))
# i = 0 #initialization
# while i < len(search):
#     if(search[i] == x):
#         print("number found")
#         break
#     else:
#         print(f"number is not found on {search[i]}")
#     i += 1



'''
    Break and continue: 
    
    
            Break : used to terminate the loop when encounted
            
            Continue:  terminates executation in the current iteration and continue execution of the loop with the next iteration
            
            '''


#example: 

# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1



''''
    For loop in python:

        loops are used for sequential traversal. for traversing list, string, tuples. etc.
    '''

# num =(1, 2, 3, 4)

# for val in num:
#     print(val)


'''
    Range() function:
        Range function returns a sequence of numbers, starting form 0 by default, and increments by 1(by_default), and stops before a specified numbers. '''

# seq = range(5)
# for i in seq:
#     print(i)


'''
    Pass statement: 
        Pass is a null statement that does nothing, It is used as a placeholder for future code.
    
'''

#example

# for i in range:
#     pass

# print(" Hello Everyone! ")


#example:

#write a program sum of first n natural number

n = 5
sum = 0 
for i in range(1, n+1):
    sum += i
print(sum)


#alternate solution using while loop 

n = 7 
sum = 0
i = 1

while i<= n:
    sum += i
    i+= 1

print(sum)