# #Conditions if
# import random
# if 5 > 2:
#     print("Final KamehameHAAAAA")
#         # print("wrrrrrrrrrry")

# # Assigning Variables
# x = 5
# x = "Johnny"

# """
#     This is a multi
#     line comment
#     more than a line>>>
# """
# print(x)

# #Casting
# a = str(3)
# b = int(3)
# c = float(3)

# print(type(a))

# saiyans = ["Goku", "Vegeta", "Gohan"]
# x, y, z = saiyans
# print(x, y, z)

# # Functions
# x = "Subarashi"

# def myfunc():
#     x = "o bakarayo"
#     print("Goku Black is " + x)

# myfunc()

# def nextfunc():
#     global x
#     x = "megoto"

#     nextfunc()

# print("Goku black is " + x)
# x = 1
# y = 35656222554887711
# z = -3255522

# print(type(x))
# print(type(y))
# print(type(z))

# print(random.randrange(1, 10))

# # For Loops and if syntax
# for y in "goku":
#     print(y)

# txt = "True there was a guy like that huh"
# # if "guy" in txt:
# #     print("Bombardia")
# if "brother" not in txt:
#     print("owari da")

# s = "Hello, World!"
# print(s.strip())

# test = "I'm the \"Collosal Titan\""
# print(test)

# yonkou = ["Shanks", "Blackbeard", "Buggy", "Luffy", "Luffy"]
# yonkou[4] = "Loki"
# print((yonkou))
# # i = 0
# # while i < len(yonkou):
# #     print(yonkou[i])
# #     i = i + 1

# new_kotei = [x for x in yonkou if x != "Loki"]
# print(new_kotei)

# # Tuples
# worst_gen = ("zoro", "luffy", "law")
# # Unpacking tuple
# (third, first, second) = worst_gen

# print(third)
# print(first)
# print(second)

# #Set
# nicknames = {"akagami", "mugiwara", "big mom"}
# moreNicknames = ["carnibal", "kurohige"]
# nicknames.update(moreNicknames)
# villages = {"Hidden Leaf", "Hidden Sand", "Hidden Rain"}
# print(nicknames)
# nicknames.discard("mugiwara")
# #union to join to sets or use "|"

# goats = nicknames | villages
# print(goats)

# tupleX = (1, 2, 3)
# goats.union(tupleX)

#Intersection would take what's common between the both of them 
# or can use & or intersection_update

# difference would keep items from set1 that ain't in set 2
# could also use "-" or difference_update

# symmetric_differnce keep elements that are not presnt in both sets
# could also use "^" or symmetric_difference_update

#dictionaries
# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "colors": ["red", "white", "blue"]
# }

# print(thisDict["brand"])

# # Making a dictionary
# thisdict = dict(name = "John", age = 36, country = "Norway")
# # print(thisdict)

# x = thisDict.values()
# y = thisDict.keys()
# z = thisDict.items()
# print(z)

# thisDict.update({"year": 2020})
# popitem() to remove last inserted item
# .copy() to copiy items in a dictionary

# Functions

# def my_function(fname):
#     print(fname + " Garcia")

# my_function("Fran")
# my_function("Miguel")

# Classes
# class Person:
#     def __init__(self, name, age): # __init__ function used in making class constructor use self as this in java
#         self.name = name
#         self.age = age
    
#     def __str__(self): # __str__ used for the toString() method
#         return f"The superstar striker {self.name} is {self.age} years old."
    
#     def myfunc(self):
#         print("My name is " + self.name + " i'm too compititive")

# p1 = Person("Mbappe", 26) 

# p1.age = 27

# print(p1)

#File Handling

#modes: r to read, a to append, w to write(overwrite), x to create a new file, t for text, b for binary
file = open("loveiswar.txt")
# dFile = open("C:\Users\myvp1\Documents\CV\summeranime.txt")
# print(file.readlines())
# file.close()
# with open("loveiswar.txt") as f:
#     print(f.read()) # with automatically closes files

with open("loveiswar.txt", "a") as f:
    f.write("\nThe popular romance is back.")

with open("loveiswar.txt") as f:
    print(f.read())

# To delete a file
# import os, os.remove(filename)