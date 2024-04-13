#string and numeric values can operate together with *

A, B = 2, 3

txt = "@"

print(2*txt*3)


#string and string can operate with + (concatination)

A, B = "2", 3

txt = "@"

print((A+txt) * B)

#Numeric vlues can operate with all arthmetic operators

A,B=2,3
C=4
print(A+B*C)

#Arthmetic expression with integer and float will result in float

A,B=10,5.0
C=A*B
print(C)

#Result of division operator with two integers will be float

A,B=1,2
C=A/B
print(C)

#integer division with float and int will give int displayed as float

A,B = 1.5,3
C=A//B
print(C, A/B)


#floor gives cloest integer, which is lesser than or equal to the float value 
    #Result of (A // B ) is same as floor(A/B)

A,B=12,5
C = A//B
print(C)


A,B=-12,5
C = A//B
print(C)

A,B=12,-5
C = A//B 
print(C)


#Remainder is negative when denominator is negative

A,B=-5,2
C = A%B 
print(C)

A,B=5,2
C = A%B 
print(C)

A,B=5,-2
C = A%B 
print(C)