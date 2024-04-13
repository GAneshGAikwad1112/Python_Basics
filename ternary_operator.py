# clever if / ternary operator

# <var> = (false_val, true_val)[<condition>]

#example
age = int(input("age: "))
vote = ("Yes", "No")[age>=18]


#example

sal = float(input("salary: "))
tax = sal *(0.1, 0.2) [sal<= 50000]
print(tax)