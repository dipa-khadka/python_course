# x=5
# y="maya"
# print(type(x))
# print(type(y))

x="awesome"

def myfunc():
    print("python is" + x)
     
myfunc()


print("   *")
print("  * *")
print(" *   *")
print("* * * *")




# => "comments ,Escape Sequences & print statement"
"""#comments
    1>  # => single line comment 

     2>  '''  =>multiline comment
         '''
     """
  
# Escape Squences:
# for single:\
    # double:\*
    # back:\\
        # new line:\n
        # tab:\tkef
""" 
   \->it is a escape squence which is used to jump on a new line
       for eg:hi my name is sudha \n and i am a studenet
            -> it's output will be =>hi my name is sudha 
                                     and i am a studenet        
   """

#Print Statement
print ("Hi i am a good girl and i am 17 years old" ,6, 7 ,sep="~" , end="009\n")
print("harray")

# Variables and Data Types
a=1
print(a)
print(type(a))
a=complex(8,2)
print(type(a))
b=None
print(type(b))

" Data Type :type of values which variable can hold"

# Calculator using Python : Operators
'''
1> Airthmetic Operator:
#    Addition -> (+)
#    Subtraction -> (-)
#    Multiplication -> (*)
#    Division -> (/)
#    Modulus -> (%) => answer as reminder
#    Exponentiation -> (**) => to do squre of any number
#    Floore division -> (//) => it will remove any number which is after "." for eg: assume final answer is 10.22  but it will give you answer as 10.
   
'''


# Typecasting in Python:
'''The conversion of one data type into the other data type is known as type casting in python or type conversion python.'''
a=2
b=3
print(a,b)
print(a+b)

a="1"
b="2"
print(a,b)
print(a+b)

print(int(a)+int(b))

# Explicit data typecasting: The conversion of one data type into another data type , done via devloper or programmer's intervation
  # or manually as per the requirement.
  
" for eg:" 
string= "15"
number=7
sum=number+number
print("The sum of both variables is :" ,sum)
print(string,number)
# print(string+number)

# Implcit TypeCasting:Accoring to the level one data type is converted into ohter by the python interpreterr(automatically).
   #while performing any operations on variables with different data types
   #in python, one of the variable's data types will be changed to the higher data type to prevent data loss.
  
c=1.9
d=8

print(c+d)    
print(type(c+d) )   



# Strings:Strings are sequence of characters.strings in python are surrounded by either single quotation marks, or double quotation marks.
#    ->Assign string to a variable
a="Hello i am a web developer"
print(a)

#    ->Multile String:you can assign a multiple string to a variable by using three quotes.
apple='''He said,Hi harry 
hey i am good 
"I want to eat an apple'''
print(apple)

# Accessing Characters of a String
a="sapana"
print(apple[4])
print(apple[0])

# Looping through the String
print("we are using for loop to access characters:")
cat="maya"
for character in cat:
    print(character)

   # Strings Slicing and  Operations in python
names="Harry,Shubham"
# if you want only one name to display
print(names[0:5]) 

# to find out length
print(len(names))

fruit="Mango"
len1=len(fruit)

# concatination
num_1="strings"
num_2="concat"


# class
# non_value :using none keyword
non_value=None
print(non_value)
type(non_value)

int_value=2e2
print(int_value)
id(int_value)

# complex type
# simple way
complex_value=1+3j
print(complex_value)
type(complex_value)

# complex variable creation :approach 2 using "complex " function for eg:
complex_value=complex(1,5)
print(complex_value)

# just simple way
a=4
b=5
complex(a,b)

# to print only imaginary or real part
print(complex_value.real)


# 1> create a complex number 0j. get the Data type and print the result.
complex_num=0j
print(complex_num)
print(type(complex_num))

# 2> create a complex number 2+3j using complex() function passing integer 2 and 3.
complex_val=2+3j
complex(2,3)

# boolean type:it return true or false

print(bool(1))
print('-------')
print(bool(-1))
print('-------')
print(bool(0))


# assert keyword:
#to check wethere the ttwo strings are same or not
# assert condition,<failure_condition>
# single_string='my first string'
# double_string=="my first string"

# assert single_string == double_string





 