
# \n for new line

#  for single line comment

"""
MULTI-LINE COMMENT STARTS LIKE THIS
+ and , to concat string
+ for string to string and , to concat for different data type
"""


'''

a = "Nabay"
b = 21
print(a,"is",b,"years old.")

b = str(21)
print(a + " is " + b + " years old.")

'''

'''
print("Print equilateral triangle Pyramid using stars")

size = 5
m = (2 * size) - 2

for i in range(0, size):
    for j in range(0, m):
         print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("*", end = " ")
    print(" ")
'''


'''
Calculator
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
sum = a+b
diff = a-b
mul = a*b
div = a/b
floorDiv = a//b
modulo = a%b
print(f"The sum, difference, product, quotient , floor_quotient and remainder of are:{sum},{diff},{mul},{div},{floorDiv},{modulo}")
'''

'''
#STRING SLICING AND METHOD

# print("I want to \n eat an apple ")

# for i in "Nabaraj":
#     print(i)



## STRING  SLICTING
fruit = "orange"
length = len(fruit)
print(fruit[-3:-1])


###STRING METHOD

a = "Hi!!!!!!! Nabaraj. please dont do it everytime. you Are not good boy."
# a = "Nabaraj!!!!!!!!"
print(a.upper())
print(a.lower())

# rstrip("!") removes all the ! presented in the string
print(a.rstrip("!"))
print(a.replace("aba","urba"))

# converts string to list
print(a.split(" "))

#only capitalize the first letter in the string
print(a.capitalize())



NewString= "Welcome to my channel."

print(len(NewString))
print(len(NewString.center(46)))

## To align the string to the center specifying width as the parameter
print(NewString.center(100))

print(NewString.count("a"))

print(NewString.endswith("channel."))
print(NewString.endswith("to",7,10))

## find to in string . and give the index of t of first to
print(NewString.find("to"))

##work same as find but throws an error if the searched pattern is not found
print(NewString.index("to"))

print(NewString.isalnum())
print(NewString.isalpha())
print(NewString.islower())
print(NewString.isupper())
## printable returns true if the string doesnot contain backward slash
print(NewString.isprintable())
print(NewString.istitle()) # first letter only should be capitalize
print(NewString.isspace()) # returns true if it is space
print(NewString.startswith("Wel"))
print(NewString.swapcase()) # upper to lower and lower to upper


'''
'''

## OPERATORS IN PYTHON. >,<,<=,>=,+,-,*,/,==,!=


## Conditionals
num = int(input("Enter the number:"))
if num<0:
    print(f"{num} is negative.")
elif num>0:
    if num< 10:
        print(f"{num} is less than 10.")
    elif num >=10 and num < 20:
        print(f"{num} is between 10 and 20.")
    else:
        print(f"{num} is greater than 20.")
else:
    print(f"{num} is 0.")
'''



"""
# GREETINGS

import time
##Asuming goodmorning to  11:59:59 , goodafternoon upto 4:59:59, goodevening upto 6:59:59, else goodnight
current_time = time.localtime()
hour = current_time.tm_hour
minutes = current_time.tm_min
seconds = current_time.tm_sec

print("Current time: {}:{}:{}".format(hour, minutes, seconds))
hour = int(hour)
minutes = int(minutes)
seconds = int(seconds)

TotalTimeFrame = (hour * 60 * 60) + (minutes * 60) + seconds

if TotalTimeFrame > 43199:
    if TotalTimeFrame < 61199:
        print("Good Afternoon Sir!!")
    elif TotalTimeFrame < 68399 and TotalTimeFrame >= 61199:
        print(" Good Evening Sir")
    else:
        print("Good Night Sir")
else:
    print("Good Morning Sir")
"""



"""
##Day separator using switch case 
num = int(input("Enter the number in form of day:"))
match  num:
    case 1:
        print("Today is Sunday")
    case 2:
        print("Today is Monday")
    case 3:
        print("Today is Tueday")
    case 4:
        print("Today is Wednesday")
    case 5:
        print("Today is Thursday")
    case 6:
        print("Today is Friday")
    case 7:
        print("Today is Saturday")
    case _:
        print("Please Enter the valid day")
"""




#####FOR LOOP
"""
for i in "Nabaraj":
    print(i)
    if i == "b":
        exit()

for i in range(10):
    print(i)
for i in range(0,10):
    print(i)


for i in range(2,5):
    print(i)
for i in range(0,10,2):
    print(i)
"""



"""
### WHILE LOOP
i = 0
while (i<5):
    print(i)
    i+=1
### DECREMENTING WHILE LOOP
count = 10
while(count>5):
    print(count)
    count-=1
"""


"""
### While loop with else statement
count = 10
while(count>5):
    print(count)
    count-=1
else:
    print("You have successful reached to the 5")
"""


"""
# Continue and Break in for loop
for i in range(10):

    if i == 5:

        continue
        if i == 7:
            break
    print(i)
"""

"""
###Functions in python
def sum(a,b):
    return a + b

print(sum(2,3))

# if def sum(a=10,20) we pass value to parameter
# sum(b=20,a =10) it is same as sum(10,20)
"""


"""###List slicing
MyList = [1,3,4,6,4,7,8,2,3]
print(MyList[1:5])
print(MyList[1:5:2])
"""

"""###List Comprehension
lst = [i for i in range(10)]
print(lst)
list = [i for i in range(100) if i%9 == 0]
print(list)
"""

"""
###List methods
MyList = [1,3,4,6,4,7,8,2,3]
for i in MyList:
    print(i)
MyList.sort()
MyList.sort(reverse=True)
MyList.append(19)
print(MyList)
print(MyList[-1])
print(len(MyList))
print(MyList[9]) ## -1 = 10-1 = 9
print(MyList.reverse())
print(MyList.index(4))
print(MyList.count(4))
MyList.insert(1,45)
print(MyList)
MyList1 = [1,3,4,6,4,7,8,2,3]
MyList2 = MyList + MyList1
MyList.extend(MyList1)
###both works the same
print(MyList2)
print(MyList)
"""

"""###Tuple are immutable but can be changed when converted to list and then it can be finally back to tuple
T1 = (1,3,4,6,4,7,8,2,3)
T2 = (1,9,18,21,45,78,4,6,4,7,8,2,3)
T = T1+T2
print(T[1:6])
print(T[1:6:2])

print(T.count(4))
print(T.index(4))
print(T.index(3,1,8)) ## count 3 from 1 to 8
print(len(T))

TempList = list(T)
print(TempList)
newTuple = tuple(TempList)
print(newTuple)
"""

"""
##fstring
a = 54
b = "Hari"
print(f"My name is {b} and my age is {a}")

# DocString in python
def sum(a,b):
    '''The function takes the two argument a and b to return the sum'''
    return a +b
print(sum.__doc__)
print(sum(34,48))
"""

"""
##factorial
def fact(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * fact(n-1)
print(fact(5))


###Fibonacci
def f(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(6))
"""


"""###sets in python to return distinct elements are are immutable, doesnot maintain order
sets = {1,2,3,2,3,5,7,7,9}
print(sets)
for i in sets:
    print(i)

##to create an empty set
myset = set()
print(type(myset))

s1 = {1,2,5,8}
s2 = { 3, 4, 5}
print(s1,s2)
print(s1.union(s2))
print(s1.update(s2)) #every value of s2 will be updated to s1 in this context
print(s1,s2)

print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1)

s1 = {1,2,5,8}
s2 = { 3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3 )
s4 = s1.difference(s2)
print(s4)

##every update function updates the set with which you are applying update statement


s1 = {1,2,3,4,5,6,7,8}
s2 = {3,4,5}
print(s2.issuperset(s1))
print(s1.issuperset(s2)) ##return true
s1.add(9)
s1.remove(8) #raise error if the parameter passed is not in set
s1.discard(8) ##donot raise error if the parameter passed is not in set
print(s1)

print(s1.pop())
print(s1)
#del s1 will delete the s1 set

if 1 in s1:
    print("yes")
else:
    print("No")
"""

"""##dictionary as key value pair used to store value on the basis of key , Dictionary are ordered
info = {'name':'nabay','roll':102}
print(info)
# print(info('depart')) # throws an error if key is not in the dict
print(info.get('depart')) # throws boolean if key is not in dict

for i in info.keys():
    print(i)

print("now Values")

for i in info.values():
    print(i)

for key,value in info.items():
    print(key,value)


###Dictionary methods
Emp = {1:51,2:52,3:53}
Emp2 = {4:51,5:52,6:53}
Emp.update(Emp2)

Emp.pop(3)
print(Emp)
Emp.popitem() # automatically remove the last key value pair
print(Emp)
del Emp2 # delete Emp2 and throw an error if trying to print
del Emp1[4] # delete using key
"""

"""
##ELSE statement with looping
for i in range(10):
    print(i)
    if i ==4:
        break
else: #loop is not broke, loop completed successfully. so else statement wont be print
    print("Sorry no i")

##this will print the else statement too
for i in range(10):
    print(i)
else: #loop is not broke, loop completed successfully. so else statement wont be print
    print("Sorry no i")
"""


"""##ExceptionHandling in python
try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)
# except Exception as e:
#     print(e)
except:
    print("Error: Denominator cannot be 0.")
#line after this will be successfully executed.

finally:
    print("I am executed in every case") ## finally blocks works perfect when exception handling  is inside the function
"""

"""###Custom Error
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
"""

"""
# shorthand if else
a = 10
b = 10
print(a) if a>b else print("=") if a==b else print(b)
"""


"""## Demonstrate the use of enumerate function
marks = [1,2,3,4,23,45,79,12,56]
index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("You are at 4")
    index+=1
print("Now enumerate")
#Enumerate
marks = [1,2,3,4,23,45,79,12,56]
for index,mark in enumerate(marks): #pack the marks and index into separate tuple
    # print(index,mark)
    print(mark)
    if index == 3:
        print("You are at 4")
"""

"""import math as m
from math import sqrt as s
print(dir(math))
if __name__ == "__main__":
    function1() #one time execution of the imported module

"""

"""
#os module is used to open file, folder  , rename them, delete them
"""


"""Local and Global variable
file handling---49
to store marks , score 

"""


# print("Python program to print the pyramid:")
# size = int(input("Enter the size of the pyramid"))
# spaces = 2 * size - 2
# for i in range(size):
#     for j in range(spaces):
#
#         print("*",end = " ")
#     print("")

# size = 5
#
# for i in range(size):
#     print(" " * (size - i - 1) + "* " * (i + 1))

# size = 5
#
# for i in range(size):
#     print(" " * (size - i - 1) + "* " * (i + 1))
# #
# #
#
#
#
# size = 5
# for i in range(size):
#     spaces = " " * (size - 1-i)
#     stars = "* "*(i+1)
#     print(spaces+stars)







































