# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 16:04:18 2024

@author: SOEE
"""

D={1:'a',2:'b',3:'c',4:'d'}

for key,value in D.items():
    print(f"{key}:\t {value}")
    
    
A = ['a','b','c','d','e']

for i,_ in enumerate(A):
    print(f"{i}:\t {_}")
    
    
# Python list & map structures
customers = [{"name" : "Jeff & Tracy Heaton " , "pets" : ["Wynton","Cricket","Hickory"]},{"name": "John Smith","pets": ["rover"] } ,{"name": "Jane Doe"}]
print(customers)
for customer in customers:
    print( f"{customer['name']} : {customer.get('pets','no pets')}")
    
    
hex_n=0x_400

import sys
sys.version_info
    
a ="Rohan"
def greet(name):
    """This function greets the user with the given name.
    Parameters:
    name (str): The name of the user.
    Returns:
    str: A greeting message.    """
    return f"Hello, {name}! Welcome."
print(help(greet))


with open('shakespeare.txt','r') as f:
    A = f.read()
    B=A.split()
words_count =dict()
for word in B:
    word = word.strip('.,!?').lower()        
    if word:
        # Update word count dictionary
        words_count[word] = words_count.get(word, 0) + 1
   
# Find the maximum count and corresponding word(s)
max_count = max(words_count.values())
max_words = [word for word, count in words_count.items() if count == max_count]    




lst1 = ["Rohan Singh" ,"34","Bhubeneswar"]
lst2 = ["Aman" ,"32","Delhi"]
print("My name is {0[0]} and my age is {0[1]}. I live in {0[2]} wheras my friend's name is {1[0]} and his age is {1[1]}. He lives in {1[2]}".format(lst1,lst2))


f = open('shakespeare.txt')
d=f.read()




f = open('shakespeare.txt')
for line in f:
    print(line)
    
# Alternatively
f = open('shakespeare.txt')
lines=f.readlines()

for line in lines:
    print(line)


lst =[]
# Alternatively
f = open('shakespeare.txt')
for line in f.read():
      print(line)
      #print(line.strip('.,!?').lower())
      #lst.append(line.strip().lower())


import numpy as np
dir(np) # check all the methods in the numpy module
A = np.array([1,2,3]) # Creation of an Array (Vector)
type(A) # numpy.ndarray
A.size # 3 elements
A.shape # (3,) 
A.ndim # 1
A.itemsize # 4
A.dtype # dtype('int32')
A = np.array([1,2,3],dtype='float32')
A.dtype # dtype('int32')
#More than one dimension:
A = np.array([[1,2],[2,4]])
# Altenatively
A = np.array(([1,2],[2,3]),ndmin=2)
# Creation of 3 dimensional Matrix
A = np.array([[[1,2,3],
               [2,3,4],
               [4,5,6]],
              [ [7,8,9],
               [12,13,14],
               [14,15,16]],
              [[27,28,29],
               [22,23,24],
               [24,25,26]]   
              ])    
# For Numpy Array with String

help(np.array)


A =np.arange(3) # array([0, 1, 2])
A = np.arange(1,5) # array([1, 2, 3, 4])
A = np.arange(1,10,2) #  array([1, 3, 5, 7, 9])
A=np.array(range(4)) #  array([0, 1, 2, 3])
A = np.zeros(4) # array([0., 0., 0., 0.])
A = np.zeros((3,4)) #array([[0., 0., 0., 0.],[0., 0., 0., 0.],[0., 0., 0., 0.]])
A = np.zeros((3,4,3)) #array([[0., 0., 0., 0.],[0., 0., 0., 0.],[0., 0., 0., 0.]])
A = np.ones((2, 3, 4), dtype=np.int16)
A= np.empty((2, 3)) # Random elements
A = np.linspace(4, 20, 6) #array([ 4. ,  7.2, 10.4, 13.6, 16.8, 20. ])
A = np.eye(3) #array([[1., 0., 0.], [0., 1., 0.],[0., 0., 1.]])
A = np.diag([1, 2, 3]) # array([[1, 0, 0],[0, 2, 0],[0, 0, 3]])
#Vandermonde matrix useful for Least square
A = np.vander(np.linspace(0, 2, 5), 2)
B =  np.vander([1, 2, 3, 4], 2)
C= np.vander((1, 2, 3, 4), 4)
# Random matrix
rand_gen = np.random.default_rng(42)
A=rand_gen.random((2,3))

z = np.array([i % 4 for i in range(14)])



A = np.arange(5)**2 # array([ 0,  1,  4,  9, 16])
B = A[1:4] # array([1, 4, 9])
A[:5] # array([ 0,  1,  4,  9, 16])
A[:len(A)+1] #array([ 0,  1,  4,  9, 16])
A[0:]  # array([ 0,  1,  4,  9, 16])
A[:-1] #array([0, 1, 4, 9])


A = [[j for j in range(1 + i, 4 + i)] for i in range(0, 9,3)]




for i in range(0, 9,3):
    print(i)


A = np.array([1,2,3])

B= A*3
B
A

A = np.array([[4,5,6],[7,8,9],[10,11,12]])

A[:,1] # array([ 5,  8, 11]) All rows 2nd column
A[1,:] # array([7, 8, 9]) All columns  2nd  row 
A[0:3,0:2] #array([[ 4,  5], [ 7,  8],[10, 11]])


def f(x, y):
    return 10 * x + y


print(f(1,2))


A  = np.arange(0, 7)
print(A)
B = np.arange(7, 0, -1)
print(B)

print(A + B)
print(A * B)
print(A ** B)





rg=np.random.default_rng(42)
A = np.floor(10 * rg.random((3, 4)))



A = np.array([[2,3],[4,5]])
B = np.array([[7,8],[9,10]])
print(np.vstack((A, B)))
print(np.hstack((A, B)))

A = np.array([6, 7])
B = np.array([8, 9])
print(np.column_stack((A, B)))
print(np.vstack((A.T,B.T)))



A = [1,2,3]
B = [4,5,6]
C =np.meshgrid(A,B)
print(C)

C[0][1]


import pandas as pd
A = pd.Series([6, 9, 10, -3])
type(A)
print(A)

A.array
A.values
A.index # RangeIndex(start=0, stop=4, step=1)
# Change the index annotations
A = pd.Series([6, 9, 10, -3], index=["d", "b", "a", "c"])



S = pd.Series([6, 9, 10, -3], index=["d", "b", "a", "c"])

A = pd.Series(range(10))
A



# Dictionary to Pandas Series
A = {"Delhi": 45000, "Mumbai": 75000, "Kolkata": 27000, "Banguluru": 80000}
S = pd.Series(A)
# Back to a dictionary
B = S.to_dict()

# List to Pandas Series
A = list(range(2,10,2))
S = pd.Series(A)
# Back to a List
B = S.to_list()


A = list(range(1,10))

A = np.array(A)
B = A * 2


m = len(A)

E1 =(1/m)*np.sum(np.square(A-B))

E2 = (1/m)*((A-B).dot(A-B))

print(E1 == E2)



D = {"Rohan": 176,"John": 175,"Harvinder": 180,"Hasan": 174} 
S =pd.Series(D) 
print(S)
B= ["Tinku","John","Ramesh","Hasan"] 

S =pd.Series(D, index=B) 

S.isna()

pd.isna(S)

pd.notna(S)


S.iloc[0]


import math
D = {0: 176,1: None , 2: math.nan, 3: '/' } 

S =pd.Series(D) 
print(S)


# Data frame
data = {"City": ["Delhi", "Kolkata", "Mumbai", "Chennai", "Bengaluru", "Gurgaon"],
"year": [2021, 2021, 2021, 2021, 2021, 2020],
"pop": [30, 15, 21, 11, 12, 3.2]}
df = pd.DataFrame(data)


df = pd.DataFrame(np.arange(25).reshape((5, 5)),index=["Rohan", "Mohan", "shyam", "Peter","John"], columns=["one", "two", "three", "four","five"])


df.loc["Rohan"]
df.iloc[0]


df = pd.DataFrame(np.arange(25).reshape((5, 5)))
df = pd.DataFrame(np.arange(25).reshape((5, 5)),columns=["one", "two", "three", "four","five"])
df = pd.DataFrame(np.arange(25).reshape((5, 5)),index=["Rohan", "Mohan", "shyam", "Peter","John"], columns=["one", "two", "three", "four","five"])


df["debt"]=np.arange(5,)


val = pd.Series([4, 5, 7], index=["Rohan", "Mohan", "John"])

df["debt"]=val




populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},"Nevada": {2001: 2.4, 2002: 2.9}}

df = pd.DataFrame(populations)


import tensorflow as tf

help(tf.keras.metrics.mse)


A =np.array(range(25)).reshape(5,5)
df=pd.DataFrame(A)

df

df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),index=["Indore", "Rohtak", "Kasol"])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bcd"),index=["Panipat", "Kurukshetra", "Indore", "Rohtak"])
df1+df2


df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),index=["Indore", "Rohtak", "Kasol"])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),index=["Indore", "Rohtak", "Kasol","Panipat"])
df1+df2


df = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bad"),index=["Indore", "Rohtak", "Kasol"])
print(df.sort_index())
print(df.sort_index(axis="columns"))
print(df.sort_index(axis=1))


df = pd.DataFrame({'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
    'col2': [2, 1, 9, 8, 7, 4],
    'col3': [0, 1, 9, 4, 2, 3],
    'col4': ['a', 'B', 'c', 'D', 'e', 'F']})
# Sort by single
df.sort_values(by=['col1'])
#Sort by multiple columns
df.sort_values(by=['col1','col2'])
#Sort Descending
df.sort_values(by='col1', ascending=False)
#Putting NAs first
df.sort_values(by='col1', ascending=False, na_position='first')
# Sorting with a key function
df.sort_values(by='col4', key=lambda col: col.str.lower())


df = pd.DataFrame(np.random.standard_normal((5, 3)),index=["a", "a", "b", "b", "c"])
df.index.is_unique



df = pd.read_csv("E:\Python Manual\Test_data.csv")
df = pd.read_csv("E:\Python Manual\Test_data.csv",header=None)
df =pd.read_csv("E:\Python Manual\Test_data.csv",names=["Name","Height","Weight","Age"]) # Assigning column names
 # Note: ``index_col=False`` can be used to force pandas to *not* use the first
 # column as the index, e.g. when you have a malformed file with delimiters at
 # the end of each line.
df =pd.read_csv("E:\Python Manual\Test_data.csv",skiprows=[0,2,3])



import requests
url = "https://api.github.com/repos/pandas-dev/pandas/issues"
resp = requests.get(url)
resp.raise_for_status()
resp

data = resp.json()

data[0]["title"]

# Each element in data is a dictionary containing all of the data found on a GitHub
# issue page (except for the comments). We can pass data directly to pandas.Data
# Frame and extract fields of interest:
issues = pd.DataFrame(data, columns=["number", "title","labels", "state"])
issues

 

import sqlite3
query = """CREATE TABLE test(a VARCHAR(20), b VARCHAR(20),c REAL, d INTEGER);"""
con = sqlite3.connect("mydata.sqlite")
con.execute(query)
con.commit()
# insert a few rows of data:
data = [("Atlanta", "Georgia", 1.25, 6),("Tallahassee", "Florida", 2.6, 3),("Sacramento", "California", 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()
# Python SQL drivers return a list of tuples when selecting data from a table:
cursor = con.execute("SELECT * FROM test")
rows = cursor.fetchall()
rows
# You can pass the list of tuples to the DataFrame constructor, but you also need
# the column names, contained in the cursor’s description attribute. Note that for
# SQLite3, the cursor description only provides column names (the other fields,
# which are part of Python’s Database API specification, are None), but for some other
# database drivers, more column information is provided:
cursor.description
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])




df = pd.DataFrame(np.random.standard_normal((7, 3)))
df.iloc[:4,1] = np.nan

df.dropna(thresh=2)



np.random.randint((3,100))




A = [[1,2,3,7],[4,5,6,7],[7,8,9,10]]
B = [[11,12,13],[14,15,16],[17,18,19],[17,18,19]]




def matrix_multiply(A, B):
        n = len(A[0])
        p=len(B)
        if p != n:
            print("Required condition is False")
            return None
        C= [[0 for _ in range(len(B[0]))] for _ in range(len(A))]    

        for i in range(n):
            for j in range(p):
                for k in range(n):
                       C[i][j]+=A[i][k]*B[k][j]

        return C


df = pd.DataFrame(np.random.standard_normal((1000, 4)))
col = df[2]
col[col.abs() > 3]


A = {"one":123,"two":235,"four":231,"five":543}

for i in A.keys():
    print(i)

for i in A.values():
    print(i)


for i,j in A.items():
    print('keys\tValues')
    print(f'{i}:\t{j}')


df = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"], "data1": range(6)})


import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(np.random.standard_normal(50).cumsum(), color="black",linestyle="dashed")
ax1.hist(np.random.standard_normal(100), bins=20, color="black", alpha=0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal
(30))


fig = plt.figure()
ax = fig.add_subplot()
data = np.random.standard_normal(30).cumsum()
ax.plot(data, color="black", linestyle="dashed", label="Default");
ax.plot(data, color="black", linestyle="dashed",drawstyle="steps-post", label="steps-post");
ax.legend()   



class Person:
    
    speed =30
    def fly(speed):        
        print(speed)
        
p = Person()
p.fly()
    



def scale(*arg):
    
     arg = arg ** 2
    
     return arg




class Person:
    
    Name ="John" # Instance Variable
    Age =32
    
    
# Main Function
p = Person()# p is reference to object of class Person
print(p.Name)
print(p.Age)  




class Person:
    
    Name ="John" # Instance Variable
    Age =32
    
    def talk(): 
         print(f"{Name} with age {Age} will talk")


# Main Function
p = Person()# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()


class Person:
    
    Name ="John" # Instance Variable
    Age =32
    
    def talk(): 
        Name ="Mahesh"
        Age =30
        print(f"{Name} with age {Age} will talk")


# Main Function
p = Person()# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()
#Person.talk() takes 0 positional arguments but 1 was given



class Person:
    
    Name ="John" # Instance Variable
    Age =32
    
    def talk(xyz): 
        Name ="Mahesh"
        Age =30
        print(f"{Name} with age {Age} will talk")


# Main Function
p = Person()# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()



class Person:
    
    Name ="John" # Instance Variable
    Age =32
    
    def talk(xyz):  
        print(id(p))
        print(f"{xyz.Name} with age {xyz.Age} will talk")


# Main Function
p = Person()# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()

# class HelloWorld {
#         String name;//Instance Variable
        
#         HelloWorld(){
#         System.out.println(this);
#         }
#     void walk(String name){
#        this.name = name;
#     }
    
    
    
    
    
#     public static void main(String[] args) {
        
#         HelloWorld h =new HelloWorld();
#         h.walk("Ramesh");
#         System.out.println(h.name);
#         System.out.println("Hello, World!");
#         System.out.println(h);
#     }
# }

# With Constructor
# use .__init__() to declare which attributes each instance of the class
#Attributes created in .__init__() are called instance attributes. 
class Person:
    
    def __init__(self,n,a):#constructor or initializer
        self.age=a
        self.Name=n
    
    def talk(self):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk")


# Main Function
p = Person()# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()
#Person.__init__() missing 2 required positional arguments: 'n' and 'a'

# With Constructor
class Person:
    
    def __init__(self,n,a):
        self.Age=a
        self.Name=n
    
    def talk(self):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk")
# Main Function
p = Person("Mahesh",30)# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()
# Every method should have the self which represents the variable belonging to object instance



# With Constructor
class Person:
    
    def __init__(self,n,a):
        self.Age=a
        self.Name=n
    
    def talk(self,n1):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk and his friend is {n1}")
# Main Function
p = Person("Mahesh",30)# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk("joshi")
# Every method should have the self which represents the variable belonging to object instance



# With Constructor
class Person:
    """This is person Class"""
    def __init__(self,n,a,n1):
        self.Age=a
        self.Name=n
        self.n1=n1
    
    def talk(self):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk and his friend is {self.n1}")
# Main Function
p = Person("Mahesh",30,"Joshi")# p is reference to object of class Person
print(id(p))
print(p.Name)
print(p.Age)  
p.talk()
print(dir(p))
print(p.__doc__)
print(p.__class__)
print(p.__dict__)
print(p.__weakref__)
print(p.__sizeof__)
print(p.__repr__)
print(p.__str__)
# Every method should have the self which represents the variable belonging to object instance

# --------------------------------------------------
class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
print(Rodger.attr1)
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
 
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
# ---------------------------------------------------------------------------



#  __repr__ to do this.

# In Python, a special method is a defined function that starts and ends with 
# two underscores and is invoked automatically when certain conditions are met.



# With Constructor
class Person:
    """This is person Class"""
    def __init__(self,n,a,n1):
        self.Age=a
        self.Name=n
        self.n1=n1
    
    def talk(self):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk and his friend is {self.n1}")
# Main Function
p1 = Person("Mahesh",30,"Joshi")
p2 = Person("Timmy",27,"Neena")
print(p1)
print(p2)


# With Wrapper Fucntion (__repr__)

# With Constructor
class Person:
    """This is person Class"""
    def __init__(self,n,a,n1):
        self.Age=a
        self.Name=n
        self.n1=n1
        print(f"{self.Name} with age {self.Age} will talk and his friend is {self.n1}")
    
    def talk(self):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk and his friend is {self.n1}")
        
        
    def __repr__(self):
        return f"{self.Name} with age {self.Age} will talk and his friend is {self.n1}"
        
        
        
        
        
# Main Function
p1 = Person("Mahesh",30,"Joshi")
p2 = Person("Timmy",27,"Neena")
print(p1)
print(p2)


# What is Encapsulation?
# Encapsulation is the process of preventing clients from accessing certain properties, 
# which can only be accessed through specific methods.

# Private attributes are inaccessible attributes, and information hiding is the 
# process of making particular attributes private. You use two underscores to 
# declare private characteristics.

# With Constructor
class Person:
    """This is person Class"""
    def __init__(self,n,a,n1):
        self.Age=a
        self.Name=n
        self.n1=n1
        self.__email="{self.Name}@gmail.com"
        
    
    def talk(self):  
        print(id(self))
        print(f"{self.Name} with age {self.Age} will talk and his friend is {self.n1}")
  
        
        
        
# Main Function
p1 = Person("Mahesh",30,"Joshi")
p2 = Person("Timmy",27,"Neena")
print(p1.__email)



# use getter and setter methods to access private attributes.

# setter method to assign the discount attribute 
#getter function to get the price attribute.

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


single_book = Book('Two States', 1, 'Chetan Bhagat', 200)
bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())
print(single_book)
print(bulk_books)



# Inheritance is regarded as the most significant characteristics of OOP. 
# A class's ability to inherit methods and/or characteristics from another class 
# is known as inheritance.

# The subclass or child class is the class that inherits. The superclass or parent
#  class is the class from which methods and/or attributes are inherited.



class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch



novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)



# What is Polymorphism?
# The term 'polymorphism' comes from the Greek language and means 'something that takes on multiple forms.'

# Polymorphism refers to a subclass's ability to adapt a method that already exists in 
# its superclass to meet its needs. To put it another way, a subclass can use a method 
# from its superclass as is or modify it as needed.


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


# The Book superclass has a specific method called __repr__. This method can be used by
#  subclass Novel so that it is called whenever an object is printed.

# The Academic subclass, on the other hand, is defined with its own __repr__ special 
# function in the example code above. The Academic subclass will invoke its own method 
# by suppressing the same method present in its superclass, thanks to polymorphism.


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)



# What is Abstraction?
# Abstraction isn't supported directly in Python. Calling a magic method, on the other hand,
#  allows for abstraction.

# If an abstract method is declared in a superclass, subclasses that inherit from 
# the superclass must have their own implementation of the method.

# A superclass's abstract method will never be called by its subclasses. But the 
# abstraction aids in the maintenance of a similar structure across all subclasses.

# In our parent class Book, we have defined the __repr__ method. 
# Let's make that method abstract, forcing every subclass to compulsorily have 
# its own __repr__ method.

from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)


# In the above code, we have inherited the ABC class to create the Book class. 
# We've made the __repr__ method abstract by adding the @abstractmethod decorator.

# While creating the Novel class, we intentionally missed the implementation of 
# the __repr__ method to see what happens.


# We get a TypeError saying we cannot instantiate object of the Novel class. 
# Let's add the implementation of the __repr__ method and see what happens now.


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


# Method Overloading
# The concept of method overloading is found in almost every well-known programming
#  language that follows object-oriented programming concepts. It simply refers 
#  to the use of many methods with the same name that take various numbers of 
#  arguments within a single class.

# Let's now understand method overloading with the help of the following code:

class OverloadingDemo:
    def add(self, x, y):
        print(x+y)

    def add(self, x, y, z):
        print(x+y+z)


obj = OverloadingDemo()
obj.add(2, 3)


# TypeError: OverloadingDemo.add() missing 1 required positional argument: 'z'

# You're probably wondering why this happened. As a result, the error is displayed 
# because Python only remembers the most recent definition of add(self, x, y, z), 
# which takes three parameters in addition to self. As a result, three arguments 
# must be passed to the add() method when it is called. To put it another way,
#  it disregards the prior definition of add().

# Thus, Python doesn't support Method Overloading by default.




# Method Overriding
# When a method with the same name and arguments is used in both a derived class 
# and a base or super class, we say that the derived class method "overrides" 
# the method provided in the base class.

# When the overridden method gets called, the derived class's method is always 
# invoked. The method that was used in the base class is now hidden.

class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()


# In the above code, when the call_me() method was called on the child object, 
# the call_me() from the child class was invoked. We can invoke the parent class
# 's call_me() method from the child class using super(), like this:

class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")
        super().call_me()

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()    



class Hello:
    print("Hello")


t =Hello()


#--------------------------------------------------------
#                   Instance Variable (object level)
#---------------------------------------------------------


# 1. instance Variable (object level)

# if values of variable is varied from object to object, they are called:
#     instance variable

# In general, instance varaible are declared inside constructor

# Various place to declare Instance variable
# 1. Inside the constructor
# 2. Inside instance methods using self
# 3. Outside the Class using object reference variable




class Student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    
# Can we assign default values to instance Variables
# yes

class Student:
    
    def __init__(self,name="guest",rollno=0):
        self.name=name
        self.rollno=rollno



class Student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.collegename="KIIT University"

##########################
class Test:
    
    def __init__(self):
        self.a=10
        self.b=23


t = Test()
print(t.__dict__)

# Output {'a': 10, 'b': 23}

###################################
class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        
    def m1(self):
        self.c=21


t = Test()
print(t.__dict__)


# Still Output {'a': 10, 'b': 23}

#####################


class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        
    def m1(self):
        self.c=21


t = Test()
t.m1()
print(t.__dict__)

# Now Output {'a': 10, 'b': 23, 'c': 21}
#################################

# Adding outside the class
class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        
    def m1(self):
        self.c=21


t = Test()
t.m1()
t.d=24
t.e=26
print(t.__dict__)

# {'a': 10, 'b': 23, 'c': 21, 'd': 24, 'e': 26}

##

class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        
    def m1(self):
        self.c=21


t1 = Test()
t2 = Test()
t1.m1()
t2.d=24
t2.e=26
print(t1.__dict__)
print(t2.__dict__)

### Accessing variable outside the class
class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        
    def m1(self):
       print(self.a)
       print(self.b)

t = Test()
t.m1()

print(t.a)
print(t.b)

# How to delete instance variables

# Within class
     #  del self.VariableName

# Outside class
     # del self.OBjectReferenceName.VariableName

########### --Inside class-------------

class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        self.c=10
        self.d=23
    def m1(self):
       del self.a

t = Test()
print(t.__dict__)# nopne is deleted

# Output {'a': 10, 'b': 23, 'c': 10, 'd': 23}
class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        self.c=10
        self.d=23
    def m1(self):
       del self.a

t = Test()
t.m1()
print(t.__dict__)# a is deleted once we called the method
# Output :  {'b': 23, 'c': 10, 'd': 23}

########### -- Outside class-------------
class Test:
    
    def __init__(self):
        self.a=10
        self.b=23
        self.c=10
        self.d=23
    def m1(self):
       del self.a

t = Test()
t.m1()
del t.d# a is deleted
print(t.__dict__)# a is deleted once we called the method
# Output :  {'b': 23, 'c': 10}


#--------------------------------------------------------
#                   Static Variable(class level)
#---------------------------------------------------------


# 2. Static Variable(class level)

# If only one copy is required, then we go for static variable
#only one copy is created and shared to all the object instances

# 1. In general, static variables should be declared within the class
# 2. Inside Constructor and Method using class Name
# 3. Inside class Method by using eithr class name or cls variable
# 4.Inside static method by sing class name
# 5. From Outside, using class Name

# In class
class Student:
    collegename="KIIT University"#Static variable

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

#Inside Constructor
class Student:
    
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.Age =21 # #Instance variable
        Student.collegename="KIIT University"#Static variable
    

# If value of a variable  is not varied from object to objet, only one copy is 
# created


# How to check Output of static variable
class Test:    
    a =10     
print(Test.a) # use direct Class name
print(Test.__dict__) 

######################################
class Test:    
    a =10
    def __init__(self):
        self.a=10 #Instance variable
        Test.b=20 # Static Method
    def m1(self):
        Test.c =30

     
print(Test.a) # use direct Class name
print(Test.__dict__) 
# No b as Object is not declared

########################################
class Test:    
    a =10
    def __init__(self):
        self.a=10 #Instance variable
        Test.b=20 # Satic Method

t=Test()
     
print(Test.a) # use direct Class name
print(Test.__dict__) 
# Now b will be visible as constructor is automatically invoked

## Using Class Method
class Test:    
    a =10
    def __init__(self):
        self.a=10 #Instance variable
        Test.b=20 # Satic Method
    
    def m1(self):
        Test.c =30
# 4.Inside static method by sing class name   
    @classmethod
    def m2(cls):
        Test.d =30
        cls.e=40
# 5. From Outside, using class Name        
    @staticmethod
    def m2():
        Test.f =30

t=Test()
t.m2()     
print(Test.a) # use direct Class name
print(Test.__dict__) 


# How to access Static variable
# We can access static variable by using self,classname,cls and object reference

class Test:
    a=10    
    def __init__(self):
        print(Test.a)
        print(self.a)

t = Test()
print(t.__dict__) # We will Get empty as there is no instance variable


###  

class Test:
    a=10    
    def __init__(self):
        print(Test.a)
        print(self.a)
        
    def m1(self):
        print(self.a)
        print(Test.a)
        
    @classmethod
    def m2(cls):
        print(Test.a)
        print(cls.a)
     
    @staticmethod
    def m3():
        print(Test.a)

t = Test()
t.m1()
t.m2()
t.m3()
print(Test.a)
print(t.__dict__) # We will Get empty as there is no instance variable


# How to update the value of static variable?
#---------------------------------------------


# Either by class Name or cls variable
# We can not use self or object reference to update static variable

class Test:
    a = 10

# Accessing the variable
print(Test.a)
t =Test()
print(t.a)

# uodating the variable name

class Test:
    a = 10
    @classmethod
    def m1(cls):
        cls.a=20
     
    @staticmethod
    def m2():
       Test.a=30
    

Test.m1()
Test.m2()
print(Test.a)


##
class Test:
    a=10
    
    def m1(self):
        self.a=888
        
        
t =Test()
t.m1()
print(Test.a) # 10 
print(t.a)    # 888
# there for static variable is not updated



class Test:
    x = 10    
    def __init__(self):
         self.y=20
        
        
t1=Test()
t2=Test()

print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
#Output
# t1: 10 20
# t2: 10 20

t1=Test()
t2=Test()

t1.x=888
t1.y=999

print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
#Output
# t1: 888 999
# t2: 10 20


t1=Test()
t2=Test()

Test.x=888 # Static variable is changed using class name
t1.y=999

print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)

# t1: 888 999
# t2: 888 20


class Test:
    x = 10    
    def __init__(self):
         self.y=20
         
    def m1(self):
        self.x =888 # instance variable
        self.y =999
        
t1=Test()
t2=Test()     
t1.m1()

print('t1:',t1.x,t1.y)   
print('t2:',t2.x,t2.y) 

# t1: 888 999
# t2: 10 20


class Test:
    x = 10    
    def __init__(self):
         self.y=20
         
    @classmethod
    def m1(cls):
        cls.x =888 # class level variable
        cls.y =999
        
t1=Test()
t2=Test()     
t1.m1()

print('t1:',t1.x,t1.y)   
print('t2:',t2.x,t2.y) 

# t1: 888 20
# t2: 888 20


class Test:
    x = 10    
    def __init__(self):
         self.y=20
         
    @classmethod
    def m1(cls):
        cls.x =888 # class level variable
        cls.y =999
        
t1=Test()
t2=Test()     
t1.m1()

print('t1:',t1.x,t1.y)   
print('t2:',t2.x,t2.y) 
print("Test :", Test.x,Test.y)


# t1: 888 20
# t1: 888 20
# Test : 888 999



#---------------------------------------------------------------
# We can declare static variable : className,cls variable
# We can access static variable: classname,self,object reference
# We can Update static variable :classname,cls variable
#---------------------------------------------------------------



# TO delte static variable
# Anywhere classname.variablename'
#classmethod: del cls.VariableName

class Test:
    a=10
    
    @classmethod
    def m1(cls):
        del cls.a

print(Test.__dict__)# It will not delete

Test.m1()
print(Test.__dict__)# It will delete

## Another example
class Test:
        a=10    
        def __init__(self):
            Test.b=20
            del Test.a
            
            
        def m1(self):
            Test.c=30
            del Test.b
            
            
        @classmethod 
        def m2(cls):
            cls.d=40
            del Test.c
            
    
        @staticmethod 
        def m3():
            Test.e=50
            del Test.d

print(Test.__dict__)# It will not delete as constructor not called
t = Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)

Test.m2()
print(Test.__dict__)


Test.m3()
print(Test.__dict__)

Test.f =50
print(Test.__dict__)

del Test.e
print(Test.__dict__)

del t.f #AttributeError: f


# How to declare Static variable:
#     1. Within class directly
#     2. Inside class method:cls or className
#     3. Remaining places: Using class Name
    
# How to access static variable
#     classname or cls
    
# How to delete static variable:
#     classname or cls
    
# We cannot update/delete static variable by using self or object reference
    

# Insatnce Variable Vs Static variable:
    
    
#     In case of instance variable , for every obeject a seperate copy will be created
#     In case of static variable,only one copy will be created at class level
#     and can be shared by every object of that class.
    





#--------------------------------------------------------
#                   Local variable (Method Level Variable)
#---------------------------------------------------------

# 3. local Variable (Method level)
# To meet temporary requirements, variable declared inside a method is 
# called Local variable
# After Execution, local variable is deleted

# Wes hould not use self and cls for Local variable

# Local variable will be created at time of execution and destroyed once method complete
#Local variable can not be accessed from outside of method 

class Student:
    collegename="KIIT University"#Static variable

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
    def m1(self):
        x=10 # Local variable self is not used
        for i in range(x):
            print(i)

        # i is also local variable
#_-----------------------------------------        

class Test:    
    def m1(self):
        a=100
        print(a)     
        
    def m2(self):
        b=200
        print(b)
        
        
t =Test()        
t.m1() #100
t.m2() #200   
#-------------------------------------------------        
# e.g. Local variable can not be accessed outside method of its scope        
class Test:
    
    def m1(self):
        a=100
        print(a)
        
        
    def m2(self):
        b=200
        print(b)
        print(a)
        
t =Test()        
t.m1()
t.m2()       
        
#-------> NameError: name 'a' is not defined      
        
        
class Test:

        def average(self,list):
            result=sum(list)/len(list) # result is local variable
            print("The Average is:",result)
        
t =Test()
t.average([10,20,30,40])        
        
        
  # Global Keyword      
x=10   # Global variable    
class Test:

        def m1(self):
            print(x)
             
        def m2(self):
            print(x)  
             
             
t =Test()
t.m1() 
t.m2()       
 


x=10   # Global variable    
class Test:
        x=777
        def m1(self):
            x=888
            print(x)
            print(self.x)
             
        def m2(self):
            print(x)  
            print(Test.x) 
             
t =Test()
t.m1() 
t.m2()       


# Global variable can be accessed with global keyword
class Test:
        x=777
        def m1(self):
            global x 
            x=888            
            print(x)
            print(self.x)
             
        def m2(self):
            print(x)  
             
             
t =Test()
t.m1() 
t.m2()       
print(x)
       
        
# Three types of methods

# 1. Instance methods
# 2.Class Methods
# 3.Static Methods


# Instance Variable + Static+variable ----> Instance Method
# Static +local Variable ----> Class Method
#Local Variable ---> Static Method

####################################################

# 1. Instance method (OBJECT RELATED METHOD)

####################################################

# if we are using atleat one instance variable(using static variable or not)
#----------> Instance Method

# the first argument to a method should be self which point to current object

#No decorator required

# To call Instance method
#  1. by self
#  2. by object reference







class Student:
    collegename="KIIT University"#Static variable

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        
     # Instance methods   
    def getStudentInfo(self):
        print("Student name:",self.name)
        print("Student rollno:",self.rollno)

s =Student("Mohan",102)
s.getStudentInfo() # Instance method


# or

class Student:
            def __init__(self,name,marks):
                self.name=name
                self.marks=marks
                
            def display(self):
                print("Hi,", self.name)
                print("Yours Marks are: " ,self.marks)
                
             # Instance methods   
            def grade(self):
                
                if self.marks >=60:
                    print("You got A grade")
                    
                elif self.marks >=50:
                    print("You got B grade")    
                    
                    
                elif self.marks >=40:
                     print("You got C grade")        
                    
                else:
                    print("You are failed")
                    
                    
s =Student("Rohan",90)                    
                    
s.grade()                    
                    
n =int(input("Enter the number of students:"))                    
for i in range(n):
    name=input("Enter student name")
    marks=int(input("Enter student marks"))
    s.display()
    s.grade()
    print("*"*20)
    
    
    
    
    
    
#2. Class Method (CLASS RELATED METHOD)
# if we are not using instance variable but we are using static variables
# -------Class Method
# If you are using static variable(class level variable), then it is 
# CLass Method 

# the first argument to a method should be cls which points to corresponding 
# class object

# Calling instance methd is costly,there for we can make class method'so that 
# static variable can be accessed across all instances of class with cls or classname







class Student:
    collegename="KIIT University"#Static variable
    director ="Nagaur"
    def __init__(self,name,rollno):
        print(id(self))
        self.name=name# Instance Variable
        self.rollno=rollno #instance variable
        
     # Instance methods   
    def getStudentInfo(self):
        print("Student name:",self.name)
        print("Student rollno:",self.rollno)
        
    @classmethod
    def getCollegeInfo(cls):
        print(id(cls))
        print("College Name:",cls.collegename)
        print("Director Name: ",cls.director)
# cls ---> Reference variable to class object
# it is used to make seperate object & Only one time it is created
#class method decorator ,we use this to inform python virtual machine

s =Student("Mohan",102)
s.getStudentInfo() # Instance method using instance variable
print(id(s))

s.getCollegeInfo() 

## ------
@classmethod 
def m1(cls):
    cls.x
    Test.x
        
# cls ---> Special  Reference variable to class object
# it is used to make seperate object & Only one time it is created
#class method decorator ,we use this to inform python virtual machine

####################################################

#3. Static Method  (GENERAL UTILITY METHOD)

#########################################################


# If we are not using any instance method or any static variable, then this 
# it is no way related to object and class & it is general utility method,
# -----> Static Method
# If you are  using only local variable, then it is 
# static method


###############################

class Student:
    collegename="KIIT University" #Static variable
    director ="Nagaur" #Static variable
    def __init__(self,name,rollno):
        print(id(self))
        self.name=name# Instance Variable
        self.rollno=rollno #instance variable
        
     # Instance method   
    def getStudentInfo(self):
        print("Student name:",self.name)
        print("Student rollno:",self.rollno)
        
    @classmethod
    def getCollegeInfo(cls):
        print(id(cls))
        print("College Name:",cls.collegename)
        print("Director Name: ",cls.director)
        
    @staticmethod    #decorator
    def getAverage(a,b,c):
        return (a+b+c)/3


s =Student("Mohan",102)
s.getStudentInfo() # Instance method using instance variable
print(id(s))

s.getCollegeInfo() 
s.getAverage(10,20,30)

Student.getCollegeInfo() 
Student.getAverage(10,20,30)

@staticmethod # Decorator is need
def add(x,y):
    
    print(x+y)


####################################################################

 #-------------Setter and Getter METHOD------------------#
 
# Setter - To set data to object
# gettter -  To get data from object
#IDE is repsonsible for setting the data
 
#######################################################
class Studnet :
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
        
s=Student("Mahesh",80)
#--------------------------
s=Student()
s.setName('Durga')
s.setMarks(100)

print('Student Name:',s.getName())

## Syntax of setter Method
def setVariableName(self,variableName):
            self.variableName=variableName

## Setter 
def setMarks(self,marks):
            self.marks=marks
#Getter method
def getMarks(self,marks):
            self.marks=marks

#############################################
# e.g 1

class Student:
    def setName(self,name):
        self.setName=name
        
    def getName(self,name):
        self.setName=name
    
    def setMarks(self,marks):
        self.marks=marks
    
    
    
    def getMarks(self,marks):
        self.marks=marks



n =int(input("Enter the number of students:"))                    
for i in range(n):
    name=input("Enter student name")
    marks=int(input("Enter student marks"))
    s=Student()
    s.setName(name)
    s.setMarks(marks)
    print(s.name)# Direct access No validation
    print(s.getName)
   
# Can we use setnamemarks(self,name,marks) --- Its not a standard form

# if a person is authenticated , then only he can access
# Ask his name , if it does not matches setName, No access
# Hiding data behind methods ----> Encapsulation

# age
# def setAge(self,age):
#     self.age=age


# ---Instance Methods---------

# Inside constructor , we can not write validation



## instance Vs Class Method

# 1. Inside method body, if we are using alteleast one instance variable, then
# compulsory we should declare that method as instance method

# 2. Inside method body if we are using static variables , then it is highly
# recommend to declare that method as class method.

# 3. TO declare class method, we should use @classmethod decorator 
# and first agrumnet should be cls which is refernce variable to class


# 4 Inside instance method, we can access both static and instance variables.
# Inside class method, we can access only stativ variable 7 we can not access 
# instance variable

# 5. We can call Instance method by using object reference
# We can call class method either by using object reference or by using class name but recommened
# to use classname


class Animal:
    legs=4
    
    @classmethod 
    def walk(cls,name):
        print('{} walks with {} legs'.format(name,cls.legs))

Animal.walk('Dog')
Animal.walk('cat')


# To track number of objects


class Test:
    count=0
    
    def __init__(self):
        Test.count+=1
    
    @classmethod        
    def getNoOfObjects(cls):
        
        print("The number of objects created:",cls.count)
        
t1=Test()
t2=Test()
t3=Test()
t4=Test()

Test.getNoOfObjects()


# Q-- Can I define a method with both self and cls

class Test:
    def m1(cls,self):
        cls.x=10
        print('Instance method:',cls.x,self)
    
t =Test()
t.m1("Durga")  

# Instance method: 10 Durga   


# e.g Same output as above
class Test:
    def m1(self,name):
        self.x=10
        print('Instance method:',self.x,name)
    
t =Test()
t.m1("Durga")    

# Instance method: 10 Durga

# For Static Method (General utility method)
class DurgaMethod:
    @staticmethod 
    def sum(x,y):    
        print("The sum is ",x+y)
    
    @staticmethod 
    def prod(x,y):    
        print("The product is ",x*y)
    
    @staticmethod 
    def average(x,y):    
        print("The average is ",(x+y)/2)
        
DurgaMethod.sum(5,4)    
DurgaMethod.average(5,4)        
    
d =DurgaMethod()   
d.sum(5,4)

# Instance Vs Class Vs Static Method 


# 1. If we are using instance variable inside method body, then we should go for instance method. We
# shuld call using object reference only
# 2. If we are using static variable inside method body, 
# then this method is nowhere is related to a particular object.
# we should declare such type of method as class method.
# We can call by using object reference or by using class name but recommneded to use class name
# 3. If we are not using instance variable and any static variable inside method bosy,
# to definesuch type of general utility methods, we should go for static methods




# Note : If we are not using any decorator :
# -------------------------

# For classmethod @classmethod is mandatory
# For staticmethods, @static methods decorator is optional
# Without any decorator , method can be either instance or static method
# if we are calling by using object reference , it should be instance method
#if we are calling by using class name , there it should be static method

# Example

class Test:
    
    def m1():
        print("Some Method")
        
t = Test()
# upto here is no error
t.m1() #  but here we calling by object reference , so problem arises here
# It will give error
# TypeError: Test.m1() takes 0 positional arguments but 1 was given
# in the above example, Python will consider the method as instance method 
# but we are not declaring self variable.Hence we are getting eror

# e.g 
## Modify it so that no error
class Test:
    
    def m1(self):
        print("Some Method")
        
t = Test()
# upto here is no error
t.m1() 
# Output
#Some Method

# Note to convert it inot static method we need to call it
#by class name

class Test:
    
    def m1():
        print("Some Method")
        
Test.m1()
#Output with no error  is # Some Method



class Test:
    
    def m1(x):
        print('some method',x)
        
t = Test()
t.m1(10)


# TypeError: Test.m1() takes 1 positional argument but 2 were given

# Modify and use class name to acess so no error
class Test:
    
    def m1(x):
        print('some method',x)
        
Test.m1(10)


#############################################
# How to access member of one class into another
##################################################
class Employee:
    def __init__(self,Name,Salary,EmployeeNo):
        self.Name=Name
        self.Salary=Salary
        self.EmployeeNo=EmployeeNo
        
        
    def display(self):
        print('Employee Name:',self.Name)
        print('Employee Salary:',self.Salary)
        print('Employee Number:',self.EmployeeNo)

class Test:
    # Static method 
    def modify(emp):# its passing emp as an object of Employee class.
        emp.Salary=emp.Salary+10000
        emp.display()
# Its not a inheritance concept        
e=Employee("Durga",70000,98765)
Test.modify(e) # Its called by class name therefore it is static method

# Employee Name: Durga
# Employee Salary: 80000
# Employee Number: 98765



# Inner Classes
# 1. The class which is declared inside another class is called inner class.
# 2. Without existing one type of object, if there is no chance of existing another
# type of object , we should go for inner classes.

# eg: 

# Wihout existing Car object, no chane of existing Engine object
# class Car: # Outer class    
#     class Engine: # Inner class

# Wihout existing University object, no chane of existing Department object       
# class University:  # Outer class   
#     class Department: # Inner class

# # Wihout existing Human object, no chane of existing Head object 
# class Human: # Outer class
#     class Head:# Inner class

class Outer:
    
    def __init__(self):
        print('Outer class Object creation......')
        
        
    class Inner:
        def __init__(self):
            print("Inner class object creation")
            
        def m1(self):
            print('Inner class Method')


o =Outer()
# Outer class Object creation......
i =o.Inner()
# Inner class object creation
i.m1()
# Inner class Method

# or in a single line
Outer().Inner().m1()
# Outer class Object creation......
# Inner class object creation
# Inner class Method



class Outer:
    
    def __init__(self):
        print('Outer class Object creation......')
        
    def m2(self):
        print('Outer class Method')
        
        
    class Inner:
        def __init__(self):
            print("Inner class object creation")
            
        def m1(self):
            print('Inner class Method')



o =Outer()
# Outer class Object creation......
i =o.Inner()
# Inner class object creation
i.m1()
# Inner class Method
i.m2() # it will give error
# AttributeError: 'Inner' object has no attribute 'm2'


# Person -- 
#     name
#     date of birth--- DOB()
#           db
#           mm
#           yyyy


class Person:
    
    def __init__(self):
        self.name='Durga'
        self.dob= self.DOB()
        
    def display(self):
        print("Name:",self.name)
        self.dob.display()
        
    class DOB:
        def __init__(self):
            self.dd=15
            self.mm=8
            self.yyyy=1947
            
        def display(self):
            print('DOB ={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
        

p=Person()
p.display()
#Output
# Name: Durga
# DOB =15/8/1947

# =============================================================================
# Example
# =============================================================================



class Person:
    def __init__(self,name,dd,mm,yyyy):        
            self.name =name           
            self.dob = self.DOB(dd,mm,yyyy)
            
    def display(self):
         print("Name:",self.name)
         self.dob.display()
    
    class DOB:
         def __init__(self,dd,mm,yyyy):
             self.dd=dd
             self.mm=mm
             self.yyyy=yyyy
             
         def display(self):
             print('DOB ={}/{}/{}'.format(self.dd,self.mm,self.yyyy))
     

p =Person("Rohan",30,12,1988)
p.display()


# Name: Durga
# DOB =15/8/1947

p.dob.display()

# DOB =30/12/1988


# =============================================================================
# ## -----Three Level----------
# =============================================================================

class Human:
    
    def __init__(self):
        self.name="parveen"
        self.head=self.Head()
        #self.brain=self.Brain()
        
        
    def display(self):
        print('Name',self.name)
        
        self.head.talk()
        self.head.brain.think()
    ##  Inner class
    class Head: 
        def __init__(self):
            self.brain=self.Brain()
        
        def talk(self): 
            print("Talking")  
        
        #Inner to inner class
        
        class Brain:            
            
            def think(self):
                print("Thinking")


h=Human()
h.display()

# Name parveen
# Talking
# Thinking


# =============================================================================
# Nested Method Concept 
# 1. Only in Python ---Not in Java
# =============================================================================


# def m1(): 
#     def m2():
        
# #         xxxxx
# #         xxxxx/1000000 lines of code
# #         xxxxx

#     m2()
#     m2()
#     m2()


class Test:
    
    def m1(self):
        
        def sum(a,b):
            print('*'*20)
            print('First Argument:',a)
            print('Second Argument:',b)
            print('The sum:',a+b)
            print('The product:', a*b)
            
        sum(10,20)
        sum(100,200)
        sum(1000,2000)


t =Test()
t.m1()
# ********************
# First Argument: 10
# Second Argument: 20
# The sum: 30
# The product: 200
# ********************
# First Argument: 100
# Second Argument: 200
# The sum: 300
# The product: 20000
# ********************
# First Argument: 1000
# Second Argument: 2000
# The sum: 3000
# The product: 2000000



# =============================================================================
# Garbage Collection (GC)
# =============================================================================

# To destroy useless objects
# use of del ObjectName
# Based on our requirement , we can enable or disable GC
# Destructor is
        # def __del__() =====> Destructor
        
#         close db cinnection
#         close network connection#         
# Just before destroying an object, GC always calls destructor to perform cleanup
#          
# =========. Java has finalize method............

# =============================================================================
# gc module
# =============================================================================

    # 1. gc.isenabled()
    # 2. gc.isdisabled()
    # 3. gc.enable()

# GC is invoked by Python Virtual Machine
import gc
print(gc.isenabled())
# true
gc.disable()
print(gc.isenabled())
# False
gc.enable()
print(gc.isenabled())
# True


class Test:
    
    def __init__(self):
        print('Object Inialization')
        
    def __del__(self):
        print('FUlfilling clean up ')


t1 =Test()
# Object Inialization
t1=None # Automatically enabled for doing garbage collection but still t1 is in memory only its reference is destroyed
# FUlfilling clean up 
print(t1)
# None ----- Varaible is still present
del t1
print(t1)
# NameError: name 't1' is not defined
import time
time.sleep(10)
print('End of application')

##################################
list =[Test(),Test(),Test()]
time.sleep(10)
list=None
time.sleep(10)
print('End of application')
# Object Inialization
# Object Inialization
# Object Inialization
# FUlfilling clean up 
# FUlfilling clean up 
# FUlfilling clean up 
################################
## To check how many reference variable to current object
t1=Test()
t2=t1
t3=t2
t4=t3
print(sys.getrefcount(t1))

# Object Inialization
# 5


# =============================================================================
# Module 3

# =============================================================================

# Polymorphism
# Duck type philosophy of python
# Overloading
#     operator overloading
#     Method overloading (Not supported in Python & Considers the last method)
#     Constructor overloading (Not supported in Python)
    
# Overriding 
#     Method 
#     Constructor

###-------- Person----------------
# Home
        # class,book,temple,college,milk , butter
        
# Outside of Home
        # brand,cigar,cinema,park,beer
        
# Outside of his native place
        # different colour
        
# Overloading
# --------Operator Overloading
        # 10 +20 =======>30 -------- Addition
        # 'durga' + 'soft'=====> durgasoft --Concatenation

        # 10*3=========>30
        # 'durga'*3====>durgadurgadurga

class Book:
    def __init__(self,pages):
        self.pages=pages
        

b1=Book(100)
b2=Book(200)

print(b1+b2)
# TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
# + support only for string or int object

# operator overloading by using magic methods
# =============================================================================
# __add__(self,other)======> b1=self & b2=other
# __sub__(self,other) +
# __mul__(self,other) *
#__div__(self,other) %
#__mod__(slef,other) | |
#__floordiv__(self,other) //
#__pow__(self,other)  **

# __iadd__() --> +=
# __isub__() --> -=
# __imul__() --> *=
# __idiv__() --> /=
# __imod__() --> %=
# __ifloordiv__() ---> //=
# __ipow__()  ----> **=

# Relational
# >  ---->  __gt__()  Greater than
# >=  ---->  __ge__()  Greater than equal to
# <  ---->  __lt__()  less than
# <=  ---->  __le__()  less than equal to
# != ------> __ne__()  Not equal
# == ------> __eq__() Equal to


# =============================================================================

class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):        
        return self.pages+other.pages
    def __sub__(self,other):
        return self.pages-other.pages
    def __mul__(self,other):
        return self.pages*other.pages
        

b1=Book(100)
b2=Book(200)
b3=Book(700)
print(b1+b2) #300
print(b1+b3) #800
print(b1-b2) #-100
print(b1*b2) #20000




# eg. Method overloading --- but not supported in python
# deposit(cash)
# deposit(cheque)
# deposit(dd)


class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):        
        return self.pages+other.pages
    
    def __str__(self):
        return 'No. of pages: '+ str(self.pages)# If we try print any instances it will print
        

b1=Book(100)
b2=Book(200)
b3=Book(400)

print(b1)
# No. of pages: 100 

# =============================================================================
# To print(b1+b2+b3)
# =============================================================================

class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)        
        return b
    
    

b1=Book(100)
b2=Book(200)
b3=Book(400)
print(b1+b2+b3)
# <__main__.Book object at 0x0000026D7BE79270>

## Add str method to print the number of pages
class Book:
    def __init__(self,pages):
        self.pages=pages
        
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)        
        return b
    
    def __mul__(self,other):
        total=self.pages*other.pages
        b=Book(total)        
        return b
    
    def __str__(self):
        return 'No. of pages: '+ str(self.pages)
    
    

b1=Book(100)
b2=Book(200)
b3=Book(400)
print(b1+b2+b3)
# No. of pages: 700

b4=Book(450)
print(b1+b2+b3+b4)

# No. of pages: 1150
print(b1*b2+b3*b4)
# No. of pages: 200000

# Note
# 1. Whenever we are calling + operator then __add_() method will be called
# + operator return type will become __add_() method return type
# 2. Whenever we are printing any object reference/object, then use __str__ method
# will be called. If we are not providing, otherwise default implementation will be executed


class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
        
s1=Student('Mohan',120)
s2=Student('John',130)

print(s1<s2)
# TypeError: '<' not supported between instances of 'Student' and 'Student'


class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def __lt__(self,other):
        return self.marks<other.marks
        
        
s1=Student('Mohan',120)
s2=Student('John',130)

print(s1<s2)
# True

# ======================================
# 
# =======================================
class Employee:
    def __init__(self,name,salary):
        
        self.name=name
        self.salary=salary
        
class TimeSheet:
    def __init__(self,name,days):        
        self.name=name
        self.days=days


e =Employee('John',10000)
t =TimeSheet('John', 25)

print('The salary is:', e*t)
# TypeError: unsupported operand type(s) for *: 'Employee' and 'TimeSheet'

# Modify it
class Employee:
    def __init__(self,name,salary):
        
        self.name=name
        self.salary=salary
        
    def __mul__(self,other):
        return self.salary*other.days
        
class TimeSheet:
    def __init__(self,name,days):        
        self.name=name
        self.days=days
        
    def __mul__(self,other):
        return self.days*other.salary
        


e =Employee('John',10000)
t =TimeSheet('John', 25)

print('The salary is:', e*t)
# The salary is: 250000

print('The salary is:', t*e)
# The salary is: 250000



# =============================================================================
# Method Overloading 
# Python does not provide support for method/constructor overloading
# =============================================================================
# abs(int)
# abs(long)
# abs(float)


# -- No concept as we dont have any declaration of type (int,float) of objects

class Test:
    def m1(self):
        print('No-arg method')
        
    def m1(self,x):
        print("One arg method")
        
    def m1(self,x,y):
        print("Two arg method")

t=Test()
t.m1()
# TypeError: Test.m1() missing 2 required positional arguments: 'x' and 'y'
t.m1(1,21) # Last method is executed
# Two arg method

# =============================================================================
# 
#Default Arguments
#Variable length Arguments
# =============================================================================
#------------------Default Arguments----------------
class Test:    
    def sum(self,a=None,b=None,c=None):
        if a!= None and b!=None and c!=None:
            print("The sum of three numbers :",a+b+c)            
        elif a!=None and b!=None:
            print("The sum of two numbers :",a+b)            
        else:
            print(("please provide 2 or 3 arguments"))
            
    

t =Test()
t.sum(10,20)
# The sum of two numbers : 30
t.sum(10,20,30)
#The sum of three numbers : 60
t.sum(10)
# please provide 2 or 3 arguments

t.sum(10,0)
# The sum of two numbers : 10


#----------------Variable length Arguments------------

class Test:
    def sum(self,*a):        
        total=0
        for x in a:
            total=total+x
        print('The sum is',total)

t =Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10,20,30,40,50)
# The sum is 30
# The sum is 60
# The sum is 150

t.sum(10,20,'Durga')
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


class Test:
    def m1(self,*a):        
        total=''
        for x in a:
            total=total+x
        print('The concatenation is',total)


t=Test()
t.m1("Durga"," ","software'")

# The concatenation is Durga software'



# =============================================================================
# # Constructor Overloading
# Last constructor will be executed
# =============================================================================


class Test:
    
    def __init__(self):
        print('zero argument constructor')


    def __init__(self,x):
        print('One argument constructor')
    
    
    def __init__(self,x,y):
        print('Two argument constructor')
    
    
    
t =Test()
# TypeError: Test.__init__() missing 2 required positional arguments: 'x' and 'y'
t=Test(1,2)
# Two argument constructor


#----------- Default value Arguments-------------
class Test:    
    def __init__(self,a=None,b=None,c=None):        
        print('Constructor with 0|1|2|3|4')    

t =Test()
t =Test(10)
t =Test(10,20)
t =Test(10,20,30)
# Constructor with 0|1|2|3|4
# Constructor with 0|1|2|3|4
# Constructor with 0|1|2|3|4
# Constructor with 0|1|2|3|4

#---------Variable length arguments--------------
class Test:    
    def __init__(self,*a):        
        print('Constructor with any number of arguments')  
t =Test()
t =Test(10)
t =Test(10,20)
t =Test(10,20,30)
# Constructor with any number of arguments
# Constructor with any number of arguments
# Constructor with any number of arguments
# Constructor with any number of arguments



# =============================================================================
# Method Overriding 
# =============================================================================
# =============================================================================
# Inheritance
# =============================================================================
# class P:
#     10 methods
    
# class C(P):
#     5 More method
# class(P1,P2,P3):

# 1. Code Reusability
# 2. Existing functionality, we can extend


class P:
    def property(self):        
        print('cash+land+gold+power')       
        
    def marry(self):
        print('Subalaxmi')       
    
class C(P):
    pass

c =C()
c.marry()
c.property()
# Subalaxmi
# cash+land+gold+power

# =============================================================================
# # Method Overriding
# It occurs in inheritance and child class method gets preferance
# =============================================================================
class P:
    def property(self):        
        print('cash+land+gold+power')       
        
    def marry(self):
        print('Subalaxmi')       
    
class C(P):
    def marry(self):
        print('Katrina...')


c =C()
c.property()
c.marry()
# cash+land+gold+power
# Katrina...

## Using Both functions
class P:
    def property(self):        
        print('cash+land+gold+power')       
        
    def marry(self):
        print('Subalaxmi')       
    
class C(P):
    def marry(self):
        super().marry()# Access the super class
        print('Katrina...')


c =C()
c.property()
c.marry()
# cash+land+gold+power
# Subalaxmi
# Katrina...


# =============================================================================
# Is A vs Has-A Relationship
# =============================================================================

# =============================================================================
# Composition Vs Aggregation
# =============================================================================
# Husband vs Wife or Boyfriend vs Girlfriend:
# Without you i cannot be

# Without you i cannot be====> Strong Association--- Composition
# Without you I can be (Time pass ) ======> Weak Association --- Aggregation

# University Vs Department============>
# Without University , there is no chance of existing Department
# ========Strong Association (Composition)
# University /Container Object
# Department/Contained object
# University Has-A Department but strong Association

# Department vs Professor =======> 
# Department /Container Object
# Professor/Contained object
# University Has-A Professor but weak association
# ==> Container just hold weak association with contained objects

class Student:
    collegeName='SBM'
    # IT has weak reference to object of student class
    def __init__(self,name):
        self.name=name
# Object and instance variable has strong association--- Composition

print(Student.collegeName) # Without creating student object we can access
# this is called weak assciation
print(s.name) #NameError: name 's' is not defined
# As we need to create an object ,then only we can access
# # this is called strong association or composition class

# =============================================================================
# Types of Inheritance
# 1.Single Inheritance
# 2.Multilevel
# 3.Hierarchical Inheritance
# 4.Multiple Inheritancr
# 5.Hybrid Inheritance
# 6.Cyclic Inheritance
# =============================================================================
# =============================================================================
# ##------------- Single Inheritance-------------
# 
# # Single Parent
# # Single child
# =============================================================================

class P:
    def m1(self):
        print('Parent Method')        
        
class C(P):
    def m2(self):
        print('Child Method')
        
        
c = C()
c.m1()
# Parent Method

# =============================================================================
# # ------- Multilevel Inheritance-------------
# =============================================================================

class P:
    def m1(self):
        print('Parent Method')        
        
class C(P):
    def m2(self):
        print('Child Method')
        
class GC(C):
    def m3(self):
        print('Grand Child Method')


        
gc = GC()
gc.m1()


# =============================================================================
# # -------Hierarchical Inheritance-------------
# 
# # One parent but multiple childs
# =============================================================================


class P:
    def m1(self):
        print('Parent Method')        
        
class C1(P):
    def m2(self):
        print('Child 1 Method')
        
class C2(P):
    def m3(self):
        print('Child 2 Method')


c1 =C1()
c1.m1()
# Parent Method
c2 =C2()
c2.m1()
# Parent Method


# =============================================================================
# #---------------- Multiple Inheritance------------------------
# # Multiple parents but single child
# 
# # Ambiguity or Diamond access proble
# # Output depends upon the order of parents
# =============================================================================

class P1:
    def m1(self):
        print('Parent 1 Method')        
        
class P2:
    def m1(self):
        print('Parent 2 Method')
        
# class C(P):
#     def m3(self):
#         print('Child  Method')

class C(P1,P2):
    pass


c =C()
c.m1()
# Parent 1 Method

# Change order of parents
class P1:
    def m1(self):
        print('Parent 1 Method')        
        
class P2:
    def m1(self):
        print('Parent 2 Method')
        
# class C(P):
#     def m3(self):
#         print('Child  Method')

class C(P2,P1):
    pass

c =C()
c.m1()
# Parent 2 Method


# =============================================================================
# #---------------- Hybrid Inheritance------------------------
# # Single + Multiple + Multilevel + Hierarchical
# # Method Resolution Order
#  
# =============================================================================
class P:
    def m1(self):
        print('Parent Method')
        
class C(P):
    pass

print(C.mro())

# [<class '__main__.C'>, <class '__main__.P'>, <class 'object'>]
# Order is  C ---> P -------> object class


class P:
    def m1(self):
        print('Parent Method')
        
class C(P):
    pass

p =P()
p.m1()

print(P.mro())

# [<class '__main__.P'>, <class 'object'>]
# General approach -- Left to Right

class A:
    def m1(self):
        print('A Class Method')
class B(A):
    def m1(self):
        print('B Class Method')
class C(A):
    def m1(self):
        print('C Class Method')
class D(B,C):
    def m1(self):
        print('D Class Method')
    

print(A.mro())
# [<class '__main__.A'>, <class 'object'>]

print(B.mro())
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>] 
print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

d=D()
d.m1()
# D Class Method
#-----------------------------------
class A:
    def m1(self):
        print('A Class Method')
class B(A):
    pass
class C(A):
    def m1(self):
        print('C Class Method')
class D(B,C):
    def m1(self):
        print('D Class Method')
    
b=B()
b.m1()
# A Class Method


# --------------------------------------------
                  #    o
                  #   -  -
                  # -   -  -
                  # A   B   C
                  # -   -   -
                  #   -   -  -
                  #   X   Y  -
                  #   -   -  -
                  #     -    -
                  #     P- - -



class A : pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass

print(P.mro())
# [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

# Note: For multilevel, there i no guarantee of order 
# C3 Algorithm
# Note:  if Head element of first element not present in the tail part of
# any other list,then consider that element in the result and
# remove that element from all the lists.
# List: ABCDEF
# Head Element : A
# Tail Part : BCDEF

# mro(P) = P + Merge(mro(X),mro(Y),mro(C),XYC)
# XYC is Parents List
# mro(P) = P + Merge(XABO,YBCO,CO,XYC)
# mro(P) = P + Merge(XABO,YBCO,CO,XYC)
#mro(P) = P + X + Merge(ABO,YBCO,CO,YC)
#mro(P) = P + X + A + Merge(BO,YBCO,CO,YC)
# Now is B is present tail part (BCO) of YBCO, there go to next level
#mro(P) = P + X + A + Y+ Merge(BO,BCO,CO,C)
#mro(P) = P + X + A + Y + B + Merge(O,CO,CO,C)
#mro(P) = P + X + A + Y + B + C+ Merge(O,O,O)
# mro(P) = P + X + A + Y + B + C+ O

#-----------------------------------------------------------
class D : pass
class E:pass
class F:pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass

print(A.mro())

# [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]

#---------------- Cyclic Inheritance------------------------
# If a class extends same class

# class A(A):
    
# class A(B)

# class B(A)


########################
# =============================================================================
# Has -A Relationship --Strong ---- Composition
# Is- A relationship --Weak -----Aggregation
# =============================================================================

# =============================================================================
# Super()
# From child class to call parent class memebers
# Code Reusabilty
# =============================================================================

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # 100 Properties like color,weight
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        self.name=name
        self.age=age
        # 100 Properties like color,weight
        self.rollno=rollno
        self.marks=marks
        
class Teacher(Person):
    def __init__(self,name,age,salary,subject):        
        self.name=name
        self.age=age
        # 100 Properties like color,weight
        self.salary=salary
        self.subject=subject
    
    
s = Student("John",21,102,80)
print(s.__dict__)
# {'name': 'John', 'age': 21, 'rollno': 102, 'marks': 80}

t =Teacher('Ramesh',45,10000,'Python')
print(t.__dict__)
# {'name': 'Ramesh', 'age': 45, 'salary': 10000, 'subject': 'Python'}


# We have to write 100 lines of codes for mentionaing the attrivutes
# use Super class--- super().__init__


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # 100 Properties like color,weight
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
class Teacher(Person):
    def __init__(self,name,age,salary,subject):        
        super().__init__(name,age)        
        self.salary=salary
        self.subject=subject
    
s = Student("John",21,102,80)
t =Teacher('Ramesh',45,10000,'Python')

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # 100 Properties like color,weight
    def display(self):    
         print('Name:', self.name)
         print('Age:', self.age)
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Roll No.:', self.rollno)
        print('Marks:', self.marks)       
        
        
class Teacher(Person):
    def __init__(self,name,age,salary,subject):        
        super().__init__(name,age)        
        self.salary=salary
        self.subject=subject
    def display(self):    
        print('Name:', self.name)
        print('Age:', self.age)
        print('salary:', self.salary)
        print('subject:', self.subject) 
    
s = Student("John",21,102,80)
s.display()
# Name: John
# Age: 21
# Roll No.: 102
# Marks: 80
t =Teacher('Ramesh',45,10000,'Python')
t.display()
# Name: Ramesh
# Age: 45
# salary: 10000
# subject: Python

# Here Code reusabilty is not there w.r.t to Method

#%%%%%%%%%%%%%%%%%%%% Modify

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # 100 Properties like color,weight
    def display(self):    
         print('Name:', self.name)
         print('Age:', self.age)
        
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
        
    def display(self):
        super().display()
        print('Roll No.:', self.rollno)
        print('Marks:', self.marks)       
        
        
class Teacher(Person):
    def __init__(self,name,age,salary,subject):        
        super().__init__(name,age)        
        self.salary=salary
        self.subject=subject
    def display(self):    
        super().display()
        print('salary:', self.salary)
        print('subject:', self.subject) 
    
s = Student("John",21,102,80)
s.display()
t =Teacher('Ramesh',45,10000,'Python')
t.display()
# Name: John
# Age: 21
# Roll No.: 102
# Marks: 80
# Name: Ramesh
# Age: 45
# salary: 10000
# subject: Python

#%%%%%%%%%%%%%%%%% LOOP HOLE in super

# A-- B--C--D --E
# which super method is going to execute

class A:
    def m1(self):
        print('A Method')        
        
class B(A):
    def m1(self):
        print('B Method')
        
class C(B):
    def m1(self):
        print('C Method')
class D(C):
    def m1(self):
        print('D Method')
        
class E(D):
    def m1(self):
        print('E Method')

e =E()
e.m1()
# E Method

##########################
class A:
    def m1(self):
        print('A Method')        
        
class B(A):
    def m1(self):
        print('B Method')
        
class C(B):
    def m1(self):
        print('C Method')
class D(C):
    def m1(self):
        print('D Method')
        
class E(D):
    def m1(self):
        super().m1()
        print('E Method')

e =E()
e.m1()

# D Method
# E Method

####################

class A:
    def m1(self):
        print('A Method')        
        
class B(A):
    def m1(self):
        print('B Method')
        
class C(B):
    def m1(self):
        print('C Method')
class D(C):
    def m1(self):
        super().m1()
        print('D Method')
        
class E(D):
    def m1(self):
        super().m1()
        print('E Method')

e =E()
e.m1()

# C Method
# D Method
# E Method

#########################

class A:
    def m1(self):
        print('A Method')        
        
class B(A):
    def m1(self):
        super().m1()
        print('B Method')
        
class C(B):
    def m1(self):
        super().m1()
        print('C Method')
class D(C):
    def m1(self):
        super().m1()
        print('D Method')
        
class E(D):
    def m1(self):
        super().m1()
        print('E Method')

e =E()
e.m1()

# A Method
# B Method
# C Method
# D Method
# E Method
#######################

#2 Ways to call any class

#  1. parentsclassName.methodname(self)




class A:
    def m1(self):
        print('A Method')        
        
class B(A):
    def m1(self):
       
        print('B Method')
        
class C(B):
    def m1(self):        
        print('C Method')

class D(C):
    def m1(self):        
        print('D Method')
        
class E(D):
    def m1(self):
        B.m1(self)
        print('E Method')

e =E()
e.m1()

# B Method
# E Method


# 2.2nd  way --- super(D,self).m1()-- here super of D will be called i.e. C

class A:
    def m1(self):
        print('A Method')        
        
class B(A):
    def m1(self):
       
        print('B Method')
        
class C(B):
    def m1(self):        
        print('C Method')

class D(C):
    def m1(self):        
        print('D Method')
        
class E(D):
    def m1(self):
        super(B,self).m1()
        print('E Method')

e =E()
e.m1()
# A Method
# E Method

# 1. From child class by using super(), we can not call parent
# class instance variable. Use self. only.:
    
# 2. From child class by using super(),we can call parent class
# static variables

#############################

class P:
    a =10
    
    def __init__(self):
        self.b=20
        
class C(P):
    def m1(self):
        print(super().a)
    
c =C()
c.m1()

# 10
############################
class P:
    a =10
    
    def __init__(self):
        self.b=20
        
class C(P):
    def m1(self):
        print(super().b)
    
c =C()
c.m1()
# AttributeError: 'super' object has no attribute 'b'

######################## use self
class P:
    a =10
    
    def __init__(self):
        self.b=20
        
class C(P):
    def m1(self):
        print(self.b)
    
c =C()
c.m1()
# 20


######################## use self and super
class P:
    a =10
    
    def __init__(self):
        self.b=20
        
class C(P):
    def m1(self):
        print(super().a)
        print(self.b)
    
c =C()
c.m1()
# 10
# 20


###### More example

class P:
    
    def __init__(self):
        print('Parent Constructor')
        
    def m1(self):
        print('Parent instance method')
        
    @classmethod 
    def m2(cls):
        print('Parent class Method')
        
    @staticmethod 
    def m3():
        print('Parent static method')
        
        
class C(P):

    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = C()

# Parent Constructor
# Parent instance method
# Parent class Method
# Parent static method


###### 
class P:
    
    def __init__(self):
        print('Parent Constructor')
        
    def m1(self):
        print('Parent instance method')
        
    @classmethod 
    def m2(cls):
        print('Parent class Method')
        
    @staticmethod 
    def m3():
        print('Parent static method')
        
        
class C(P):

    def m4(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()


c = C()
c.m4()
# Parent Constructor
# Parent Constructor
# Parent instance method
# Parent class Method
# Parent static method

l = []
n = int(input('Enter the number of values'))
for i in range(n):
    x=input('Enter value:')
    l.append(int(x))
print(l)

# =============================================================================
# File Handling I/O
# Temporary Storage : List ,Tuple,Dictionary as part of heap
# Permanent Storage: Files, Database concepts, Big Data (Warehouse,cloud)
# e.g 1 lakh customers --go for database
# More than bilion (facebook posts --- Big data concepts

# Files:
#     1. Text File ----> text data like name of students,marks 
#     2. Binary Files ---> Images,video files,audio files
##############################
# 1. Text File ----> text data like name of students,marks 
# Open File
#     Write Operation
#     Read Operation
# f = open(FileName,mode) # f is a object
# Only available for text file
# Mode  -- 
# 1. Read (r), # File not available, then it will give FileNotFound Error
# 2. Write(w), # File not available, then it will create a file & perform overwrite operation
# 3. Append (a) # File not available, then it will create a file & add text
# 4. Read/write (r+) # To read and then write
# 5. Write/read (r+) # To write and read. It will overwrite existing data
# 6. Append/read (a+) # File append and then read. It wont overwrite
# 7. Exclusive (x) 

# it is for write operation
f =open('abc.text','w')
# File may or may not exists
f =open('abc.text','x')
# Compulsory ----> file should not be available
# if abc.txt file is already availabe - File ExistsError

# ++++++++ Default Mode is read mode
# Exmple
# To open abc.txt file as write mode
f =open('abc.text','w')
#############################################
# 2. Binary File-- Only 7 modes are availabe
# rb
# wb
# ab
# r+b
# w+b
# a+b
# xb

# Use Close ---- Judicious use of System Allocated resurces
# f.close()
# =============================================================================
# f is a object and various prpoerties of File Object:
f.name # variable
f.mode # variable
f.closed # variable
f.readable() # Methods
f.writable() # Methods


f =open('abc.txt','w+')
print('File name', f.name)
print('File Mode', f.mode)
print('Is file readable', f.readable())
print('Is file Writeable', f.writable())
print('Is file closed?', f.closed)
f.close()

# Writing Data to File:
       
# f.write(str)
# f.write(list of lines)

# Write one line
f=open('abc.txt','w')
f.write('Let us enjoy learning by Prof. Durga')
f.close()
print('Write operation completed')
## Write two lines
f=open('abc.txt','w')
f.write('Let us enjoy learning by Prof. Durga\n')
f.write('Let us enjoy music by A.R. Rehman\n')
f.close()
print('Write operation completed')

##-----Using List
f=open('abc.txt','w')
f.writelines(['Let us enjoy learning by Prof. Durga\n','Let us enjoy music by A.R. Rehman'])
f.close()
print('Write operation completed')
## Using Tuple
f=open('abc.txt','w')
f.writelines(('Let us enjoy learning by Prof. Durga\n','Let us enjoy music by A.R. Rehman'))
f.close()
print('Write operation completed from Tuple')



############### Important Dynamic reading /Writing
f=open('E:\Python Manual\abc.txt','w')
# It will give error as single backslash(\) is treated as escape character.
# Either use \\ or forward slash

f=open('E:\\Python Manual\\abc.txt','w')
# or f=open('E:/Python Manual/abc.txt','w')
f.writelines(('Let us enjoy learning by Prof. Durga\n','Let us enjoy music by A.R. Rehman'))
f.close()
print('Write operation completed from Tuple')


fname=input('Enter File name:')
f =open('E:\\Python Manual\\'+fname,'w')
data =input('Enter your data')
f.write(data)
f.close()
print('Write operation completed')


# =============================================================================
# reading chracter data from the text files
# =============================================================================
f.read() --> To read total data from file
f.read(n) --> To read n characters from the file
f.readline() --> To read only one line
f.readlines() --> To read all lines into a list















































