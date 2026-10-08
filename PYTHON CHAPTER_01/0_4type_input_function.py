#type() function is used to 
#find the data type of a given variable in python.

a = 31 
type(a) # class <int> 

b = "31" 
type (b) # class <str>

"""
A number can be converted into a string and vice versa (if possible)
There are many functions to convert one data type into another

"""

#str(31) =>"31" # integer to string conversion
#int("32") => 32 # string to integer conversion 
#float(32) => 32.0 # integer to float conversion




# INPUT () FUNCTION 

#This function allows the user to take input from the keyboard as a string.

A = input ("enter name") # if a is "harry", the user entered amey 

""" 

The input() function in Python is used to take input from the user.
By default, it returns the entered 
data as a string (str). If we need
the input in a specific data type,
we use type conversion such as int(), float(), etc.

"""

"""
For example:

a = input("Enter number 1: ")
b = input("Enter number 2: ")

print(a + b)

If you enter:

5
10

Output will be:

510

because "5" + "10" means string concatenation.

But:

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(a + b)

Output:

15

"""
