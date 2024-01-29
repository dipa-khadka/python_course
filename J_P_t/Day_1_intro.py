# find the maximum number between two number by taking input from user.
number_1=int(input("Enter the first number"))
number_2=int(input("Enter the second number"))

if number_1>number_2:
  print("number_1 is largest")
else:
  print("number_2 is largest")

# find the maximum number between three number by taking input from user.
number_1=int(input("Enter first number"))
number_2=int(input("Enter second number"))
number_3=int(input("Enter third number"))

if number_1>number_2 and number_1>number_3:
  print("Number_1 is larger")

elif number_1<number_2 and number_2>number_3:
  print("number_2 is larger")

else:
  print("number_3 is large")

# find the maximum number between three number by taking input from user.using ternary conditional statement.
number_1=int(input("Enter first number"))
number_2=int(input("Enter second number"))
number_3=int(input("Enter third number"))

maximum_number=number_1 if number_1>number_2 and number_1>number_3 else(number_2 if number_2>number_3 and number_2>number_1 else number_3)

print(maximum_number)

 # find the maximum number between twonumber by taking input from user.using ternary conditional statement.
number_1=int(input("Enter first number"))
number_2=int(input("Enter second number"))

maximum_number=number_1 if number_1>number_2  else number_2
print(maximum_number)

# LOOP IN PYTHON
x=[1,2,3,4,5,6]
for item in x:
  print(x)

# program to print even numbers from 1 to 10

num = 0

while num < 10:
    num += 1

    if (num % 2) = 0:
        continue

    print(num)

  

i=0
while i<5:
  if i==3:
    print("continue")
    i=i+1
    continue

if i==3:
  print("........")

else:
  print('hello')
  i=i+1

infinite loop
while True:
  print('Hello world')

# using range funtion print:
*
**
***
****
*****
i=0
for i in range(5):
  print("*" * (i+1))

i=20
if i%2==0:
  print("even")

else:
  print("odd")

# wap a python program to print: using range function
1
12
123
1234
123
# write a program that takes a string as inpyt and counts the number of vowels (a,e,i,o,u) using a for loop.
input_string = input("Enter a string: ")
vowel_count = 0

for char in input_string:
  if char.lower() in "aeiou":
    vowel_count += 1

print("Number of vowels:", vowel_count)
# write a program that generates all possible combinations of three numbers from 1 to 5 usingn nested for loops and prints them
for a in range(1, 6):
  for b in range(1, 6):
    for c in range(1, 6):
      print(a, b, c)

# python for loop:
# for loop
# 1> iterating over string
name="arjun"
for i in name:
  print(i)
  if(i=="j"):
    print("this is something special")

# 2>iterating over list
color=["red", "green", "yellow", "black"]
for x in color:
  print(x , end=",")
  # to iterate over color for eg. red or present in list
  for c in x:
    print(c)

range() function:
for i in range(1, -1):
  print(i)


for i in range(1,9):
  if(i%2)==1:
   print(i)

# while loop
i=int(input("Enter the number"))
while(i<=60):
  i= print(int(input("enter your number:")))
  print(i)

print("done with the loop")

# use of break statement:
# whenever we start a loop , we want it to exist and stop at specific spot for this we use break.
# means exit the loop
for i in range(10):
  print("5 X ", i + 1, "=", 5 * (i + 1))

# use of continue statement:
# sometimes we want to skip a particular iteration of loop  for thus we use continue.
# means exit the iteration

# function in python
# NOTE:
# def - keyword used to declare a function
# function_name - any name given to the function
# arguments - any value passed to function
# return (optional) - returns value from a function

# Finding the greatest number using function
def find_greatest(num1=20, num2=30, num3=40):
  greatest_num = max(10, 20, 30)
  print("The greatest number is:", greatest_num)

find_greatest()

def add(a):
  b=a+1
  print(a,"value of :",b)
  return(b)
  return(a)

# write a puthon function that takes two interger input from user and print greater .(no parameter , no return)
def find_greater():
  num1=int(input("Enter first number:"))
  num2=int(input("Enter second number:"))

  greatest_num=max(num1,num2)
  print("greatest number:",greatest_num)

find_greater()

# Finding the smallest number among two number
def find_greater():
  num1=int(input("Enter first number:"))
  num2=int(input("Enter second number:"))

  greatest_num=min(num1,num2)
  print("smallest number:",greatest_num)

find_greater()

# create function parameters and without return statement  take integer input from user.
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
def find_greatest(num1, num2):
  greatest_num = max(num1,num2)
  print("The greatest number is:", greatest_num)

find_greatest(num1,num2)

in another way:
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

def find_greater(num1,num2):
  if num1>num2:
    print("greater number is :", num1)

  else:
    print("greater number:",num2)

find_greater(num1,num2)

# creat a function to find the greater number among two number take integer input form user without usig parameter and with return statement

def find_greater_number():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))

  if num1 > num2:
    return num1
  else:
    return num2

result = find_greater_number()
print("The greater number is:", result)

# in another way:
def find_greater_number():
  num1 = int(input("Enter the first number: "))
  num2 = int(input("Enter the second number: "))

  if num1 > num2:
    msg = "num1 is greater"

  elif num1 == num2:
    msg = "num1 and num2 is equaal"

  else:
    msg = "num1 and num2 is equaal"

msg = find_greater_number()
print(msg)

# write a python program that takes two integer as a argument and return greater number from function.
def find_greater_number(num1, num2):
  if num1 > num2:
    return num1
  else:
    return num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = find_greater_number(num1, num2)
print("The greater number is:", result)

 in another way
def find_greater_number(a, b):
  pass

a = 4
b = 5

msg = find_greater_number(a, b)
print(msg)

# LOCAL VS GLOBAL VARIABLE:
# Q.1> Local variable

# wap a python program to pass multiple value through argument.
def fun(a, *b):
  print(a)
  print(type(a))

fun(1, 2, 3, 4, 5, 6, 7)


# write a python program function that return multiplicatioin of a all the numbers passed by user as a argument.
def multiply_numbers(*args):

  result = 1
  for n in args:
    result *= n
  return result


mul1 = multiply_numbers(2, 3, 4)
print(mul1)


# arbitary keyword argument:(**kwargs)
def my_function(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")

my_function(name="sita" , age=30 , address="dang")


form math import *
floor (2.4)


a = int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(a):
    print(fibonacci(i))
print(fibonacci(6))

