# print("Hello World In python")
# Determine whether a user is 18 years and above
# age = 18
# if age >= 18: then the program should output "You are 18 years and above"
# else the program should output "You are below 18 years"

#if user >= age:
# output something
#else:
#output something
'''
age = int(input("Enter your age: "))
if age >= 18:
    print("You are 18 years and above")
else:
    print("You are below 18 years") 
'''

'''
if a user is >18 then print a young a person
else if a user is > 18 and < 30 them print a youth
else if a user is > 30 and <50 then print an adult
else print an old person
'''

'''age = int(input("Enter your age: "))
if age <= 18:
    print("You are a young person")
elif age > 18 and age <30:
    print("You are a youth")
elif age >30 and age < 50:
    print("You are an adult")
else:
    print("You are an old person")
'''

#loops
#for loop

'''print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
'''

'''
for i in range(1, 6):
    print("Hello World")
    '''
#while loop
'''
age = 18
while age < 18:
    print("You are below 18 years")
else:
    print("You are 18 years and above")
'''
'''
i = 0
while i < 6:
    print("Hello World")
    i += 1 # i = i + 1

else:
    print("This loop has been completed")
    '''
#functions
#function definition
#def funtion_name(): # function arguments, parameters
 #   return value
'''
def addition(a, b):
    return a + b

def multiply(a, b):
    return a * b
result = multiply(2, 3)
result1 = addition(2, 3)

def area_of_circle(radius):
    return 3.142 * radius * radius

result2 = area_of_circle(7)
print(result2)

'''

#importing modules
import math
result = math.sqrt(16)
# print(result)

import datetime
date = datetime.datetime.now()

import random
result = random.randint(1, 100)
print(result)

# define a number
# custom a user to enter guess the number between a certain range
# if the user guess the number correctly print "You have guessed the number correctly"
# else print "You have not guessed the number correctly"
 # if statements elif 
 # while loop