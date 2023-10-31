# If Else Conditional Statement:
age=20

if(age>18):
    print("you can drive")
else:
    print("you can't drive")
    
# input number from user . print "positive numbe " if number is positive else print "negative number". consider 0 as positive as well.
input=int(input("Enter your number"))
print(input)

if input>= 0:
  print("positive number")

else:
  print("negative numbe")

    
# if, elif , else statement:
num=9
    
if(num>18):
        print("you are still teenage")
        
elif(num<10):
        print("you are a child")
        
else:
        print("you are mature person")
        
        
#  Nested if statement: 
num=18

if(num<10):
   print("Number is greater")
elif(num>0):
    if(num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is big")
        
else:
    print("number is zero")
    
  
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
  print("number_3 is larger")   
  
  
  
 # find the maximum number between three number by taking input from user.using ternary conditional statement.
number_1=int(input("Enter first number"))
number_2=int(input("Enter second number"))
number_3=int(input("Enter third number"))

maximum_number=number_1 if number_1>number_2 and number_1>number_3 else(number_2 if number_2>number_3 and number_2>number_1 else number_3)

print(maximum_number)

#  find the maximum number between twonumber by taking input from user.using ternary conditional statement.
number_1=int(input("Enter first number"))
number_2=int(input("Enter second number"))


maximum_number=number_1 if number_1>number_2  else number_2
print(maximum_number)

 
 
    
# Match case statement:
# exammple_1:
in_put=int(input("Enter the number"))

match in_put:
    case 0:
        print("not matching")
    case 10:
        print("case is matching")
    case _ if in_put>10:
        print("........")    
        
# For loop:
n = 10
for i in range(0 , n):
  print(i)
  
  # Iteration over a list
  print("List operator")
  l = ["save", "water"]
  for i in l:
    print(i)
    
    
  # Iteration over a tuple
  print("we are iterating the tuple note: tuple is immutable")
  t = ("hi", "I", "am" , "Student")
  for i in t:
    print(i) 
    
# Iteration over the string
print("This is string iteration")
s = "Hi i am learning django"
for i in s:
  print(i)
  
  
  # Iteration over the dictionary
  print("we are iterating over the dictionary")
  d = dict()
  d['xyz'] = 123
  d['abc'] = 345
  for i in d:
    print("%s %d" % (i, d[i]))
    
  # Iteration over a set
  print("We are iterating over the set")
  set1 = {1,2,3,4,5,6,7,8,9}
  for i in set1:
   print(i)
        
    