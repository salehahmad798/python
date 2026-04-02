# print(12+4/2)


# Assignment operator   


#a = 2

#a= 3 # python resign the data so print 3 reassign variables
#print(a)
# Compound Assignment operator

# +=  Add and assig

"""variables"""

# sher = "harsh bhaiya"

# SheryiansSchool = "students" #pascal case

# sheryiansSchool = "students" #camel case

# sheryians_school = "students" #snake case




"""data types"""

# a = -34

# b = 56.8
# c = 12/3

# v = 34j

# print(type(v))



# st = '1231243235 dsagaiogiaeb !@#$%^&*'

# print(type(st))

# b = True

# t = False

# print(type(b))


"""strings"""

# a = "SHER CODER"


# print(a[::])

# a = 12 

# print(12/3)

# name = "akarsh"
# age = "23"

# print(f"my name is {name} and my age is {age}")

# age = int(input("hello what is your age"))

# print(age)

# a = 5
# b = 32


# print(a + b)
# print(b - a)
# print(a * b)
# print(b//a)
# print(b/a)
# print(5**100)
# print(32%5)


# print(12+4/2)


#assignment operators 

# a = 23

#compound assignmet operations

# a = 20

# a += 20
# a += 40
# a += 60
# a-=
# a*=
# a/=
# a//=
# a**=

# print(a)

# a = 12.1
# b = 12 

# print(a == b)

# print(a != b)

# print(a > b)
# print(45 < 67)
# print(23 >= 23)
# print(45 <= 45)


# print(ord("A"))
# print(ord("B"))

# print("ABC" > "ACD")

# print("A" > 34)

# print(12 >20 and 123 > 100 and 34 == 34 and 45 < 90)

# print(12 !=12 or 23 ==45 or 67 == 56 or 10 > 5)

# print(not 12 == 12)

#IF else 

# a = 6

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")

# money = int(input("please provide me the money :- "))

# if money == 10:
#     print("I will have a choco bar icecream")

# elif money == 20:
#     print("I will have a mangodolly")

# elif money == 30:
#     print("I will have a frosty")
    
# else:
#     print("I will have a cone")

# num1 = int(input("pleae tell your first number "))
# num2 = int(input("pleae tell your second number "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")

# else:
#     print("Both the numbers are same")


# gen = input("please tell your gender as character (M or F):-")

# if gen == 'M' or gen == 'm':
#     print("Good morning SIR")
# elif gen == "F" or gen == 'f':
#     print("Good morning MAM")

# else:
#     print("Unidentified gender")


# num = int(input("please tell your number :- "))

# if num%2 == 0:
#     print("even number")

# else:
#     print("Odd number")

# name = input("please tell your name : - ")
# age = int(input("now tell your age :- "))

# if age >=18 :
#     print(f"hello {name} you are a valid vote")

# else:
#     print(f"hello {name} you are not a valid vote")

# year = int(input("tell your year :- "))

# if year %100 == 0 and year %400 == 0:
#     print("Its a leap year")

# elif  year %100 != 0 and year %4 ==0:
#     print("Its a leap year")

# else:
#     print("its a normal year")

# t = int(input("please tell the temprature :- "))

# if t < 0:
#     print("Freezing cold")

# elif t >= 0 and t <10:
#     print("very cold")

# elif t >= 10 and t <20:
#     print("cold")

# elif t >= 20 and t <30:
#     print("plesant")

# elif t >= 30 and t <40:
#     print("hot")

# else:
#     print("temprature is very hot ")


# print("hello world ")


#For loop

#lets print a table of 5
'''n = int(input("Which table you want ? "))

for i in range(n,(n*10)+1,n): # range is the function with the three argument like start, stop , and step ok
      print(i)'''
''' Line 1 — n = int(input("Which table you want ? "))

input() asks the user to type a number
int() converts their text response into a whole number
That number is stored in n

So if the user types 5, then n = 5.

Line 2 — for i in range(n, (n*10)+1, n):
This is the heart of the code. range() takes 3 arguments here:'''

'''

Argument      Value (if n=5)           Meaning

start          5                       Begin at n
stop           51                     Stop before n×10+1
step           5                       Jump by n each time 

'''
'''
So range(5, 51, 5) gives: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
The +1 in the stop ensures n×10 is included (since range stops before the end value).

Line 3 — print(i)
Simply prints each value of i on a new line.
'''
# a = "SHERYIANS TEACHES INDUSTRY THINGS"
# print(len(a))

# for i in range(len(a)):
#     print(a[i])


#a = "saleh"
#for i in range(len(a)):
 #    print(a[i])

'''for char in a:
    print(char)'''

# a = "SHERYIANS IS COOL"

# for i in a:
#     print(i)


# for i in range(1,21):
#     if i == 56:
#         print("break statement is executed")
#         break
#     print(i)

# else:
#     print("Break statement is not executed")


# n = int(input("please tell your number"))

# for i in range(n):
#     print("hello world ")

# n = int(input("please tell your number "))

# for i in range(1,n+1):
#     print(i)



# n = int(input("please tell your number "))

# for i in range(n,0,-1):
#     print(i)


# n = int(input("which table you want : - "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")


# n = int(input("please tell your number:- "))

# sum = 0 

# for i in range(1,n+1):
#     sum = sum + i


# print(f"your sum is {sum}")


  
# python is runtime language
# Factorial of a number

#

# n = int(input("please tell your number:- "))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i


# print(f"your factorial is {fact}")


# n = int(input("tell your number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i

# print(f"your even and odd sum are {even} , {odd}")


#Print the sum of all even & odd numbers in a range
#separately

# n = int(input("tell your number :-"))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even +i
#     else:
#         odd = odd + i
    
# print(f"your sum of even {even} and your sum of odd {odd}")    
       


# n = int (input("please enter the number :-"))
# count = 0
# for i in range(1 , n+1):
#     if n%i == 0:
#         count = count +1
# if count ==2:
#     print("your number is prime")        
# else:
#     print("your number is non-prime")        

 


# n =int(input("which number factors you want :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("check your number is perfect or not :-"))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i

# if sum == n:
#     print("your number is perfect")
# else:
#     print("not a perfect number")




# n = int(input("check your number is prime or not  :-"))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime")


a = "saleh"
b = ""
# print(a+b) 

for i in range(len(a)-1, -1 , -1):
    # print(a[i])
    b = b + a[i]
print(b)


# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]

# print(b)

# a = "NAMAN"

# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]


# if b == a:
#     print("your string is pallindrome")

# else:
#     print("its not a pallindrome")

# a = "sdfsogn12413@#$%^&U"

# char = 0
# dig = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         dig +=1 
#     elif i.isalpha():
#         char+=1
#     else:
#         spchr +=1 

# print(f"your digits are {dig}\nyour alphabets are {char}\nyour special characters are {spchr}")

# print(dir(str))

# a = 1 

# while a <= 30:
#     print(a)
#     a = a + 1


# a = int(input("tell your number"))

# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# print(rev)


# a = int(input("tell your number"))

# copy = a
# rev = 0

# while a > 0:
#     rev = rev *10 + a % 10
#     a = a //10

# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a pallindromic number")



# import random

# num = random.randint(1,10)

# tries = 0

# while True:
#     guess = int(input("please guess your number between 1 and 10 :- "))
#     if num == guess:
#         tries +=1
#         print(f"you are right you guessed the number is {tries} tries")
#         break

#     elif num < guess:
#         print("go a little lower")
#         tries +=1
    
#     elif num > guess:
#         print("go a little higher")
#         tries +=1

#     else:
#         tries +=1 
#         print("sorry you are wrong")

# print(12)


# def hello():
#     print("this is a hello function so I am doing hello")


# hello()


# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")

# hello(age = 22,name = "akarsh")


# def pallindrome(st):
#     rev = ""
#     for i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]
    
#     if rev == st:
#         print(f"{st} is a pallindrome")
#     else:
#         print(f"{st} is not a not a pallindrome")


# pallindrome("NAMAN")
# pallindrome("CURSOR")

# def hello():
#     return "hello how are you"

# print(hello())


# a = [12,13,14,15,16,34.5]


# #1st way using index

# for i in range(len(a)):
#     print(a[i])

# #2nd way directly on values

# for i in a:
#     print(i)

# l = [-45,67,12,-68,-69,34]

# print("positive elements are ")
# for i in l:
#     if i >= 0:
#         print(i)
# print("negitive elements are")

# for i in l:
#     if i < 0:
#         print(i)

# l = [12,435,67,89,23,25,69]

# sum = 0

# for i in l:
#     sum = sum + i

# print(sum/len(l))





# l = [12,567,43,235,347,568,45,7]

# largest = l[0]
# index = 0

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"your largest number is {largest} at index {index}")


# l = [12,16,13,19,17]

# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i


# print(sec_largest, largest)



# Lists in Python — Complete Beginner's Guide

# What is a List?
# A list is a collection of items stored in a single variable.
# python# Without list — messy!
# student1 = "Ali"
# student2 = "Sara"
# student3 = "Ahmed"

# # With list — clean!
# students = ["Ali", "Sara", "Ahmed"]

# 💡 Think of a list like a shopping list — multiple items, in order, in one place.


# Creating a List
# python# Empty list
# my_list = []

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # List of strings
# fruits = ["apple", "banana", "mango"]

# # List of mixed types
# mixed = [1, "Ali", 3.14, True]

# # List inside a list (nested)
# nested = [[1, 2], [3, 4], [5, 6]]
# ```

# ---

# ## Indexing — Accessing Items

# Every item has a **position number** called an index.
# Index always starts from **0**, not 1.
# ```
# fruits = ["apple", "banana", "mango", "orange"]
# index:       0         1         2        3
# pythonfruits = ["apple", "banana", "mango", "orange"]

# print(fruits[0])   # apple   ← first item
# print(fruits[1])   # banana
# print(fruits[2])   # mango
# print(fruits[3])   # orange  ← last item
# ```

# ### Negative Indexing — Count from the end
# ```
# fruits = ["apple", "banana", "mango", "orange"]
# index:      -4        -3       -2       -1
# pythonprint(fruits[-1])   # orange  ← last item
# print(fruits[-2])   # mango
# print(fruits[-3])   # banana

# Slicing — Getting Multiple Items
# pythonfruits = ["apple", "banana", "mango", "orange", "grape"]
# #           0         1         2        3          4

# # [start : end]  ← end is NOT included
# print(fruits[0:3])    # ['apple', 'banana', 'mango']
# print(fruits[1:4])    # ['banana', 'mango', 'orange']
# print(fruits[0:2])    # ['apple', 'banana']

# # Skip start → from beginning
# print(fruits[:3])     # ['apple', 'banana', 'mango']

# # Skip end → till end
# print(fruits[2:])     # ['mango', 'orange', 'grape']

# # Full copy
# print(fruits[:])      # ['apple', 'banana', 'mango', 'orange', 'grape']

# # Every 2nd item [start:end:step]
# print(fruits[::2])    # ['apple', 'mango', 'grape']

# # Reverse the list
# print(fruits[::-1])   # ['grape', 'orange', 'mango', 'banana', 'apple']

# Modifying a List
# Change an item
# pythonfruits = ["apple", "banana", "mango"]

# fruits[1] = "strawberry"

# print(fruits)   # ['apple', 'strawberry', 'mango']

# List Methods — All the Tools
# Adding Items
# pythonfruits = ["apple", "banana"]

# # append() — add ONE item at the END
# fruits.append("mango")
# print(fruits)   # ['apple', 'banana', 'mango']

# # insert() — add at a SPECIFIC position
# fruits.insert(1, "orange")   # insert at index 1
# print(fruits)   # ['apple', 'orange', 'banana', 'mango']

# # extend() — add MULTIPLE items at the end
# fruits.extend(["grape", "kiwi"])
# print(fruits)   # ['apple', 'orange', 'banana', 'mango', 'grape', 'kiwi']

# Removing Items
# pythonfruits = ["apple", "banana", "mango", "banana"]

# # remove() — removes FIRST match by VALUE
# fruits.remove("banana")
# print(fruits)   # ['apple', 'mango', 'banana']

# # pop() — removes by INDEX (default: last item)
# fruits.pop()       # removes last item
# print(fruits)      # ['apple', 'mango']

# fruits.pop(0)      # removes item at index 0
# print(fruits)      # ['mango']

# # clear() — removes EVERYTHING
# fruits.clear()
# print(fruits)   # []

# # del — delete by index or entire list
# fruits = ["apple", "banana", "mango"]
# del fruits[1]
# print(fruits)   # ['apple', 'mango']

# Searching & Counting
# pythonfruits = ["apple", "banana", "mango", "apple"]

# # index() — find position of item
# print(fruits.index("mango"))    # 2
# print(fruits.index("apple"))    # 0 (first occurrence)

# # count() — how many times item appears
# print(fruits.count("apple"))    # 2
# print(fruits.count("banana"))   # 1

# # in — check if item exists (True/False)
# print("mango" in fruits)        # True
# print("grape" in fruits)        # False

# Sorting & Reversing
# pythonnumbers = [3, 1, 4, 1, 5, 9, 2, 6]

# # sort() — sorts in place (changes original)
# numbers.sort()
# print(numbers)   # [1, 1, 2, 3, 4, 5, 6, 9]

# # sort descending
# numbers.sort(reverse=True)
# print(numbers)   # [9, 6, 5, 4, 3, 2, 1, 1]

# # sorted() — returns NEW sorted list (original unchanged)
# nums = [3, 1, 4, 1, 5]
# new = sorted(nums)
# print(nums)    # [3, 1, 4, 1, 5]  ← unchanged
# print(new)     # [1, 1, 3, 4, 5]  ← new sorted list

# # reverse() — reverses in place
# fruits = ["apple", "banana", "mango"]
# fruits.reverse()
# print(fruits)   # ['mango', 'banana', 'apple']

# Other Useful Methods
# pythonnumbers = [1, 2, 3, 4, 5]

# # len() — how many items
# print(len(numbers))     # 5

# # sum() — total of all numbers
# print(sum(numbers))     # 15

# # min() and max()
# print(min(numbers))     # 1
# print(max(numbers))     # 5

# # copy() — make a copy of list
# original = [1, 2, 3]
# copy = original.copy()
# copy.append(4)
# print(original)   # [1, 2, 3]  ← not affected
# print(copy)       # [1, 2, 3, 4]

# Looping Through a List
# pythonfruits = ["apple", "banana", "mango"]

# # Basic loop
# for fruit in fruits:
#     print(fruit)
# # apple
# # banana
# # mango

# # Loop with index
# for i in range(len(fruits)):
#     print(i, fruits[i])
# # 0 apple
# # 1 banana
# # 2 mango

# # enumerate() — cleaner way to get index + value
# for index, fruit in enumerate(fruits):
#     print(index, fruit)
# # 0 apple
# # 1 banana
# # 2 mango

# List Comprehension — Shortcut to Create Lists
# python# Normal way — 4 lines
# squares = []
# for x in range(1, 6):
#     squares.append(x * x)
# print(squares)   # [1, 4, 9, 16, 25]

# # List comprehension — 1 line!
# squares = [x * x for x in range(1, 6)]
# print(squares)   # [1, 4, 9, 16, 25]
# With condition
# pythonnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Get only even numbers
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)   # [2, 4, 6, 8, 10]

# # Get squares of even numbers
# even_squares = [x*x for x in numbers if x % 2 == 0]
# print(even_squares)   # [4, 16, 36, 64, 100]

# Nested Lists — List inside a List
# python# A 3x3 grid (like a table)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Access items — [row][column]
# print(matrix[0][0])   # 1  (row 0, col 0)
# print(matrix[1][2])   # 6  (row 1, col 2)
# print(matrix[2][1])   # 8  (row 2, col 1)

# # Loop through nested list
# for row in matrix:
#     for item in row:
#         print(item, end=" ")
#     print()
# # 1 2 3
# # 4 5 6
# # 7 8 9

# Common Mistakes Beginners Make
# python# ❌ Mistake 1 — Index out of range
# fruits = ["apple", "banana", "mango"]
# print(fruits[5])   # ERROR! only 0,1,2 exist

# # ✅ Fix — check length first
# if len(fruits) > 5:
#     print(fruits[5])

# # ❌ Mistake 2 — Modifying list while looping
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     numbers.remove(n)   # unpredictable results!

# # ✅ Fix — loop over a copy
# for n in numbers.copy():
#     numbers.remove(n)

# # ❌ Mistake 3 — Copy by assignment (not a real copy)
# a = [1, 2, 3]
# b = a              # b points to SAME list!
# b.append(4)
# print(a)           # [1, 2, 3, 4]  ← a also changed!

# # ✅ Fix — use .copy()
# a = [1, 2, 3]
# b = a.copy()       # real independent copy
# b.append(4)
# print(a)           # [1, 2, 3]     ← a unchanged
# print(b)           # [1, 2, 3, 4]

# Quick Reference Cheat Sheet
# pythonfruits = ["apple", "banana", "mango"]

# # Access
# fruits[0]              # first item
# fruits[-1]             # last item
# fruits[1:3]            # slice

# # Add
# fruits.append("grape")        # add to end
# fruits.insert(1, "orange")    # add at position
# fruits.extend(["kiwi"])       # add multiple

# # Remove
# fruits.remove("banana")       # by value
# fruits.pop()                  # last item
# fruits.pop(0)                 # by index
# fruits.clear()                # all items

# # Search
# fruits.index("mango")         # find position
# fruits.count("apple")         # count occurrences
# "mango" in fruits             # check existence

# # Sort
# fruits.sort()                 # ascending
# fruits.sort(reverse=True)     # descending
# fruits.reverse()              # flip order

# # Info
# len(fruits)                   # count items
# min(fruits)                   # smallest
# max(fruits)                   # largest


# a = [12,13,18,15,16]

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")



# a = (1,2,3,4,5,5,5.5,print(),"hello")


# count = a.count(5)

# print(count)


# a = (1,)

# print(type(a))



# a = {1,8,9,"hello",2,3,4,5}

# for i in a:
#     print(i)

# a = {8,1,2,3,4}

# a.clear()

# print(a)


# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# b -= a

# print(b)

# d = {10:100,20:200,30:300,40:400}

# d[10] = 100 #updating
# d[50] = 500 # creating
# del d[30] # deleting 

# print(d)




# d = {10:100,20:200,30:300,40:400}

# print(d.items())

# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}


# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# d1 = {10:100,20:200,40:300}
# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)


# a = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,7,8]

# d = {}
# for i in a:
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1

# print(d)


# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]



# a = int(input("tell your number :- "))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry there is an err as {err}")

# else:
#     print("good there is no exception")

# finally:
#     print("i will run no matter what")


# print("ok i have done the division")




# age = int(input("tell your age :- "))

# try:

#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")

# except Exception as err:
#     print(f"an error occured as {err}")


# print("the club will start soon")

#File handling

# r = open("superman.txt",'a')

# r.write("and now I am appending some content inside the file  ")

# r.close()

# class Factory:
#     a = 12 # attribute 

#     def hello(self): #method
#         print("how are you")
    


# obj = Factory()

# obj2 = Factory()


# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"your object details are {self.material}, {self.pockets},{self.zips} ")
    


# reebok = Factory("leather",3,2)

# campus = Factory("nylon",3,3)

# reebok.show()

   

# class Animal:
#     name = "lion" #class attribute
    
#     def __init__(self,age):
#         self.age = age #instance attribute
    
#     def show(self):  #instance method
#         print(f"how are you your agger is {self.age}")
    
#     @classmethod
#     def hello(cls):
#         print(f"how are you brother {cls.age}")

#     @staticmethod
#     def static():
#         print("how are you")

   

# obj = Animal(12)

# class Factorymumbai: #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
#     def hello(self):
#         print("hello I am a method mentioned inside Factory")

# class Factorypune(Factorymumbai):   #child class /subclass
#     pass

# obj = Factorymumbai()

# obj2 = Factorypune()

# obj2.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}")
    

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
    
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")


# animal1 = Animal("lion")
# person1 = Human("akarsh",23)

# animal1.show()


# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,name,age):
#         pass

# class Robots(Human,Animal):
#     name3 = "charli123"

# obj = Robots()

# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips 
    

# class BhopalFactory(Factory):
#     def __init__(self, material, zips,color):
#         super().__init__(material, zips)
#         self.color = color
    
# class Punefactory(BhopalFactory):
#     def __init__(self, material, zips, color,pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets


# class Animal:
#     def show(self):
#         print("hello I am akarsh")
    


# class Human(Animal):
#     def show(self):
#         print("how are you")

# obj = Human()
# obj.show()


# class Animal:
#     def show(self):
#         print("I am showing ")

# class Human:
#     def show(self):
#         print("hello I am also showing ")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()


# Modules, Packages & Environments

# 1. Import System
# import
# pythonimport math
# print(math.sqrt(16))  # 4.0
# from
# pythonfrom math import sqrt, pi
# print(sqrt(25))  # 5.0 — no need for math. prefix
# as (aliasing)
# pythonimport numpy as np
# from datetime import datetime as dt

# arr = np.array([1, 2, 3])
# now = dt.now()
# ```

# ### How Python Finds Modules (Search Order)
# ```
# 1. Built-in modules (sys, os, math...)
# 2. Current directory
# 3. PYTHONPATH directories
# 4. Standard library
# 5. Site-packages (installed packages)

# 2. Creating Modules
# A module is simply any .py file.
# mymath.py
# pythonPI = 3.14159

# def area(r):
#     return PI * r * r

# def circumference(r):
#     return 2 * PI * r
# main.py
# pythonimport mymath

# print(mymath.area(5))           # 78.53
# print(mymath.circumference(5))  # 31.41
# ```

# ---

# ## 3. Creating Packages

# A **package** is a folder containing an `__init__.py` file.

# ### Folder Structure
# ```
# myproject/
# │
# ├── main.py
# │
# └── shapes/               ← package
#     ├── __init__.py       ← marks it as a package
#     ├── circle.py
#     └── rectangle.py
# shapes/circle.py
# pythondef area(r):
#     return 3.14 * r * r
# shapes/rectangle.py
# pythondef area(l, w):
#     return l * w
# shapes/__init__.py
# pythonfrom .circle import area as circle_area
# from .rectangle import area as rect_area
# main.py
# pythonfrom shapes import circle_area, rect_area

# print(circle_area(5))    # 78.5
# print(rect_area(4, 6))   # 24

# 4. Virtual Environments
# A virtual environment is an isolated Python setup per project — so packages don't conflict across projects.
# venv (built-in)
# bash# Create
# python -m venv myenv

# # Activate
# myenv\Scripts\activate        # Windows
# source myenv/bin/activate     # Mac/Linux

# # Deactivate
# deactivate
# ```
# ```
# Without venv: all projects share ONE Python + packages (version conflicts!)
# With venv:    each project has its OWN Python + packages (isolated)
# conda (Anaconda)
# bash# Create
# conda create --name myenv python=3.11

# # Activate
# conda activate myenv

# # Deactivate
# conda deactivate

# # List environments
# conda env list
# FeaturevenvcondaBuilt-in✅ Yes❌ Needs installManages Python version❌ No✅ YesManages non-Python deps❌ No✅ YesBest forGeneral PythonData science

# 5. Dependency Management
# pip — Python's package installer
# bashpip install requests              # install
# pip install requests==2.28.0      # specific version
# pip uninstall requests            # remove
# pip list                          # show installed
# pip show requests                 # details about a package
# requirements.txt
# bash# Generate from current environment
# pip freeze > requirements.txt

# # Install from file (share with team / deploy)
# pip install -r requirements.txt
# ```

# **`requirements.txt`**
# ```
# requests==2.28.2
# numpy==1.24.0
# pandas>=2.0.0
# flask
# poetry — Modern dependency manager
# bash# Setup
# pip install poetry
# poetry new myproject     # creates project structure
# poetry add requests      # add dependency
# poetry add pytest --dev  # dev-only dependency
# poetry install           # install all deps
# poetry run python main.py
# pyproject.toml (poetry's config file)
# toml[tool.poetry.dependencies]
# python = "^3.11"
# requests = "^2.28"

# [tool.poetry.dev-dependencies]
# pytest = "^7.0"
# ToolFileBest Forpiprequirements.txtSimple projectspoetrypyproject.tomlProfessional projectscondaenvironment.ymlData science

# 6. Understanding __main__
# The Problem it Solves
# python# greet.py
# def say_hello():
#     print("Hello!")

# say_hello()   # ← runs when imported too! (unintended)
# pythonimport greet  # prints "Hello!" — not what we wanted
# The Fix — if __name__ == "__main__"
# python# greet.py
# def say_hello():
#     print("Hello!")

# if __name__ == "__main__":
#     say_hello()   # only runs when THIS file is executed directly
# pythonimport greet      # now silent — nothing runs unexpectedly
# greet.say_hello() # we control when it runs
# ```

# ### How it works
# ```
# Run directly:   python greet.py  →  __name__ == "__main__"  ✅ block runs
# Imported:       import greet     →  __name__ == "greet"     ❌ block skipped
# Real-world Pattern
# python# app.py

# def process_data(data):
#     return [x * 2 for x in data]

# def main():
#     data = [1, 2, 3, 4, 5]
#     result = process_data(data)
#     print(result)

# if __name__ == "__main__":
#     main()       # Entry point when run directly
# ```

# ---

# ## Full Picture
# ```
# your_project/
# ├── venv/                  ← virtual environment (isolated)
# ├── requirements.txt       ← dependencies list
# ├── main.py                ← entry point (uses __main__)
# └── mypackage/             ← your package
#     ├── __init__.py
#     ├── module1.py
#     └── module2.py
# bash# Typical workflow
# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python main.pymore explaination for each topic step by step i am beginer in python10:23 PMPython Modules, Packages & Environments — Beginner's Guide

# 1. Import System
# What is a Module?
# Think of a module like a toolbox. Python has many ready-made toolboxes you can use.
# python# Without import — you have to write everything yourself
# result = 3.14159 * 5 * 5   # calculating circle area manually
# python# With import — use Python's ready-made tools
# import math
# result = math.pi * 5 * 5   # much easier!

# import — Bring the whole toolbox
# pythonimport math

# print(math.pi)        # 3.141592653589793
# print(math.sqrt(9))   # 3.0
# print(math.ceil(4.2)) # 5

# ✅ You get everything, but must write math. every time.


# from — Pick specific tools from the toolbox
# pythonfrom math import sqrt, pi

# # Now use directly — no need to write math.
# print(sqrt(9))   # 3.0
# print(pi)        # 3.14159...

# ✅ Cleaner code, but only brings what you asked for.


# as — Give it a nickname
# python# "numpy" is long to type every time
# import numpy as np

# # "datetime" is also long
# from datetime import datetime as dt

# # Now use short nicknames
# arr = np.array([1, 2, 3])
# today = dt.now()

# ✅ Used when module names are long or clash with your variable names.


# Common Built-in Modules to Know
# pythonimport math        # sqrt, pi, floor, ceil
# import random      # random numbers
# import os          # file system operations
# import sys         # system-level operations
# import datetime    # dates and times
# import json        # work with JSON data

# # Examples
# import random
# print(random.randint(1, 10))   # random number between 1 and 10

# import datetime
# print(datetime.date.today())   # today's date
# ```

# ---

# ## 2. Creating Your Own Modules

# ### Step 1 — Understand what a module is

# A module is just a **normal `.py` file** you create yourself.
# That's it. Nothing special.
# ```
# myproject/
# ├── calculator.py    ← this IS a module
# └── main.py

# Step 2 — Create the module
# calculator.py
# python# This is your module — just a normal Python file

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero!"
#     return a / b

# PI = 3.14159   # you can also store variables in modules

# Step 3 — Use the module in another file
# main.py
# pythonimport calculator

# print(calculator.add(10, 5))       # 15
# print(calculator.subtract(10, 5))  # 5
# print(calculator.multiply(10, 5))  # 50
# print(calculator.divide(10, 5))    # 2.0
# print(calculator.PI)               # 3.14159

# Step 4 — Import only what you need
# main.py
# pythonfrom calculator import add, multiply

# # No need to write calculator. now
# print(add(3, 4))       # 7
# print(multiply(3, 4))  # 12
# ```

# > 💡 **Why create modules?**
# > - Avoid writing same code again and again
# > - Keep your code organized
# > - Share code between multiple files

# ---

# ## 3. Creating Packages

# ### What is a Package?
# If a **module** is one toolbox, a **package** is a **cabinet full of toolboxes**.
# ```
# One module  =  calculator.py          (single toolbox)
# One package =  shapes/                (cabinet)
#                ├── circle.py          (toolbox 1)
#                ├── rectangle.py       (toolbox 2)
#                └── triangle.py        (toolbox 3)
# ```

# ---

# ### Step 1 — Create the folder structure
# ```
# myproject/
# ├── main.py
# └── shapes/
#     ├── __init__.py      ← IMPORTANT! Makes it a package
#     ├── circle.py
#     └── rectangle.py

# 🔑 The __init__.py file tells Python:
# "Hey! This folder is a package, not just a random folder."
# It can be completely empty — just needs to exist.


# Step 2 — Create files inside the package
# shapes/circle.py
# pythonPI = 3.14159

# def area(radius):
#     return PI * radius * radius

# def circumference(radius):
#     return 2 * PI * radius
# shapes/rectangle.py
# pythondef area(length, width):
#     return length * width

# def perimeter(length, width):
#     return 2 * (length + width)
# shapes/__init__.py
# python# Can be empty, OR you can import here for convenience
# from .circle import area as circle_area
# from .rectangle import area as rect_area

# The . in .circle means "from the same package folder"


# Step 3 — Use the package
# main.py
# python# Method 1 — import the whole sub-module
# from shapes import circle
# print(circle.area(5))          # 78.53

# # Method 2 — import specific function
# from shapes.circle import area
# print(area(5))                 # 78.53

# # Method 3 — use what __init__.py exposed
# from shapes import circle_area, rect_area
# print(circle_area(5))          # 78.53
# print(rect_area(4, 6))         # 24
# ```

# ---

# ## 4. Virtual Environments

# ### The Problem First — Why do we need this?

# Imagine this situation:
# ```
# Project A (old) → needs requests version 1.0
# Project B (new) → needs requests version 3.0

# Without virtual env → only ONE version installed globally
# → One of your projects will BREAK!
# ```
# ```
# With virtual env:
# Project A → has its own isolated Python + requests 1.0  ✅
# Project B → has its own isolated Python + requests 3.0  ✅
# Both work perfectly!

# venv — Built into Python (Recommended for beginners)
# Step 1 — Create a virtual environment
# bashpython -m venv myenv
# This creates a folder called myenv with its own Python inside.
# Step 2 — Activate it
# bash# Windows
# myenv\Scripts\activate

# # Mac / Linux
# source myenv/bin/activate
# ```

# After activation you'll see this in your terminal:
# ```
# (myenv) C:\myproject>     ← the (myenv) shows it's active
# Step 3 — Install packages (they go INTO the env)
# bashpip install requests
# pip install numpy
# Step 4 — Deactivate when done
# bashdeactivate

# conda — Popular in Data Science
# bash# Step 1 — Create (also lets you choose Python version)
# conda create --name myenv python=3.11

# # Step 2 — Activate
# conda activate myenv

# # Step 3 — Install packages
# conda install numpy pandas

# # Step 4 — Deactivate
# conda deactivate
# ```

# ---

# ### venv vs conda — Which to use?
# ```
# Learning Python?          → use venv (simpler, built-in)
# Data science / ML / AI?   → use conda (manages more things)

# 5. Dependency Management
# What is a Dependency?
# Any package your project needs to run is a dependency.
# pythonimport requests   # your project DEPENDS on this package
# import numpy      # and this one too

# pip — The Package Installer
# bash# Install a package
# pip install requests

# # Install a specific version
# pip install requests==2.28.0

# # Install minimum version
# pip install requests>=2.0.0

# # Uninstall
# pip uninstall requests

# # See all installed packages
# pip list

# # See details about one package
# pip show requests

# requirements.txt — Your Project's Shopping List
# This file lists every package your project needs.
# When someone else gets your project, they install everything in one command.
# Step 1 — Create it automatically
# bashpip freeze > requirements.txt
# ```

# **What it looks like inside:**
# ```
# requests==2.28.2
# numpy==1.24.0
# pandas==2.0.1
# flask==2.3.0
# Step 2 — Install from it (on a new machine or for a teammate)
# bashpip install -r requirements.txt

# poetry — Professional Dependency Manager
# Better than pip for larger projects. Handles everything automatically.
# bash# Step 1 — Install poetry
# pip install poetry

# # Step 2 — Create a new project
# poetry new myproject

# # Step 3 — Add packages
# poetry add requests      # regular dependency
# poetry add pytest --dev  # only needed for development/testing

# # Step 4 — Install all dependencies
# poetry install

# # Step 5 — Run your project
# poetry run python main.py
# Poetry creates pyproject.toml automatically:
# toml[tool.poetry.dependencies]
# python = "^3.11"
# requests = "^2.28"

# [tool.poetry.dev-dependencies]
# pytest = "^7.0"
# ```

# ---

# ### pip vs poetry — Which to use?
# ```
# Small project / learning?   → pip + requirements.txt (simpler)
# Serious / team project?     → poetry (handles everything better)

# 6. Understanding __main__
# The Problem — A Story
# You write a file with useful functions AND some test code:
# greet.py
# pythondef say_hello(name):
#     print(f"Hello, {name}!")

# # You test it here
# say_hello("Ali")    # prints: Hello, Ali!
# Now your friend imports your module in their project:
# friend.py
# pythonimport greet    # "Hello, Ali!" prints automatically — UNWANTED!

# greet.say_hello("Sara")   # Hello, Sara!

# ❌ The test code ran automatically when imported — not good!


# The Solution — if __name__ == "__main__"
# greet.py
# pythondef say_hello(name):
#     print(f"Hello, {name}!")

# # This block ONLY runs when YOU run this file directly
# if __name__ == "__main__":
#     say_hello("Ali")
# friend.py
# pythonimport greet    # nothing prints automatically now ✅

# greet.say_hello("Sara")   # Hello, Sara!

# How does __name__ work?
# python# Every Python file has a __name__ variable
# # Its value depends on HOW the file is run

# # Run directly:  python greet.py   →  __name__ = "__main__"
# # Imported:      import greet      →  __name__ = "greet"
# ```
# ```
# python greet.py
#        ↓
# Python sets __name__ = "__main__"
#        ↓
# if "__main__" == "__main__" → TRUE → block runs ✅

# import greet
#        ↓
# Python sets __name__ = "greet"
#        ↓
# if "greet" == "__main__" → FALSE → block skipped ❌

# Real World Example
# python# student.py

# def get_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     else:
#         return "F"

# def print_result(name, score):
#     grade = get_grade(score)
#     print(f"{name} scored {score} → Grade: {grade}")

# # Only runs when this file is executed directly
# if __name__ == "__main__":
#     print_result("Ali", 95)      # A
#     print_result("Sara", 82)     # B
#     print_result("Ahmed", 60)    # F
# bashpython student.py
# # Ali scored 95 → Grade: A
# # Sara scored 82 → Grade: B
# # Ahmed scored 60 → Grade: F
# python# another_file.py
# from student import get_grade    # imports cleanly, nothing prints

# score = get_grade(88)
# print(score)    # B

# Full Beginner Workflow — Put It All Together
# bash# 1. Create your project folder
# mkdir myproject
# cd myproject

# # 2. Create virtual environment
# python -m venv venv

# # 3. Activate it
# source venv/bin/activate       # Mac/Linux
# venv\Scripts\activate          # Windows

# # 4. Install packages you need
# pip install requests

# # 5. Save dependencies
# pip freeze > requirements.txt

# # 6. Write your code
# # create modules, packages, use __main__

# # 7. Run your project
# python main.py

# # 8. When done
# deactivate
# ```

# ### Project Structure (Best Practice)
# ```
# myproject/
# ├── venv/                  ← virtual environment (don't touch)
# ├── requirements.txt       ← package list
# ├── main.py                ← your entry point
# └── mypackage/             ← your package
#     ├── __init__.py
#     ├── helpers.py
#     └── calculator.py

# 💡 Golden Rules for Beginners

# Always use a virtual environment per project
# Always save deps with pip freeze > requirements.txt
# Always use if __name__ == "__main__" in your scripts
# One module = one responsibility (don't put everything in one file)




# class Factory:
#     __a = "pune"

#     def show(self):
#         print(Factory.__a)


# obj = Factory()

# obj.show()


# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")



# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")

# obj = Circle(7)
# obj2 = Square(12)


# class Animal:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age

#         return f"your sum of ages are {self.age + sum}"

# obj = Animal("lion",12)
# obj2 = Animal("dolphin",14)
# obj3 = Animal("tiger",34)

# print(obj + (obj2,obj3))


# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")
    
# obj = Animal()

# obj.show



# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper


# @decorate
# def addition(a,b):
#     print(f"your total is {a + b} ")

# addition(12,67)


# def information(**kwargs):
#     print("your information is\n\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")
    



# information(name = "Akarsh", age = 23, designation = "AI/ML")

# l = {i : i**2 for i in range(1,10)}

# print(l)

# a = [1,2,3,4,5]

# def double(x):
#     return x *2

# result = map(double,a)

# print(list(result))

# from modelss.model import hello,maths

# a = int(input("how many rows you  want "))

# for i in range(1,a + 1):
#     for j in range(i):
#         print("* ",end = "")
#     print()

# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print("  ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()



# n = int(input("tell how many rows you want"))

# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()


# for i in range(n-1,0,-1):
#     for j in range(n-i):
#         print(" ",end = "")
#     for k in range(i):
#         print("* ",end = "")
#     print()

# a = 1234
# copy = a
# sum = 0

# while a > 0:
#     z = a %10
#     fact = 1 
#     for i in range(1,z+1):
#         fact = fact * i
    
#     sum = sum + fact
#     a = a//10 

# if sum == copy:
#     print("this is a strong number ")
# else:
#     print("not a strong number")


# for j in range(2,21):
#     a = j

#     for i in range(2,(a//2)+1):
#         if a % i == 0:
#             break

#     else:
#         print(a)



# a = [1,1,1,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5]
# count = 0
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] +=1 
#     else:
#         dict[i] = 1
# max = 0
# for i in dict.values():
#     if i > max:
#         max = i
# for i in dict:
#     if dict[i] == max:
#         print(f"{i} occured {max} times and that is largest occurence")
#         break

