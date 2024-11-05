#Following are some common operators in python:
'''
1. Arithmetic operators: +, -, *, / etc.

2. Assignment operators: =, +=, -= etc.

3. Comparison operators: ==, >, >=, <, != etc.

4. Logical operators: and, or, not.

'''
#Arithmetic  Operators
a = 6
b = 7
c = a + b
print(c) 

#Assignment Operators
a = 4-2 #assign 4-2 in a
print(a)
b = 6
b += 3 # Increment the value of b by 3 and the assign it to b 
print(b)

#Comparison Operators - their values are always in boolean
d = 5<4
e = 7==7
print(d,e) #comparing will always return a boolean value either false or true

#Logical Operators

f = True or False
#Truth table of OR
print("True or False is", True or False)
print("True or True is",True or True)
print("False or False is",False or False)
print("False or True is",False or True)

#Truth table for 'AND'
print("True and False is", True and False)
print("True and True is",True and  True)
print("False and False is",True and False)
print("False and True is",True and True)

#not operator 
print(not(False))
print(not(True))