
'''
Functions in python:

    Block of statement that performs a specific task
    

    syntax

    def function_name(parameter1, parameter2....):
        #some works


    return value
    '''
#function defination
def sum(a, b):  #parameters
    s = a + b
    print(s) 
    return s   #used print(sum) / return sum

# sum( 5, 10)#function call; arguments



#function defination
def cal_sum(a, b):  #parameters
    return a+b

s = cal_sum(2, 1) #function call; arguments

print(s)



#example

def hello():
    print("Hello")

output =  hello()
print(output)    #output None


#example

def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg
cal_avg(95, 99, 60)


'''
Types of functions:
  1) Built in function :   print(), len(), type(), range() 
  
  2) User defined function: we can write a function for our code execution
  
  
Default Parameters:
    Assigning a default value to parameter, which is used when no argument is passed.'''


#example

def cal_prod(a = 10, b = 2):
    print(a * b)
    return a * b

cal_prod ()


#example

cities = [ "pune", "noida", "chennai", "mumbai"]
def print_len(list):
    print(len(list))

print_len(cities)


#example

cities = [ "pune", "noida", "chennai", "mumbai"]
heros = [ "thor", "captain america", 'sktiman']

def pri(list):
    print(len(list))

def priint_list(list):
    for item in list:
        print(item, end =" ")

pri(heros)
priint_list(heros)



#example

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i

    print(fact)
    
cal_fact(8)


#example #convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD = ", inr_val, "INR")

converter(73)



'''
Recursion:- 
    when a function calls itself repeatedly 
    
    example: 

    def show(n):
        if (n == 0 ):
            return
        print(n)
        show(n-1)
    '''
#example
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)        

show(5)