# 1> Create empty dictionary
str_1={}
print(type(str_1))

# simple dictionary
str_2= {
 "name":"aayush",
 "add":"Dang",
 "age":5
}
print(str_2)
print(".........")
print(type(str_2))
print(len(str_2))



# Nested dictionary
str_3={
    "fruits":{"mango":2, "apple":5},
    "drink":{"coke":3, "fanta":3}
}
print(str_3)
print(len(str_3))


# indexing in dictionary
print("-....-....-")
colors={
    "blue":4,
    "red":6,
    "yellow":8
}
first_key=list(colors)[1]
first_val=list(colors.values())[1]
print(first_key)
print(first_val)

# create simple dictionry and access different items
# 1> extract value 4
colors={
    "blue":4,
    "red":6,
    "yellow":8
}
result=colors["blue"]
print(result)

# by nested dic
# extrac value 3 of key coke
str_3={
    "fruits":{"mango":2, "apple":5},
    "drink":{"coke":3, "fanta":3}
}
result=str_3['drink']['coke']
print(result)

# access vallue for key=brand
str_3.get['drink']

# dictionary are mutable
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"]=2080
print(thisdict)
print(thisdict.values())

# get the list of all lthe keys present in the dictionary
print(thisdict.keys())

# print the values in tuple
print(thisdict.items())
# to add  new values
thisdict.update({"name":"sahil"})
print(thisdict)





# Q.1>print allkeys names in the dictionary onle by one using loop
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for keys in thisdict:
  print(keys)

  # Q.2> print all values in dictionary in one by one.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for values in thisdict.values():
  print(values)
  print("....................")
  # Q.3> Print all  keys and values one by one , using items().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for key,values in thisdict.items():
  print(f'key={key}')
  print(f'values={values}')


  # dictionry comprehension offers shortest syntax for looping using index and comprehension
  sample_list={10,20,30,40,50}
  sample_dic={idx:item for idx, item in enumerate(sample_list)}
  print(sample_dic)
   