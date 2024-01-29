# print strings
print('Hello World!!!')

# print int value
print(78)

# print floating value
print(5.7)

print('apple','orange','kiwi','banana',sep='-')

print("Hello" ,end=' ')
print('Nepal')


# python supports 3 categories of Data types:
'''
1. Basic Types (integer, float, complex, boolean and string)
2. Container Types (List, Tupels, Sets and Dictionary)
3. User-defined Types -class
  
'''
### BASIC TYPES :-  
# integer
print(4)
print(5000000050)

# float
print(5.6)
print(567.889680000070)

# complex
print(7+4j)


# string
print("Hi , maya")
print('Hi, Srijana')
print('''Hi, susma''')


####  CONTAINERS TYPES :-
# List
print([1,2,3,4,5])

# Tuple
print((1,2,3,4,5))

# sets
print({1,2,3,4,5})


# dictionary
print({'Name':'Maya','Age':30, 'Gender':'Female'})



# COMMENTS :-
'''COMPILER CAN'T EXECUTE THE CODE '''


# Variables
# in python there is no need to declaration of variable types this features is also known as Dynamic Typing.
name = 'maya'
age = 18

print(name,age)

# python also has Dyanamic Binding which means one variable can store multiple data types or values.

# special syntax
a=10; b=15; c=20
print(a,b,c)

a,b,c=2,4,6
print(a,b,c)
      
      
a = b= c= 13
print(a,b,c)