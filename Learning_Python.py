# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 16:42:12 2024

@author: SOEE
"""
# =============================================================================
# Keyword
# =============================================================================
# 33 Keyword
# True,False,None
#  and, or ,not,is
#  if,elif,else
#  while,for,break,continue,return,in,yield
#  try,except,finally,raise,assert
#  import,from,as,class,def,pass,global,nonlocal,lambda,del,with

import keyword
keyword.kwlist

# =============================================================================
# DataType
# =============================================================================
# Python contains the following inbuilt data types
# 1. int
# 2. float
# 3.complex
# 4.bool
# 5.str
# 6.bytes
# 7.bytearray
# 8.range
# 9.list
# 10.tuple
# 11.set
# 12.frozenset
# 13.dict
# 14.None


''' Fundamental Data types
int
float
complex
bool
str
'''
# In Python,we can represent char values also by using str type and explicitly char type is
# not available.
# =============================================================================
# int
# =============================================================================


# Python contains several inbuilt functions
# 1.type()
#  to check the type of variable
# 2. id()
#  to get address of object


# Same address but a & b are different references
a=10
b=10
print(id(a))
print(id(b))

# 2189509460496
# 2189509460496

# Now a 's name is same and it pointing to two different objects
a = 10
print(id(a))
# 2189509460496
a = 20
print(id(a))
# 2189509460816


# In Python2 we have long data type to represent very large integral values.
# But in Python3 there is no long type explicitly and we can represent long values also by
# using int type only.


# int values in the following ways
# 1. Decimal form
# 2. Binary form
# 3. Octal form
# 4. Hexa decimal form


# Binary form(Base-2):
# The allowed digits are : 0 & 1
# Literal value should be prefixed with 0b or 0B
# Eg: 
a = 0B1111
#a = 0B123 #Error
# a= b111 # Error

# Octal Form(Base-8):
# The allowed digits are : 0 to 7
# Literal value should be prefixed with 0o or 0O.
a=0o123
# a=0o786 SyntaxError: invalid digit '8' in octal literal


# Hexa Decimal Form(Base-16):
# The allowed digits are : 0 to 9, a-f (both lower and upper cases are allowed)
# Literal value should be prefixed with 0x or 0X
# Eg:
a =0XFACE #64206
a=0XBeef #48879
# a =0XBeer SyntaxError: invalid hexadecimal literal

# Being a programmer we can specify literal values in decimal, binary, octal and hexa
# decimal forms. But PVM will always provide values only in decimal form


# =============================================================================
# # Base Conversions
# =============================================================================
# 1.bin():
# We can use bin() to convert from any base to binary
# Eg:
bin(15)
# '0b1111'
bin(0o11)
#'0b1001'
bin(0X10)
#'0b10000' 


# oct():
# We can use oct() to convert from any base to octal
oct(10)
#'0o12'
oct(0B1111)
#'0o17'
oct(0X123)
#'0o443'

# hex():
# We can use hex() to convert from any base to hexa decimal
# Eg:
hex(100)
#'0x64'
hex(0B111111)
#'0x3f'
hex(0o12345)
#'0x14e5' 
# =============================================================================
# float data type:
# =============================================================================
# We can use float data type to represent floating point values (decimal values)
f=1.234
type(f) 
# float
# We can also represent floating point values by using exponential form (scientific notation)
f=1.2e3
print(f) 
#1200.0
# -------------------------------
# instead of 'e' we can use 'E'
# We can represent int values in decimal, binary, octal and hexa decimal forms. But we can
# represent float values only by using decimal form.
# --------------------------------
#f=0B11.01  #SyntaxError: invalid syntax
 

# =============================================================================
# # Complex Data Type:
# =============================================================================
# In the real part if we use int value then we can specify that either by decimal,octal,binary
# or hexa decimal form.
# But imaginary part should be specified only by using decimal form.
3+5j
10+5.5j
0.5+0.1j

a=10+1.5j
b=20+2.5j
c=a+b
print(c)


c=10.5+3.6j
c.real #==>10.5
c.imag #==>3.6


# =============================================================================
# bool data type:
# =============================================================================
# We can use this data type to represent boolean values.
# The only allowed values for this data type are: True and False
# Internally Python represents True as 1 and False as 0
b=True
type(b) #=>bool


a=10
b=20
c=a<b
print(c)#==>True
True+True  # ==>2
True-False #==>1


# =============================================================================
# String Data Type
# =============================================================================
#str represents String data type.
#A String is a sequence of characters enclosed within single quotes or double quotes.
s1='John'
s1="Malik"
#By using single quotes or double quotes we cannot represent multi line string literals.
# s1="Parveen 
#             malik"
            
# SyntaxError: unterminated string literal (detected at line 1)            
 

# For this requirement we should go for triple single quotes(''') or triple double quotes(""")
s1='''Java and
 Python'''
s1="""Java
 Python"""
# # We can also use triple quotes to use single quote or double quote in our String.
''' This" is character'''
' This is " Character '
# # We can embed one string in another string
'''This "Python class very helpful" for java students'''


# Slicing of Strings:
# slice means a piece
# [] operator is called slice operator,which can be used to retrieve parts of String.
# In Python Strings follows zero based index.
# The index can be either +ve or -ve.
# +ve index means forward direction from Left to Right
# -ve index means backward direction from Right to Left
s="Timmy"
s[0]
s[1]
s[-1]
s[40] # -------> IndexError: string index out of range

s[1:40]
s[1:]
s[:4]
s[:]
s*3
len(s)



# =============================================================================
# Type Casting
# =============================================================================
'''We can convert one type value to another type. This conversion is called Typecasting or
Type coersion.
The following are various inbuilt functions for type casting.
1. int()
2. float()
3. complex()
4. bool()
5. str()
We can convert from any type to int except complex type.
2. If we want to convert str type to int type, compulsary str should contain only integral
value and should be specified in base-10
'''
int(123.987) 
int(10+5j) 
int(True) 
int(False)
int("10")
int("ten") #ValueError: invalid literal for int() with base 10: 'ten'


float(10)
float(10+5j) 
float(True)
float("10")
float(10)
float("ten") 
float(0B1111) #-------------->15.0
float("0B1111") 


'''complex(x)
We can use this function to convert x into complex number with real part x and imaginary
part 0.'''
complex(10)
complex(10.5)
complex(True) #==>1+0j
complex(False)#==>0j
complex("10")#==>10+0j
complex("10.5") #==>10.5+0j
complex("ten") # ValueError: complex() arg is a malformed string 


''''complex(x,y)
We can use this method to convert x and y into complex number such that x will be real
part and y will be imaginary part.'''

complex(10,-2) #==>10-2j
complex(True,False) #==>1+0j



'''bool():
We can use this function to convert other type values to bool type.'''

bool(0)  #==>False
bool(1)  #==>True
bool(10) #===>True
bool(10.5) #===>True
bool(0.178) #==>True
bool(0.0) #==>False
bool(10-2j) #==>True
bool(0+1.5j) #==>True
bool(0+0j)#==>False
bool("True")#==>True
bool("False")#==>True
bool("")#==>False  # X is empty string so result is false


'''str():
We can use this method to convert other type values to str type'''

str(10)  #'10'
str(10.5) #'10.5'
str(10+5j) #'(10+5j)'
str(True) #'True'


# =============================================================================
# Fundamental Data Types vs Immutability:
# All Fundamental Data types are immutable. i.e once we creates an object,we cannot
# perform any changes in that object. If we are trying to change then with those changes a
# new object will be created. This non-chageable behaviour is called immutability.
# =============================================================================

# In Python if a new object is required, then PVM wont create object immediately. First it
# will check is any object available with the required content or not. If available then
# existing object will be reused. If it is not available then only a new object will be created.
# The advantage of this approach is memory utilization and performance will be improved.
# But the problem in this approach is,several references pointing to the same object,by
# using one reference if we are allowed to change the content in the existing object then the
# remaining references will be effected. To prevent this immutability concept is required.
# According to this once creates an object we are not allowed to change content. If we are
# trying to change with those changes a new object will be created.


a=10
b=10
a is b
#True
id(a)
# 2189698730064
id(b)
# 2189698730064

a=10+5j
b=10+5j
a is b
#False
id(a)
# 2189698730032
id(b)
# 2189698729264


a=True
b=True
a is b
#True
id(a)
# 140720224880848
id(b)
# 140720224880848

a='John'
b='John'
a is b
# True
id(a)
# 2188287793200
id(b)
# 2188287793200


# =============================================================================
# bytes Data Type:
# bytes data type represens a group of byte numbers just like an array.
# =============================================================================
x = [10,20,30,40]
b = bytes(x)
type(b)#==>bytes
print(b[0])#==> 10
print(b[-1])#==> 40
for i in b : print(i)


# Conclusion 1:
# The only allowed values for byte data type are 0 to 256. By mistake if we are trying to
# provide any other values then we will get value error.
# Conclusion 2:
# Once we creates bytes data type value, we cannot change its values,otherwise we will get
# TypeError.
# Eg:
x=[10,20,30,40]
b=bytes(x)
b[0]=100 # TypeError: 'bytes' object does not support item assignment 


# =============================================================================
# bytearray Data type:
# bytearray is exactly same as bytes data type except that its elements can be modified.
# =============================================================================
# Eg 
x=[10,20,30,40]
b = bytearray(x)
for i in b : print(i)
# Modify
b[0]=100
for i in b: print(i) 


# =============================================================================
# List
# =============================================================================
'''list data type:
If we want to represent a group of values as a single entity where insertion order required
to preserve and duplicates are allowed then we should go for list data type.
1. insertion order is preserved
2. heterogeneous objects are allowed
3. duplicates are allowed
4. Growable in nature
5. values should be enclosed within square brackets.
Note: An ordered, mutable, heterogenous collection of eleemnts is nothing but list, where
duplicates also allowed.'''

list=[10,10.5,'John',True,10] 

print(list) # [10,10.5,'durga',True,10] 

list=[10,20,30,40]
list[0]

list[-1]

list[1:3]

list[0]=100
for i in list:print(i) 

 # list is growable in nature. i.e based on our requirement we can increase or 
 # decrease the size.
list=[10,20,30]
list.append("DINO")
list.remove(20)
list2=list*2

# =============================================================================
# Tuple
# =============================================================================
'''tuple data type:
tuple data type is exactly same as list data type except that it is immutable.i.e we cannot
chage values.
Tuple elements can be represented within parenthesis.
Note: tuple is the read only version of list'''


t=(10,20,30,40)
type(t)

t[0]=100 # TypeError: 'tuple' object does not support item assignment
t.append("mjk;") # AttributeError: 'tuple' object has no attribute 'append'
t.remove(10)



# =============================================================================
# Range
# =============================================================================

'''
range Data Type:
range Data Type represents a sequence of numbers.
The elements present in range Data type are not modifiable. i.e range Data type is
immutable.'''

range(10)

range(10,20)


r = range(10,20)
for i in r : print(i)

range(10,20,2)

r = range(10,20,2)
for i in r : print(i) 

# We can access elements present in the range Data Type by using index.
r=range(10,20)
r[0] #==>10
r[15] #==>IndexError: range object index out of range
#We cannot modify the values of range data type

r[0]=100
# TypeError: 'range' object does not support item assignment
# We can create a list of values with range data type

lst = list(range(10)) 

# =============================================================================
# Set    
# =============================================================================
''' set Data Type:
If we want to represent a group of values without duplicates where order is not important
then we should go for set Data Type.
1. insertion order is not preserved
2. duplicates are not allowed
3. heterogeneous objects are allowed
4. index concept is not applicable
5. It is mutable collection
6. Growable in nature'''

s={100,0,10,200,10,'durga'}
s
s[0] #==>TypeError: 'set' object does not support indexing

'''set is growable in nature, based on our requirement we can increase or 
decrease the size.'''
s.add(60)
s

s.remove(100)
s

# =============================================================================
# Frozen Set
# =============================================================================
'''frozenset Data Type:
It is exactly same as set except that it is immutable.
Hence we cannot use add or remove functions.'''
s={10,20,30,40}
fs=frozenset(s)
type(fs)
fs
frozenset({40, 10, 20, 30})
for i in fs:print(i)
fs.add(70) # AttributeError: 'frozenset' object has no attribute 'add'
fs.remove(10) # AttributeError: 'frozenset' object has no attribute 'remove' 



# =============================================================================
# Dictionary 
# =============================================================================

'''dict Data Type:
If we want to represent a group of values as key-value pairs then we should go for dict
data type.
Eg:
d={101:'Tim',102:'ravi',103:'shiva'}
Duplicate keys are not allowed but values can be duplicated. If we are trying to insert an
entry with duplicate key then old value will be replaced with new value.
Note: dict is mutable and the order wont be preserved.'''

d={101:'durga',102:'ravi',103:'shiva'}
d[101]='sunny'
d
'''We can create empty dictionary as follows'''
d={ }
''' We can add key-value pairs as follows'''
d['a']='apple'
d['b']='banana'
print(d) 





'''Note:
1. In general we can use bytes and bytearray data types to represent binary information
like images,video files etc
2. In Python2 long data type is available. But in Python3 it is not available and we can
represent long values also by using int type only.
3. In Python there is no char data type. Hence we can represent char values also by using
str type'''
# =============================================================================
# None Data Type:
# =============================================================================
'''None means Nothing or No value associated.
If the value is not available,then to handle such type of cases None introduced.
It is something like null value in Java.'''
# Eg:
def m1():
    a=10
print(m1())
 
#None


'''Escape Characters:
In String literals we can use esacpe characters to associate a special meaning.'''
s="Tiimy\nMeeting"
print(s)

s="Ramesh\tRunning"
print(s)

# s="This is " symbol"  #SyntaxError: invalid syntax

s="This is \" symbol"
print(s) # This is " symbol 


'''The following are various important escape characters in Python
1) \n==>New Line
2) \t===>Horizontal tab
3) \r ==>Carriage Return
4) \b===>Back space
5) \f===>Form Feed
6) \v==>Vertical tab
7) \'===>Single quote
8) \"===>Double quote
9) \\===>back slash symbol'''


# =============================================================================
# Constants:
# =============================================================================
'''Constants concept is not applicable in Python.
But it is convention to use only uppercase characters if we don’t want to change value.
It is just convention but we can change the value.
'''

MAX_VALUE=10


# =============================================================================
# Operators
# =============================================================================
'''Operator is a symbol that performs certain operations.
Python provides the following set of operators
1. Arithmetic Operators
2. Relational Operators or Comparison Operators
3. Logical operators
4. Bitwise oeprators
5. Assignment operators
6. Special operators'''




# =============================================================================
# 1. Arithmetic Operators:
# =============================================================================
'''+ ==>Addition
- ==>Subtraction
* ==>Multiplication
/ ==>Division operator
% ===>Modulo operator
// ==>Floor Division operator
** ==>Exponent operator or power operator'''

a=10
b=2
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a//b=',a//b)
print('a%b=',a%b)
print('a**b=',a**b)


'''Note: / operator always performs floating point arithmetic. Hence it will always returns
float value.
But Floor division (//) can perform both floating point and integral arithmetic. If
arguments are int type then result is int type. If atleast one argument is float type then
result is float type'''


'''Note:
We can use +,* operators for str type also.
If we want to use + operator for str type then compulsory both arguments should be str
type only otherwise we will get error.'''


"ton"+10 #TypeError: must be str, not int
"nop"+"10" 


'''If we use * operator for str type then compulsory one argument should be int and other
argument should be str type.'''


2*"Tim"
"Tim"*2
2.5*"Tim" # ==>TypeError: can't multiply sequence by non-int of type 'float'
"Tim"*"Tim" #==>TypeError: can't multiply sequence by non-int of type 'str'

'''+====>String concatenation operator
* ===>String multiplication operator
Note: For any number x,
x/0 and x%0 always raises "ZeroDivisionError"'''


# =============================================================================
# Relational Operators:
# =============================================================================
'''>,>=,<,<='''

a=10
b=20
print("a > b is ",a>b)
print("a >= b is ",a>=b)
print("a < b is ",a<b)
print("a <= b is ",a<=b) 


'''We can apply relational operators for str types also'''
a="durga"
b="durga"
print("a > b is ",a>b)
print("a >= b is ",a>=b)
print("a < b is ",a<b) 
print("a <= b is ",a<=b) 
print(True>True) #False
print(True>=True) #True
print(10 >True) #True
print(False > True) #False
print(10>'Dru')

a=10
b=20
if(a>b):
  print("a is greater than b")
else:
  print("a is not greater than b") 
  
  
'''Note: Chaining of relational operators is possible. In the chaining, if all comparisons
returns True then only result is True. If atleast one comparison returns False then the
result is False'''  
  
10<20 #==>True
10<20<30 #==>True
10<20<30<40 #==>True
10<20<30<40>50 #==>False   

  
# =============================================================================
# Equality operators:
# =============================================================================
'''== , !=
We can apply these operators for any type even for incompatible types also  '''
  
10==20   
10!= 20 
10==True   
False==False   
"tot"=="tot"  
10 == "tot"  
  
  
''' Note: Chaining concept is applicable for equality operators. If atleast one comparison
returns False then the result is False. otherwise the result is True. '''
  
10==20==30==40   
10==10==10==10  
  


# =============================================================================
# Logical Operators:
# =============================================================================
'''and, or ,not
We can apply for all types.
#################################
For boolean types behaviour:
##################################    
and ==>If both arguments are True then only result is True
or ====>If atleast one arugemnt is True then result is True
not ==>complement
True and False ==>False
True or False ===>True
not False ==>True
###############################
For non-boolean types behaviour:
################################    
1. 0 means False
2. non-zero means True
3. empty string is always treated as False
'''

'''x and y:
==>if x is evaluates to false return x otherwise return y'''
10 and 20 #20
0 and 20 #0

'''x or y:
If x evaluates to True then result is x otherwise result is y'''
10 or 20 #10
0 or 20  #20

'''not x:
If x is evalutates to False then result is True otherwise False'''

not 10 #False
not 0 # true

'John' and 'John Mathew' #'John Mathew'
"" and "john" # ""

'John' or 'John Mathew' #'John'
"" or "john" # "john"

not"" # True
not "John" # false


# =============================================================================
# Bitwise Operators:
# =============================================================================
'''We can apply these operators bitwise.
These operators are applicable only for int and boolean types.
By mistake if we are trying to apply for any other type then we will get Error.
&,|,^,~,<<,>>'''

print(4&5) #4
print(10.5 & 5.6) # error
print(True & True)

'''& ==> If both bits are 1 then only result is 1 otherwise result is 0
| ==> If atleast one bit is 1 then result is 1 otherwise result is 0
^ ==>If bits are different then only result is 1 otherwise result is 0
~ ==>bitwise complement operator
1==>0 & 0==>1
<< ==>Bitwise Left shift
>> ==>Bitwise Right Shift'''

print(4&5)
print(4|5) 
print(4^5) 

'''bitwise complement operator(~):
We have to apply complement for total bits.'''

print(~5) #==>-6


'''Note:
The most significant bit acts as sign bit. 0 value represents +ve number where as 1
represents -ve value.
positive numbers will be repesented directly in the memory where as -ve numbers will be
represented indirectly in 2's complement form.'''


# =============================================================================
# Shift Operators:
# =============================================================================
'''<< Left shift operator
After shifting the empty cells we have to fill with zero'''
print(10<<2) #==>40


'''>> Right Shift operator
After shifting the empty cells we have to fill with sign bit.( 0 for +ve and 1 for -ve)'''

print(10>>2) #==>2


'''We can apply bitwise operators for boolean types also'''
print(True & False) #==>False
print(True | False) #===>True
print(True ^ False) #==>True
print(~True) #==>-2
print(True<<2) #==>4
print(True>>2) #==>0


# =============================================================================
# Assignment Operators:
# =============================================================================
'''We can use assignment operator to assign value to the variable.'''
# Eg:
x=10
'''We can combine asignment operator with some other operator to form compound
assignment operator.'''
# Eg: 1
x+=10 #====> x = x+10
'''The following is the list of all possible compound assignment operators in Python
 +=
 -=
 *=
 /=
 %=
 //=
 **=
&=
|=
^=
>>=
<<=

'''
x=10 

x+=20
print(x) #==>30
# Eg:
x=10
x&=5
print(x) #==>0 


# =============================================================================
# Ternary Operator:
# =============================================================================
'''Syntax:
x = firstValue if condition else secondValue
If condition is True then firstValue will be considered else secondValue will 
be considered.
Note: Nesting of ternary operator is possible'''
# Eg 1:
a,b=10,20
x=30 if a<b else 40
print(x) #30
#Eg 2: Read two numbers from the keyboard and print minimum value
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
min=a if a<b else b
print("Minimum Value:",min) 


# Program for minimum of 3 numbers
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
min=a if a<b and a<c else b if b<c else c
print("Minimum Value:",min)

#Q. Program for maximum of 3 numbers
a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
max=a if a>b and a>c else b if b>c else c
print("Maximum Value:",max) 

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("Both numbers are equal" if a==b else "First Number is Less than Second Number" if
a<b else "First Number Greater than Second Number") 


'''Python defines the following 2 special operators
1. Identity Operators
2. Membership operators'''


# =============================================================================
# 1. Identity Operators
# =============================================================================
'''We can use identity operators for address comparison.
2 identity operators are available
1. is
2. is not
r1 is r2 returns True if both r1 and r2 are pointing to the same object
r1 is not r2 returns True if both r1 and r2 are not pointing to the same object

Note:
We can use is operator for address comparison where as == operator for content
comparison.
'''


a=10
b=10
print(a is b) #True
x=True
y=True
print( x is y) #True
# Eg:
a="durga"
b="durga"
print(id(a))
print(id(b))
print(a is b)
# Eg:
list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2) #False
print(list1 is not list2) #True
print(list1 == list2) #True


# =============================================================================
# 2. Membership operators:
# =============================================================================
'''We can use Membership operators to check whether the given object present in the
given collection.(It may be String,List,Set,Tuple or Dict)
in  Returns True if the given object present in the specified Collection
not in  Retruns True if the given object not present in the specified Collection'''
# Eg:
x="hello learning Python is very easy!!!"
print('h' in x) #True
print('d' in x) #False
print('d' not in x) #True
print('Python' in x) #True
# Eg:
list1=["sunny","bunny","chinny","pinny"]
print("sunny" in list1) #True
print("tunny" in list1) #False
print("tunny" not in list1) #True


# =============================================================================
# Operator Precedence:
# =============================================================================
'''If multiple operators present then which operator will be evaluated first is decided by
operator precedence.'''
# Eg:
print(3+10*2) 
print((3+10)*2)
 
'''The following list describes operator precedence in Python
()  Parenthesis
**  exponential operator
~,-  Bitwise complement operator,unary minus operator
*,/,%,//  multiplication,division,modulo,floor division
+,-  addition,subtraction
<<,>>  Left and Right Shift
&  bitwise And
^  Bitwise X-OR
|  Bitwise OR
>,>=,<,<=, ==, != ==>Relational or Comparison operators
=,+=,-=,*=... ==>Assignment operators
is , is not  Identity Operators
in , not in  Membership operators
not  Logical not
and  Logical and
or  Logical or

'''

a=30
b=20
c=10
d=5
print((a+b)*c/d) #100.0
print((a+b)*(c/d)) #100.0
print(a+(b*c)/d) #70.0

3/2*4+3+(10/5)**3-2
3/2*4+3+2.0**3-2
3/2*4+3+8.0-2
1.5*4+3+8.0-2
6.0+3+8.0-2


# =============================================================================
# Mathematical Functions (math Module)
# =============================================================================
import math
print(math.sqrt(16))
print(math.pi)

# Once we create alias name, by using that we can access functions and variables of that
# module
import math as m
print(m.sqrt(16))
print(m.pi)
# We can import a particular member of a module explicitly as follows
from math import sqrt
from math import sqrt,pi

# Q. Write a Python program to find area of circle
from math import pi
r=16
print("Area of Circle is :",pi*r**2)


# =============================================================================
# Input And Output Statements
# =============================================================================


# input() function can be used to read data directly in our required format.We are not
# required to perform type casting.
# every input value is treated as str type only
x=input("Enter Value")
type(x)


# Q. Write a program to read Employee data from the keyboard and print that data.

eno=int(input("Enter Employee No:"))
ename=input("Enter Employee Name:")
esal=float(input("Enter Employee Salary:"))
eaddr=input("Enter Employee Address:")
married=bool(input("Employee Married ?[True|False]:"))
print("Please Confirm Information")
print("Employee No :",eno)
print("Employee Name :",ename)
print("Employee Salary :",esal)
print("Employee Address :",eaddr)
print("Employee Married ? :",married)


# How to read multiple values from the keyboard in a single line:

a,b= [int(x) for x in input("Enter 2 numbers :").split()]
print("Product is :", a*b) 


# Q. Write a program to read 3 float numbers from the keyboard with , seperator and print
# their sum.
a,b,c= [float(x) for x in input("Enter 3 float numbers :").split(',')]
print("The Sum is :", a+b+c) 


# =============================================================================
# eval():
# eval Function take a String and evaluate the Result.# 
# eval() can evaluate the Input to list, tuple, set, etc based the provided Input.
# =============================================================================
x = eval("10+20+30")
print(x)


x = eval(input("Enter Expression"))
#Enter Expression: 10+2*3/4


l = eval(input("Enter List"))
print (type(l))
print(l)


# =============================================================================
# # Command Line Arguments
# # argv is not Array it is a List. It is available sys Module.
# # The Argument which are passing at the time of execution are called Command Line
# # Arguments
# Note: argv[0] represents Name of Program. But not first Command Line Argument.
# argv[1] represent First Command Line Argument.
# =============================================================================
# py test.py 10 20 30

# Program: To check type of argv from sys
import argv
print(type(argv))


# Write a Program to display Command Line Arguments

from sys import argv
print("The Number of Command Line Arguments:", len(argv))
print("The List of Command Line Arguments:", argv)
print("Command Line Arguments one by one:")
for x in argv:
    print(x)

# >> D:\Python_classes>py test.py 10 20 30
# >> The Number of Command Line Arguments: 4 


from sys import argv
sum=0
args=argv[1:]
for x in args:
    n=int(x)
    sum=sum+n
    print("The Sum:",sum) 



# Note1: usually space is seperator between command line arguments. If our command line
# argument itself contains space then we should enclose within double quotes(but not
# single quotes)

from sys import argv
print(argv[1]) 

# >> D:\Python_classes>py test.py "Manakin mink"

# Note2: Within the Python program command line arguments are available in the String
# form. Based on our requirement,we can convert into corresponding type by using type
# casting methods.

from sys import argv
print(argv[1]+argv[2])
print(int(argv[1])+int(argv[2]))


# Note:
# In Python there is argparse module to parse command line arguments and display some
# help messages whenever end user enters wrong input.


# output statements:
# We can use print() function to display output.


# Form-1: print() without any argument
# Just it prints new line character

# Form-2:
    
print('String')
print("Hello World")
# We can use escape characters also
print("Hello \n World")
print("Hello\tWorld")
# We can use repetetion operator (*) in the string
print(10*"Hello")
print("Hello"*10)
# We can use + operator also
print("Hello"+"World") 


# Note:
# If both arguments are String type then + operator acts as concatenation operator.
# If one argument is string type and second is any other type like int then we will get Error
# If both arguments are number type then + operator acts as arithmetic addition operator


print("Hello"+"World")
print("Hello","World") 


# Form-3: print() with variable number of arguments:

a,b,c=10,20,30
print("The Values are :",a,b,c) 


# By default output values are seperated by space.If we want we can specify seperator by
# using "sep" attribute

a,b,c=10,20,30
print(a,b,c,sep=',')
print(a,b,c,sep=':') 


# Form-4:print() with end attribute:
print("Hello")
print("John")
print("Doe") 

# If we want output in the same line with space
print("Hello",end=' ')
print("John",end=' ')
print("Doe") 

# Note: The default value for end attribute is \n,which is nothing but new line character.


# Form-5: print(object) statement:
# We can pass any object (like list,tuple,set etc)as argument to the print() statement. 

l=[10,20,30,40]
t=(10,20,30,40)
print(l)
print(t) 

# Form-6: print(String,variable list):
# We can use print() statement with String and any number of arguments

s="John"
a=48
s1="java"
s2="Python"
print("Hello",s,"Your Age is",a)
print("You are teaching",s1,"and",s2) 


# Form-7: print(formatted string):
# %i====>int
# %d====>int
# %f=====>float
# %s======>String type
# Syntax:
# print("formatted string" %(variable list))

a=10
b=20
c=30
print("a value is %i" %a)
print("b value is %d and c value is %d" %(b,c))

s="John"
list=[10,20,30,40]
print("Hello %s ...The List of Items are %s" %(s,list)) 


# Form-8: print() with replacement operator {}
name="john"
salary=10000
gf="tara"
print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name,salary,gf))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name,y=salary,z=
gf)) 



# =============================================================================
# Flow Control
# Flow control describes the order in which statements will be executed at runtime.
# Conditional Statements - 
# 1) if
# 2) if-elif
# 3) if-elif-else
# # Transfer Statements
# 1) break
# 2) continue
# 3) pass
# Iterative Statements
# 1) for
# 2) while
# =============================================================================

# =============================================================================
# Conditional Statements
# Note:
# 1. else part is always optional
#  Hence the following are various possible syntaxes.
#  1. if
#  2. if - else
#  3. if-elif-else
#  4.if-elif
# 2. There is no switch statement in Python
# # =============================================================================
# 1) if
# if condition : statement
#  or
# if condition :
#  statement-1
#  statement-2
#  statement-3
# If condition is true then statements will be executed.

name=input("Enter Name:")
if name=="Parveen" :
    print("Hello parveen Good Morning")
    print("How are you!!!") 

# 2) if-else:
# if condition :
#  Action-1
# else :
#  Action-2
# if condition is true then Action-1 will be executed otherwise Action-2 will be executed.

name=input("Enter Name:")
if name=="Parveen":
    print("Hello Parveen Good Morning")
else:
    print("Hello Guest Good Moring")
    print("How are you!!!")


# 3) if-elif-else:
# Syntax:
# if condition1:
#  Action-1
# elif condition2:
#  Action-2
# elif condition3:
#  Action-3
# elif condition4:
#  Action-4
#  ...
# else:
#  Default Action
# Based condition the corresponding action will be executed.

brand=input("Enter Your Favourite Brand:")
if brand=="RC" :
    print("It is childrens brand")
elif brand=="KF":
    print("It is not that much kick")
elif brand=="FO":
    print("Buy one get Free One")
else :
    print("Other Brands are not recommended")


#Q. Write a program to find biggest of given 2 numbers from the commad prompt?
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
if n1>n2:
    print("Biggest Number is:",n1)
else :
    print("Biggest Number is:",n2) 
    
    
# a program to find biggest of given 3 numbers from the commad prompt?
n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
    print("Biggest Number is:",n1)
elif n2>n3:
    print("Biggest Number is:",n2)
else :
    print("Biggest Number is:",n3)     
    
    
    
# Write a program to check whether the given number is in between 1 and 100?
n=int(input("Enter Number:"))
if n>=1 and n<=10 :
    print("The number",n,"is in between 1 to 10")
else:
    print("The number",n,"is not in between 1 to 10")     
    
    
# Iterative Statements
# If we want to execute a group of statements multiple times then we should go for
# Iterative statements.
   
    
# 1) for loop:
# If we want to execute some action for every element present in some sequence
# (it may be string or collection) then we should go for for loop.
# Syntax:
# for x in sequence :
#     body
# where sequence can be string or any collection.
# Body will be executed for every element present in the sequence.
   
    
# Eg 1: To print characters present in the given string    
    
s="John Doe"
for x in s :
    print(x)     
    

# Eg 3: To print Hello 10 times
for x in range(10) :
    print("Hello") 


# To display numbers from 0 to 10

for x in range(11) :
    print(x)


# To display odd numbers from 0 to 20
for x in range(21) :
    if (x%2!=0):
        print(x)

# Eg 6: To display numbers from 10 to 1 in descending order
for x in range(10,0,-1):
    print(x) 

# To print sum of numbers present inside list
list=eval(input("Enter List:"))
sum=0;
for x in list:
    sum=sum+x;
    print("The Sum=",sum) 


# 2) while loop:
# If we want to execute a group of statements iteratively until some condition false,then we
# should go for while loop.

# Syntax:
#  while condition :
#  body

# Eg: To print numbers from 1 to 10 by using while loop
x=1
while x <=10:
    print(x)
    x=x+1
# Eg: To display the sum of first n numbers
n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print("The sum of first",n,"numbers is :",sum) 


# write a program to prompt user to enter some name until entering Name
name=""
while name!="durga":
    name=input("Enter Name:")
    print("Thanks for confirmation") 


# Infinite Loops:
i=0;
while True :
    i=i+1
    print("Hello",i) 
    
# Nested Loops:
# Sometimes we can take a loop inside another loop,which are also known as nested loops.
for i in range(4):
    for j in range(4):
            print("i=",i,"\tj=",j) 


# Write a program to dispaly *'s in Right angled triangled form

n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
            print("*",end=" ")
    print()


# Alternative way:
n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    print("* " * i)
    
#Q. Write a program to display *'s in pyramid style(also known as equivalent triangle)
n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("* "*i) 



# III. Transfer Statements
# 1) break:
# We can use break statement inside loops to break loop execution based on some
# condition.
for i in range(10):
    if i==7:
        print("processing is enough..plz break")
        break
    print(i)


cart=[10,20,600,60,70]
for item in cart:
    if item>500:
        print("To place this order insurence must be required")
        break
    print(item) 


# 2) continue:
# We can use continue statement to skip current iteration and continue next iteration.
# Eg 1: To print odd numbers in the range 0 to 9
for i in range(10):
    if i%2==0:
        continue
    print(i) 


cart=[10,20,500,700,50,60]
for item in cart:
    if item>=500:
        print("We cannot process this item :",item)
        continue
    print(item)


numbers=[10,20,0,5,0,30]
for n in numbers:
    if n==0:
        print("Hey how we can divide with zero..just skipping")
        continue
    print("100/{} = {}".format(n,100/n)) 


# loops with else block:
# Inside loop execution,if break statement not executed ,then only else part will be
# executed.
# else means loop without break
cart=[10,20,30,40,50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)

else:
    print("Congrats ...all items processed successfully") 



cart=[10,20,600,30,40,50]
for item in cart:
    if item>=500:
        print("We cannot process this order")
        break
    print(item)

else:
    print("Congrats ...all items processed successfully") 


# 3) pass statement:
# pass is a keyword in Python.
# In our programming syntactically if block is required which won't do anything then we can
# define that empty block with pass keyword.
# pass
#  |- It is an empty statement
#  |- It is null statement
#  |- It won't do anything



if True: pass
# ==>valid

# def m1():
#SyntaxError: unexpected EOF while parsing

def m1(): 
    pass


# use case of pass:
# Sometimes in the parent class we have to declare a function with empty body and child
# class responsible to provide proper implementation. Such type of empty body we can
# define by using pass keyword. (It is something like abstract method in java)

for i in range(100):
    if i%9==0:
        print(i)
    else:
        pass

# del statement:
# del is a keyword in Python.
# After using a variable, it is highly recommended to delete that variable if it is no longer
# required,so that the corresponding object is eligible for Garbage Collection.
# We can delete variable by using del keyword

x=10
print(x)
del x

# Note:
# We can delete variables which are pointing to immutable objects.But we cannot delete
# the elements present inside immutable object.
# Eg:
S="Pikoo"
print(S)
del S   #==>valid
#del S[0] #==>TypeError: 'str' object doesn't support item deletion 

# But in the case of None assignment the variable won't be removed but the corresponding
# object is eligible for Garbage Collection(re bind operation). Hence after assigning with
# None value,we can access that variable.
s="Home"
s=None
print(s) # None 



# =============================================================================
# String Data Type
# =============================================================================

# What is String?
# Any sequence of characters within either single quotes or double quotes is considered as a String.
# Syntax:
s='John'
s="JOhn"
# Note: In most of other languges like C, C++,Java, a single character with in single quotes is treated
# as char data type value. But in Python we are not having char data type.Hence it is treated as
# String only.
# Eg:
ch='a'
type(ch)

# How to define multi-line String literals:
# We can define multi-line String literals by using triple single or double quotes.
# Eg:
s='''John
Constantine
solutions'''
# We can also use triple quotes to use single quotes or double quotes as symbol inside String literal.
# Eg:
s='This is 'single quote symbol' #==>invalid
s='This is \' single quote symbol' #==>valid
s="This is 'single quote symbol"#====>valid
s='This is " double quotes symbol' #==>valid
s='The "Python Notes" by 'John' is very helpful' #==>invalid
s="The "Python Notes" by 'John' is very helpful"#==>invalid
s='The \"Python Notes\" by \'John\' is very helpful' #==>valid
s='''The "Python Notes" by 'John' is very helpful''' #==>valid


# How to access characters of a String:
# We can access characters of a string by using the following ways.
# 1. By using index
# 2. By using slice operator


# 1. By using index:
# Python supports both +ve and -ve index.
# +ve index means left to right(Forward direction)
# -ve index means right to left(Backward direction)

s='Mohan'
s[0]
s[4]
s[-1]
s[10]


# Q. Write a program to accept some string from the keyboard and display its characters by
# index wise(both positive and nEgative index)
s=input("Enter Some String:")
i=0
for x in s:
    print("The character present at positive index {} and at negative index {} is {}".format(i,i-len(s),x))
    i=i+1 


# 2. Accessing characters by using slice operator:
# Syntax: s[beginindex:endindex:step]
# beginindex:From where we have to consider slice(substring)
# endindex: We have to terminate the slice(substring) at endindex-1
# step: incremented value
# Note: If we are not specifying begin index then it will consider from beginning of the string.
# If we are not specifying end index then it will consider up to end of the string
# The default value for step is 1

s="Learning Python is very very easy!!!"
s[1:7:1]

s[1:7]

s[1:7:2]

s[:7]

s[7:]

s[::]

s[:]

s[::-1]


# ***Note:
# In the backward direction if end value is -1 then result is always empty.
# In the forward direction if end value is 0 then result is always empty.
# In forward direction:
# default value for bEgin: 0
# default value for end: length of string
# default value for step: +1
# In backward direction:
# default value for bEgin: -1
# default value for end: -(length of string+1)
# Note: Either forward or backward direction, we can take both +ve and -ve values for bEgin and
# end index.


# Mathematical Operators for String:

# We can apply the following mathematical operators for Strings.
# 1. + operator for concatenation
# 2. * operator for repetition
print("John"+"Constantine") 
print("John"*2) #durgadurga


# Note:
# 1. To use + operator for Strings, compulsory both arguments should be str type
# 2. To use * operator for Strings, compulsory one argument should be str and other argument
# should be int


# len() in-built function:
# We can use len() function to find the number of characters present in the string.

s ="John Constantine"
print(len(s))


# Write a program to access each character of string in forward and backward direction
# by using while loop?
s="Learning Python is very easy !!!"
n=len(s)
i=0
print("Forward direction")
while i<n:
    print(s[i],end=' ')
    i +=1
print("Backward direction")
i=-1
while i>=-n:
    print(s[i],end=' ')
    i=i-1 


# Alternative ways:
s="Learning Python is very easy !!!"
print("Forward direction")
for i in s:
    print(i,end=' ')

print("Forward direction")
for i in s[::]:
    print(i,end=' ')

print("Backward direction")
for i in s[::-1]:
    print(i,end=' ') 


# Checking Membership:
# We can check whether the character or string is the member of another string or not by using in
# and not in operators

s='John'
print('h' in s) #True
print('z' in s) #False


s=input("Enter main string:")
subs=input("Enter sub string:")
if subs in s:
    print(subs,"is found in main string")
else:
    print(subs,"is not found in main string") 


# Comparison of Strings:
# We can use comparison operators (<,<=,>,>=) and equality operators(==,!=) for strings.
# Comparison will be performed based on alphabetical order.

s1=input("Enter first string:")
s2=input("Enter Second string:")
if s1==s2:
    print("Both strings are equal")
elif s1<s2:
    print("First String is less than Second String")
else:
    print("First String is greater than Second String") 



# Removing spaces from the string:
# We can use the following 3 methods
# 1. rstrip()===>To remove spaces at right hand side
# 2. lstrip()===>To remove spaces at left hand side
# 3. strip() ==>To remove spaces both sides


city=input("Enter your city Name:")
scity=city.strip()
if scity=='Hyderabad':
    print("Hello Hyderbadi..Adab")
elif scity=='Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity=="Bangalore":
    print("Hello Kannadiga...Shubhodaya")
else:
    print("your entered city is invalid") 



# Finding Substrings:
# We can use the following 4 methods
# For forward direction:
# find()
# index()
# For backward direction:
# rfind()
# rindex()

# 1. find():
# s.find(substring)
# Returns index of first occurrence of the given substring. If it is not available then we will get -1
s="Learning Python is very easy" 
print(s.find("Python")) #9
print(s.find("Java")) # -1
print(s.find("r"))#3
print(s.rfind("r"))#21 


# Note: By default find() method can search total string. We can also specify the boundaries to
# search.
# s.find(substring,bEgin,end)
# It will always search from bEgin index to end-1 index

s="ParveenMalik"
print(s.find('a'))#4
print(s.find('a',7,15))#10
print(s.find('z',7,15))#-1 

# index() method:
# index() method is exactly same as find() method except that if the specified substring is not
# available then we will get ValueError.

s=input("Enter main string:")
subs=input("Enter sub string:")
try:
    n=s.index(subs)
except ValueError:
    print("substring not found")
else:
    print("substring found") 


# Q. Program to display all positions of substring in a given main string
s=input("Enter main string:")
subs=input("Enter sub string:")
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at position",pos)
    flag=True

if flag==False:
    print("Not Found") 


# Counting substring in the given String:
# We can find the number of occurrences of substring present in the given string by using count()
# method.
# 1. s.count(substring) ==> It will search through out the string
# 2. s.count(substring, bEgin, end) ===> It will search from bEgin index to end-1 index

s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,7)) 

# Replacing a string with another string:
# s.replace(oldstring,newstring)
# inside s, every occurrence of oldstring will be replaced with newstring.
s="Learning Python is very difficult"
s1=s.replace("difficult","easy")
print(s1)


# Eg2: All occurrences will be replaced
s="ababababababab"
s1=s.replace("a","b")
print(s1)

# Q. String objects are immutable then how we can change the content by
# using replace() method.
# Once we creates string object, we cannot change the content.This non changeable behaviour is
# nothing but immutability. If we are trying to change the content by using any method, then with
# those changes a new object will be created and changes won't be happend in existing object.
# Hence with replace() method also a new object got created but existing object won't be changed.
# Eg:
s="abab"
s1=s.replace("a","b")
print(s,"is available at :",id(s))
print(s1,"is available at :",id(s1))


# In the above example, original object is available and we can see new object which was created
# because of replace() method.


# Splitting of Strings:
# We can split the given string according to specified seperator by using split() method.
# l=s.split(seperator)
# The default seperator is space. The return type of split() method is List

s="John Augustine Constantine"
l=s.split()
for x in l:
    print(x) 


# Eg2:
s="22-02-2018"
l=s.split('-')
for x in l:
    print(x) 


# Joining of Strings:
# We can join a group of strings(list or tuple) wrt the given seperator.
# s=seperator.join(group of strings)

t=('sunny','bunny','chinny')
s='-'.join(t)
print(s)

l=['hyderabad','singapore','london','dubai']
s=':'.join(l)
print(s)


# Changing case of a String:
# We can change case of a string by using the following 4 methods.
# 1. upper()===>To convert all characters to upper case
# 2. lower() ===>To convert all characters to lower case
# 3. swapcase()===>converts all lower case characters to upper case and all upper case characters to
# lower case
# 4. title() ===>To convert all character to title case. i.e first character in every word should be upper
# case and all remaining characters should be in lower case.
# 5. capitalize() ==>Only first character will be converted to upper case and all remaining characters
# can be converted to lower case
# Eg:
s='learning Python is very Easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())


# Checking starting and ending part of the string:
# Python contains the following methods for this purpose
# 1. s.startswith(substring)
# 2. s.endswith(substring)
# Eg:
s='learning Python is very easy'
print(s.startswith('learning'))
print(s.endswith('learning'))
print(s.endswith('easy'))

# To check type of characters present in a string:
# Python contains the following methods for this purpose.
# 1) isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
# 2) isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)
# 3) isdigit(): Returns True if all characters are digits only( 0 to 9)
# 4) islower(): Returns True if all characters are lower case alphabet symbols
# 5) isupper(): Returns True if all characters are upper case aplhabet symbols
# 6) istitle(): Returns True if string is in title case
# 7) isspace(): Returns True if string contains only spaces



s=input("Enter any character:")
if s.isalnum():
    print("Alpha Numeric Character")
if s.isalpha():
    print("Alphabet character")
if s.islower():
    print("Lower case alphabet character")
else:
    print("Upper case alphabet character")
else:
    print("it is a digit")
elif s.isspace():
    print("It is space character")
else:
    print("Non Space Special Character") 


# Formatting the Strings:
# We can format the strings with variable values by using replacement operator {} and format()
# method.
# Eg:
name='Timmy'
salary=10000
age=48
print("{} 's salary is {} and his age is {}".format(name,salary,age))
print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))



# Important Programs rEgarding String Concept


# Q1. Write a program to reverse the given String

# 1st Way:
s=input("Enter Some String:")
print(s[::-1])

# 2nd Way:
s=input("Enter Some String:")
print(''.join(reversed(s)))

# 3rd Way:
s=input("Enter Some String:")
i=len(s)-1
target=''
while i>=0:
target=target+s[i]
i=i-1
print(target)


# Q2. Program to reverse order of words.


s=input("Enter Some String:")
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print(output) 



# Q3. Program to reverse internal content of each word.

s=input("Enter Some String:")
l=s.split()
l1=[]
i=0
while i<len(l):
    l1.append(l[i][::-1])
    i=i+1
output=' '.join(l1)
print(output) 


# Q4. Write a program to print characters at odd position and even position for the given
# String?
# 1st Way:
s=input("Enter Some String:")
print("Characters at Even Position:",s[0::2])
print("Characters at Odd Position:",s[1::2])

# 2nd Way:
s=input("Enter Some String:")
i=0
print("Characters at Even Position:")
while i< len(s):
    print(s[i],end=',')
    i=i+2
    print()
    print("Characters at Odd Position:")
    i=1
while i< len(s):
    print(s[i],end=',')
    i=i+2 


# Q5. Program to merge characters of 2 strings into a single string by taking characters
# alternatively.
s1=input("Enter First String:")
s2=input("Enter Second String:")
output=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        output=output+s1[i]
        i+=1
    if j<len(s2):
        output=output+s2[j]
        j+=1
print(output)


# Q6. Write a program to sort the characters of the string and first alphabet symbols
# followed by numeric values

s=input("Enter Some String:")
s1=s2=output=''
for x in s:
    if x.isalpha():
        s1=s1+x
    else:
        s2=s2+x
for x in sorted(s1):
    output=output+x
    
for x in sorted(s2):
    output=output+x    
print(output) 



# Q7. Write a program for the following requirement
# input: a4b3c2
# output: aaaabbbcc
s=input("Enter Some String:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x 
    else:
        output=output+previous*(int(x)-1)
print(output)



# Note: chr(unicode)===>The corresponding character
#  ord(character)===>The corresponding unicode value


# Q8. Write a program to perform the following activity
# input: a4k3b2
# output:aeknbd
s=input("Enter Some String:")
output=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+chr(ord(previous)+int(x))
print(output)



# Q9. Write a program to remove duplicate characters from the given input string?
# input: ABCDABBCDABBBCCCDDEEEF
# output: ABCDEF
s=input("Enter Some String:")
l=[]
for x in s:
    if x not in l:
        l.append(x)
        output=''.join(l)
print(output)




# Q10. Write a program to find the number of occurrences of each character present in the
# given String?
# input: ABCABCABBCDE
# output: A-3,B-4,C-3,D-1,E-1
s=input("Enter the Some String:")
d={}
for x in s:
    if x in d.keys():
        d[x]=d[x]+1
    else:
        d[x]=1
for k,v in d.items():
    print("{} = {} Times".format(k,v)) 

# =============================================================================
# 
# Formatting the Strings:
# We can format the strings with variable values by using replacement operator {} and format()
# method.
# The main objective of format() method to format string into meaningful output form.
# =============================================================================


# Case- 1: Basic Formatting for default, positional and keyword arguments


name='Tmmy'
salary=10000
age=48
print("{} 's salary is {} and his age is {}".format(name,salary,age))
print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))


# Case-2: Formatting Numbers

# d--->Decimal IntEger
# f----->Fixed point number(float).The default precision is 6
# b-->Binary format
# o--->Octal Format
# x-->Hexa Decimal Format(Lower case)
# X-->Hexa Decimal Format(Upper case)
# Eg-1:
    
    
print("The integer number is: {}".format(123))
print("The integer number is: {:d}".format(123))
print("The integer number is: {:5d}".format(123))
print("The integer number is: {:05d}".format(123))

# Eg-2:

print("The float number is: {}".format(123.4567))
print("The float number is: {:f}".format(123.4567))
print("The float number is: {:8.3f}".format(123.4567))
print("The float number is: {:08.3f}".format(123.4567))
print("The float number is: {:08.3f}".format(123.45))
print("The float number is: {:08.3f}".format(786786123.45))

# Note:
# {:08.3f}
# Total positions should be minimum 8.
# After decimal point exactly 3 digits are allowed.If it is less then 0s will be placed in the last
# positions
# If total number is < 8 positions then 0 will be placed in MSBs
# If total number is >8 positions then all intEgral digits will be considered.
# The extra digits we can take only 0
# Note: For numbers default alignment is Right Alignment(>)

# Eg-3: Print Decimal value in binary, octal and hexadecimal form

print("Binary Form:{0:b}".format(153))
print("Octal Form:{0:o}".format(153))
print("Hexa decimal Form:{0:x}".format(154))
print("Hexa decimal Form:{0:X}".format(154))


# Note: We can represent only int values in binary, octal and hexadecimal and it is not possible for
# float values.
# Note:
# {:5d} It takes an intEger argument and assigns a minimum width of 5.
# {:8.3f} It takes a float argument and assigns a minimum width of 8 including "." and after decimal
# point excatly 3 digits are allowed with round operation if required
# {:05d} The blank places can be filled with 0. In this place only 0 allowed.


# Case-3: Number formatting for signed numbers
# While displaying positive numbers,if we want to include + then we have to write
# {:+d} and {:+f}
# Using plus for -ve numbers there is no use and for -ve numbers - sign will come automatically.


print("int value with sign:{:+d}".format(123))
print("int value with sign:{:+d}".format(-123))
print("float value with sign:{:+f}".format(123.456))
print("float value with sign:{:+f}".format(-123.456))


# Case-4: Number formatting with alignment
# <,>,^ and = are used for alignment
# <==>Left Alignment to the remaining space
# ^===>Center alignment to the remaining space
# >===> Right alignment to the remaining space
# = ===>Forces the signed(+) (-) to the left most position
# Note: Default Alignment for numbers is Right Alignment.
# Ex:
    
    
    
print("{:5d}".format(12))
print("{:<5d}".format(12))
print("{:<05d}".format(12))
print("{:>5d}".format(12))
print("{:>05d}".format(12))
print("{:^5d}".format(12))
print("{:=5d}".format(-12))
print("{:^10.3f}".format(12.23456))
print("{:=8.3f}".format(-12.23456))

# Case-5: String formatting with format()
# Similar to numbers, we can format String values also with format() method.
# s.format(string)
# Eg:
    
    

print("{:5d}".format(12))
print("{:5}".format("rat"))
print("{:>5}".format("rat"))
print("{:<5}".format("rat"))
print("{:^5}".format("rat"))
print("{:*^5}".format("rat")) #Instead of * we can use any character(like +,$,a etc)

# Note: For numbers default alignment is right where as for strings default alignment is left




# Case-6: Truncating Strings with format() method

print("{:.3}".format("ParveenMalik"))
print("{:5.3}".format("ParveenMalik"))
print("{:>5.3}".format("ParveenMalik"))
print("{:^5.3}".format("ParveenMalik"))
print("{:*^5.3}".format("ParveenMalik"))

# Par
# Par  
#   Par
#  Par 
# *Par*

# Case-7: Formatting dictionary members using format()


person={'age':48,'name':'Timm'}
print("{p[name]}'s age is: {p[age]}".format(p=person)) 



# Note: p is alias name of dictionary
# person dictionary we are passing as keyword argument

# More convenient way is to use **person
# Eg:
person={'age':48,'name':'Timm'}
print("{name}'s age is: {age}".format(**person))




# Case-8: Formatting class members using format()
# Eg:

class Person:
    age=48
    name="TImm"
    print("{p.name}'s age is :{p.age}".format(p=Person()))




# Eg:
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("{p.name}'s age is :{p.age}".format(p=Person('durga',48)))
        print("{p.name}'s age is :{p.age}".format(p=Person('Ravi',50)))
    
# Note: Here Person object is passed as keyword argument. We can access by using its reference
# variable in the template string




# Case-9: Dynamic Formatting using format()


string="{:{fill}{align}{width}}"
print(string.format('cat',fill='*',align='^',width=5))
print(string.format('cat',fill='*',align='^',width=6))
print(string.format('cat',fill='*',align='<',width=6))
print(string.format('cat',fill='*',align='>',width=6)) 


# Output:
# *cat*
# *cat**
# cat***
# ***cat




Case-10: Dynamic Float format template


num="{:{align}{width}.{precision}f}"
print(num.format(123.236,align='<',width=8,precision=2))
print(num.format(123.236,align='>',width=8,precision=2))
# Output:
# 123.24
# 123.24


Case-11: Formatting Date values

import datetime
 #datetime formatting
date=datetime.datetime.now()
print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))


Case-12: Formatting complex numbers

complexNumber=1+2j
print("Real Part:{0.real} and Imaginary Part:{0.imag}".format(complexNumber))

# Output: Real Part:1.0 and Imaginary Part:2.0

# =============================================================================
# List Data Structure
# If we want to represent a group of individual objects as a single entity where insertion
# order preserved and duplicates are allowed, then we should go for List.
# insertion order preserved.
# duplicate objects are allowed
# heterogeneous objects are allowed.
# List is dynamic because based on our requirement we can increase the size and decrease
# the size.
# In List the elements will be placed within square brackets and with comma seperator.
# We can differentiate duplicate elements by using index and we can preserve insertion
# order by using index. Hence index will play very important role.
# Python supports both positive and negative indexes. +ve index means from left to right
# where as negative index means right to left
# 
# List objects are mutable.i.e we can change the content.
# 
# =============================================================================

# Creation of List Objects:
# We can create empty list object as follows...
list=[]
print(list)
print(type(list))


# 2. If we know elements already then we can create list as follows
list=[10,20,30,40]


# 3. With dynamic input:

list=eval(input("Enter List:"))
print(list)
print(type(list)) 


# 4. With list() function:
l=list(range(0,10,2))
print(l)
print(type(l))



s="Constantine"
l=list(s)
print(l) 


# 5. with split() function:
s="Learning Python is very very easy !!!"
l=s.split()
print(l)
print(type(l)) 


# Note:
# Sometimes we can take list inside another list,such type of lists are called nested lists.
A=[10,20,[30,40]]



# Accessing elements of List:
# We can access elements of the list either by using index or by using slice operator(:)
# 1. By using index:
# List follows zero based index. ie index of first element is zero.
# List supports both +ve and -ve indexes.
# +ve index meant for Left to Right
# -ve index meant for Right to Left
list=[10,20,30,40]
print(list[0]) #==>10
print(list[-1]) #==>40
print(list[10]) #==>IndexError: list index out of range

# 2. By using slice operator:
# Syntax:
# list2= list1[start:stop:step]
# start ==>it indicates the index where slice has to start
#  default value is 0
# stop ===>It indicates the index where slice has to end
#  default value is max allowed index of list ie length of the list
# step ==>increment value
#  default value is 1


n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])
print(n[4::2])
print(n[3:7])
print(n[8:2:-2])
print(n[4:100]) 



# List vs mutability:
# Once we creates a List object,we can modify its content. Hence List objects are mutable.
# Eg:
n=[10,20,30,40]
print(n)
n[1]=777
print(n) 


# Traversing the elements of List:
# The sequential access of each element in the list is called traversal.
# 1. By using while loop:
n=[0,1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(n):
    print(n[i])
    i=i+1

# 2. By using for loop:
n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    print(n1) 


# 3. To display only even numbers:
    
n=[0,1,2,3,4,5,6,7,8,9,10]
for n1 in n:
    if n1%2==0:
        print(n1) 


# 4. To display elements by index wise:
l=["A","B","C"]
x=len(l)
for i in range(x):
 print(l[i],"is available at positive index: ",i,"and at negative index: ",i-x) 

# Important functions of List:
# I. To get information about list:

# 1. len():
#  returns the number of elements present in the list
# Eg: 
n=[10,20,30,40]
print(len(n))#==>4

# 2. count():
# It returns the number of occurrences of specified item in the list

n=[1,2,2,2,2,3,3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))


# 3. index() function:
# returns the index of first occurrence of the specified item.
# Eg:
    
n=[1,2,2,2,2,3,3]
print(n.index(1)) #==>0
print(n.index(2)) #==>1
print(n.index(3)) #==>5
print(n.index(4)) #==>ValueError: 4 is not in list 



# Note: If the specified element not present in the list then we will get ValueError.Hence
# before index() method we have to check whether item present in the list or not by using in
# operator.

print(4 in n)  #==>False

# =============================================================================
# II. Manipulating elements of List:
# =============================================================================
# 1. append() function:
# We can use append() function to add item at the end of the list.
# Eg:
list=[]
list.append("A")
list.append("B")
list.append("C")
print(list)



# Eg: To add all elements to list upto 100 which are divisible by 10
list=[]
for i in range(101):
if i%10==0:
list.append(i)
print(list)


# =============================================================================
# 2. insert() function:
# To insert item at specified index position
# =============================================================================


n=[1,2,3,4,5]
n.insert(1,888)
print(n)


# Eg:
n=[1,2,3,4,5]
n.insert(10,777)
n.insert(-10,999)
print(n) 


# Note: If the specified index is greater than max index then element will be inserted at last
# position. If the specified index is smaller than min index then element will be inserted at
# first position.


# Differences between append() and insert()

# append() 
# In List when we add any element it will
# come in last i.e. it will be last element.
# insert()
# In List we can insert any element in
# particular index number


# 3. extend() function:
# To add all items of one list to another list
# l1.extend(l2)
# all items present in l2 will be added to l1
# Eg:
    
order1=["Chicken","Mutton","Fish"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)


# Eg:
order=["Chicken","Mutton","Fish"]
order.extend("Mushroom")
print(order)


# 4. remove() function:
# We can use this function to remove specified item from the list.If the item present
# multiple times then only first occurrence will be removed.

n=[10,20,10,30]
n.remove(10)
print(n)


#If the specified item not present in list then we will get ValueError
n=[10,20,10,30]
n.remove(40)
print(n)
#ValueError: list.remove(x): x not in list

# Note: Hence before using remove() method first we have to check specified element
# present in the list or not by using in operator.

# 5. pop() function:
# It removes and returns the last element of the list.
# This is only function which manipulates list and returns some element.
# Eg:
    
n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n)

# If the list is empty then pop() function raises IndexError
# Eg:
n=[]
print(n.pop()) ==> IndexError: pop from empty list 


# Note:
# 1. pop() is the only function which manipulates the list and returns some value
# 2. In general we can use append() and pop() functions to implement stack datastructure
# by using list,which follows LIFO(Last In First Out) order.
# In general we can use pop() function to remove last element of the list. But we can use to
# remove elements based on index.
# n.pop(index)===>To remove and return element present at specified index.
# n.pop()==>To remove and return last element of the list

n=[10,20,30,40,50,60]
print(n.pop()) #60
print(n.pop(1)) #20
print(n.pop(10)) #==>IndexError: pop index out of range

# Differences between remove() and pop()
#  remove() 
# 1) We can use to remove special element
# from the List.
# 2) It can’t return any value.
# 3) If special element not available then we
# get VALUE ERROR.

# pop()
# 1) We can use to remove last element
# from the List.
# 2) It returned removed element.
# 3) If List is empty then we get Error.


# Note:
# List objects are dynamic. i.e based on our requirement we can increase and decrease the
# size.
# append(),insert() ,extend() ===>for increasing the size/growable nature
# remove(), pop() ======>for decreasing the size /shrinking nature



# III. Ordering elements of List:
    
    
1. reverse():
We can use to reverse() order of elements of list.

    
n=[10,20,30,40]
n.reverse()
print(n)


# 2. sort() function:
# In list by default insertion order is preserved. If want to sort the elements of list according
# to default natural sorting order then we should go for sort() method.
# For numbers ==>default natural sorting order is Ascending Order
# For Strings ==> default natural sorting order is Alphabetical Order


n=[20,5,15,10,0]
n.sort()
print(n) #[0,5,10,15,20]

s=["Dog","Banana","Cat","Apple"]
s.sort()
print(s) #['Apple','Banana','Cat','Dog']


# Note: To use sort() function, compulsory list should contain only homogeneous elements.
# otherwise we will get TypeError
# Eg:
n=[20,10,"A","B"]
n.sort()
print(n) # TypeError: '<' not supported between instances of 'str' and 'int' 


# To sort in reverse of default natural sorting order:
# We can sort according to reverse of default natural sorting order by using reverse=True
# argument.
# Eg:
    
n=[40,10,30,20]
n.sort()
print(n) #==>[10,20,30,40]
n.sort(reverse=True)
print(n) #===>[40,30,20,10]
n.sort(reverse=False)
print(n) #==>[10,20,30,40]

# Aliasing and Cloning of List objects:
# The process of giving another reference variable to the existing list is called aliasing.
# Eg:
    
x=[10,20,30,40]
y=x
print(id(x))
print(id(y))



# The problem in this approach is by using one reference variable if we are changing
# content,then those changes will be reflected to the other reference variable.

x=[10,20,30,40]
y=x
y[1]=777
print(x) #==>[10,777,30,40]

# To overcome this problem we should go for cloning.
# The process of creating exactly duplicate independent object is called cloning.
# We can implement cloning by using slice operator or by using copy() function


# 1. By using slice operator:    
x=[10,20,30,40]
y=x[:]
y[1]=777
print(x) #==>[10,20,30,40]
print(y) #==>[10,777,30,40] 
    
# 2. By using copy() function:    
x=[10,20,30,40]
y=x.copy()
y[1]=777
print(x) #==>[10,20,30,40]
print(y) #==>[10,777,30,40]     
    
# Q. Difference between = operator and copy() function
# = operator meant for aliasing
# copy() function meant for cloning    
    
# Using Mathematical operators for List Objects:
# We can use + and * operators for List objects.

1. Concatenation operator(+):
We can use + to concatenate 2 lists into a single list

a=[10,20,30]
b=[40,50,60]
c=a+b
print(c) #==>[10,20,30,40,50,60]

# Note: To use + operator compulsory both arguments should be list objects,otherwise we
# will get TypeError.
# Eg:

c=a+40 #==>TypeError: can only concatenate list (not "int") to list
c=a+[40] #==>valid

# 2. Repetition Operator(*):
# We can use repetition operator * to repeat elements of list specified number of times
# Eg:
x=[10,20,30]
y=x*3
print(y)#==>[10,20,30,10,20,30,10,20,30]


# Comparing List objects
# We can use comparison operators for List objects.
# Eg:

x=["Dog","Cat","Rat"]
y=["Dog","Cat","Rat"]
z=["DOG","CAT","RAT"]
print(x==y) #True
print(x==z) #False
print(x!= z) #True     
    
# Note:
# Whenever we are using comparison operators(==,!=) for List objects then the following
# should be considered
#  1. The number of elements
#  2. The order of elements
#  3. The content of elements (case sensitive)
 
 
# Note: When ever we are using relatational operators(<,<=,>,>=) between List objects,only
# first element comparison will be performed.
# Eg:
    
x=[50,20,30]
y=[40,50,60,100,200]
print(x>y) #True
print(x>=y) #True
print(x<y) #False
print(x<=y) #False

# Eg:
    
x=["Dog","Cat","Rat"]
y=["Rat","Cat","Dog"]
print(x>y) #False
print(x>=y) #False
print(x<y) #True
print(x<=y) #True    
    
# Membership operators:
# We can check whether element is a member of the list or not by using memebership
# operators.
# in operator
# not in operator
# Eg:
 
n=[10,20,30,40]
print (10 in n)
print (10 not in n)
print (50 in n)
print (50 not in n)     
    
# clear() function:
# We can use clear() function to remove all elements of List.
# Eg:
n=[10,20,30,40]
print(n)
n.clear()
print(n)

# Nested Lists:
# Sometimes we can take one list inside another list. Such type of lists are called nested
# lists.
# Eg:
    
n=[10,20,[30,40]]
print(n)
print(n[0])
print(n[2])
print(n[2][0])
print(n[2][1])

# Note: We can access nested list elements by using index just like accessing multi
# dimensional array elements.    
    
    
# Nested List as Matrix:
# In Python we can represent matrix by using nested lists.

n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print("Elements by Row wise:")
for r in n:
    print(r)


print("Elements by Matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()

    
# List Comprehensions:
# It is very easy and compact way of creating list objects from any iterable objects(like
# list,tuple,dictionary,range etc) based on some condition.
# Syntax:
# list=[expression for item in list if condition]
# Eg:
    
    
s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)

# Eg:
words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[0] for w in words]
print(l)

Eg:
num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[ i for i in num1 if i not in num2]
print(num3) 

common elements present in num1 and num2
num4=[i for i in num1 if i in num2]
print(num4) #[30, 40]


# Eg:
words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)


# Q. Write a program to display unique vowels present in the given word?

vowels=['a','e','i','o','u']
word=input("Enter the word to search for vowels: ")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
                found.append(letter)
print(found)
print("The number of different vowels present in",word,"is",len(found))     
    

# =============================================================================
# Tuple Data Structure
# 1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple
# object,we cannot perform any changes in that object.
# Hence Tuple is Read Only version of List.
# 2. If our data is fixed and never changes then we should go for Tuple.
# 3. Insertion Order is preserved
# 4. Duplicates are allowed
# 5. Heterogeneous objects are allowed.
# 6. We can preserve insertion order and we can differentiate duplicate objects by using
# index. Hence index will play very important role in Tuple also.
# Tuple support both +ve and -ve index. +ve index means forward direction(from left to
# right) and -ve index means backward direction(from right to left)
# 7. We can represent Tuple elements within Parenthesis and with comma seperator.
#  Parenethesis are optional but recommended to use.
# 
# =============================================================================

t=10,20,30,40
print(t)
print(type(t))


# Note: We have to take special care about single valued tuple.compulsary the value
# should ends with comma,otherwise it is not treated as tuple.
# Eg:
t=(10)
print(t)
print(type(t))



. Which of the following are valid tuples?
t=()
t=10,20,30,40
t=10
t=10,
t=(10)
t=(10,)
t=(10,20,30,40)


# Tuple creation:
t=()
# creation of empty tuple
t=(10,)
t=10,
# creation of single valued tuple ,parenthesis are optional,should ends with comma
t=10,20,30
t=(10,20,30)
# creation of multi values tuples & parenthesis are optional
# By using tuple() function:
list=[10,20,30]
t=tuple(list)
print(t)

t=tuple(range(10,20,2))
print(t)


# Accessing elements of tuple:
# We can access either by index or by slice operator

# 1. By using index:
    
t=(10,20,30,40,50,60)
print(t[0]) #10
print(t[-1]) #60
print(t[100]) #IndexError: tuple index out of range


# 2. By using slice operator:
    
t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
print(t[::2])

# Tuple vs immutability:
# Once we creates tuple,we cannot change its content.
# Hence tuple objects are immutable.
# Eg:
t=(10,20,30,40)
t[1]=70 #TypeError: 'tuple' object does not support item assignment

# Mathematical operators for tuple:
# We can apply + and * operators for tuple

# 1. Concatenation Operator(+): 
    
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3) # (10,20,30,40,50,60)


# 2. Multiplication operator or repetition operator(*)

t1=(10,20,30)
t2=t1*3
print(t2) #(10,20,30,10,20,30,10,20,30)

# Important functions of Tuple:
# 1. len()
# To return number of elements present in the tuple
# Eg:

t=(10,20,30,40)
print(len(t)) #4

# 2. count()
# To return number of occurrences of given element in the tuple
# Eg:
 
t=(10,20,10,10,20)
print(t.count(10)) #3

# 3. index()
# returns index of first occurrence of the given element.
# If the specified element is not available then we will get ValueError.
# Eg:
 
t=(10,20,10,10,20)
print(t.index(10)) #0
print(t.index(30)) #0ValueError: tuple.index(x): x not in tuple
 
# 4. sorted()
# To sort elements based on default natural sorting order

t=(40,10,30,20)
t1=sorted(t)
print(t1)
print(t)

We can sort according to reverse of default natural sorting order as follows


t1=sorted(t,reverse=True)
print(t1) [40, 30, 20, 10]


# 5. min() and max() functions:
# These functions return min and max values according to default natural sorting order.
# Eg:
    
t=(40,10,30,20)
print(min(t)) #10
print(max(t)) #40

# 6. cmp():
# It compares the elements of both tuples.
# If both tuples are equal then returns 0
# If the first tuple is less than second tuple then it returns -1
# If the first tuple is greater than second tuple then it returns +1
# Eg:
    
t1=(10,20,30)
t2=(40,50,60)
t3=(10,20,30)
print(cmp(t1,t2)) # -1
print(cmp(t1,t3)) # 0
print(cmp(t2,t3)) # +1

# Note: cmp() function is available only in Python2 but not in Python 3


# Tuple Packing and Unpacking:
# We can create a tuple by packing a group of variables.
# Eg:
    
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t) #(10, 20, 30, 40)

# Here a,b,c,d are packed into a tuple t. This is nothing but tuple packing


# Tuple unpacking is the reverse process of tuple packing
# We can unpack a tuple and assign its values to different variables
# Eg:
    
t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)

# Note: At the time of tuple unpacking the number of variables and number of values
# should be same. ,otherwise we will get ValueError.
# Eg:
    
    
t=(10,20,30,40)
a,b,c=t  #ValueError: too many values to unpack (expected 3)

# Tuple Comprehension:
# Tuple Comprehension is not supported by Python.
t= (x**2 for x in range(1,6))

# Here we are not getting tuple object and we are getting generator object.


t= (x**2 for x in range(1,6))
print(type(t))
for x in t:
    print(x)



Q. Write a program to take a tuple of numbers from the keyboard and print its sum and
average?

t=eval(input("Enter Tuple of Numbers:"))
l=len(t)
sum=0
for x in t:
    sum=sum+x
    print("The Sum=",sum)
    print("The Average=",sum/l)

# Differences between List and Tuple:
# List and Tuple are exactly same except small difference: List objects are mutable where as
# Tuple objects are immutable.
# In both cases insertion order is preserved, duplicate objects are allowed, heterogenous
# objects are allowed, index and slicing are supported.


# List Vs Tuple
# 1) List is a Group of Comma separeated
# Values within Square Brackets and Square
# Brackets are mandatory.
# Eg: i = [10, 20, 30, 40]
# 1) Tuple is a Group of Comma separeated
# Values within Parenthesis and Parenthesis
# are optional.
# Eg: t = (10, 20, 30, 40)
#   t = 10, 20, 30, 40
# 2) List Objects are Mutable i.e. once we
# creates List Object we can perform any
# changes in that Object.
# Eg: i[1] = 70
# 2) Tuple Objeccts are Immutable i.e. once
# we creates Tuple Object we cannot change
# its content.
# t[1] = 70  ValueError: tuple object does
# not support item assignment.
# 3) If the Content is not fixed and keep on
# changing then we should go for List.
# 3) If the content is fixed and never changes
# then we should go for Tuple.
# 4) List Objects can not used as Keys for
# Dictionries because Keys should be
# Hashable and Immutable.
# 4) Tuple Objects can be used as Keys for
# Dictionries because Keys should be
# Hashable and Immutable.



# =============================================================================
# Set Data Structure
#  If we want to represent a group of unique values as a single entity then we should go
# for set.
#  Duplicates are not allowed.
#  Insertion order is not preserved.But we can sort the elements.
#  Indexing and slicing not allowed for the set.
#  Heterogeneous elements are allowed.
#  Set objects are mutable i.e once we creates set object we can perform any changes in
# that object based on our requirement.
#  We can represent set elements within curly braces and with comma seperation
#  We can apply mathematical operations like union,intersection,difference etc on set
# objects.
# =============================================================================
# Creation of Set objects:
# Eg:
s={10,20,30,40}
print(s)
print(type(s))

# We can create set objects by using set() function

# s=set(any sequence)

# Eg 1:
l = [10,20,30,40,10,20,10]
s=set(l)
print(s) # {40, 10, 20, 30}

# Eg 2:
    
s=set(range(5))
print(s) #{0, 1, 2, 3, 4}

# Note: While creating empty set we have to take special care.
# Compulsory we should use set() function.


s={} #==>It is treated as dictionary but not empty set.
# Eg:
s={}
print(s)
print(type(s))

# Eg:
    
s=set()
print(s)
print(type(s))

# Important functions of set:
# 1. add(x):
# Adds item x to the set
# Eg:
    
s={10,20,30}
s.add(40);
print(s) #{40, 10, 20, 30}

# 2. update(x,y,z):
# To add multiple items to the set.
# Arguments are not individual elements and these are Iterable objects like List,range etc.
# All elements present in the given Iterable objects will be added to the set.
# Eg:
    
s={10,20,30}
l=[40,50,60,10]
s.update(l,range(5))
print(s)


# Q. What is the difference between add() and update() functions in set?
# We can use add() to add individual item to the Set,where as we can use update()
 # function to add multiple items to Set.
# add() function can take only one argument where as update() function can take any
# number of arguments but all arguments should be iterable objects.

Q. Which of the following are valid for set s?

s.add(10)
s.add(10,20,30) #TypeError: add() takes exactly one argument (3 given)
s.update(10) #TypeError: 'int' object is not iterable
s.update(range(1,10,2),range(0,10,2))

# 3. copy():
# Returns copy of the set.
# It is cloned object.

s={10,20,30}
s1=s.copy()
print(s1)

# 4. pop():
# It removes and returns some random element from the set.
# Eg:
    
s={40,10,30,20}
print(s)
print(s.pop())
print(s)


# 5. remove(x):
# It removes specified element from the set.
# If the specified element not present in the Set then we will get KeyError

s={40,10,30,20}
s.remove(30)
print(s)  # {40, 10, 20}
s.remove(50) #==>KeyError: 50

# 6. discard(x):
# It removes the specified element from the set.
# If the specified element not present in the set then we won't get any error.

s={10,20,30}
s.discard(10)
print(s)  #===>{20, 30}
s.discard(50)
print(s)  #==>{20, 30}




# Q. What is the difference between remove() and discard() functions in Set?
# Q. Explain differences between pop(),remove() and discard() functionsin Set?

# 7.clear():
# To remove all elements from the Set.
s={10,20,30}
print(s)
s.clear()
print(s)

# Mathematical operations on the Set:
# 1.union():
# x.union(y) ==>We can use this function to return all elements present in both sets
# x.union(y) or x|y
# Eg:
    
x={10,20,30,40}
y={30,40,50,60}
print(x.union(y)) #{10, 20, 30, 40, 50, 60}
print(x|y) #{10, 20, 30, 40, 50, 60}

# 2. intersection():
# x.intersection(y) or x&y
# Returns common elements present in both x and y
# Eg:  
x={10,20,30,40}
y={30,40,50,60}
print(x.intersection(y)) #{40, 30}
print(x&y) #{40, 30}

# 3. difference():
# x.difference(y) or x-y
# returns the elements present in x but not in y
# Eg:    
x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y)) #{10, 20}
print(x-y) #{10, 20}
print(y-x) #{50, 60}

# 4.symmetric_difference():
# x.symmetric_difference(y) or x^y
# Returns elements present in either x or y but not in both
# Eg:    
x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y)) #{10, 50, 20, 60}
print(x^y) #{10, 50, 20, 60}


Membership operators: (in , not in)
Eg:
    
s=set("John")
print(s)
print('d' in s)
print('z' in s)

# Set Comprehension:
# Set comprehension is possible.
s={x*x for x in range(5)}
print(s) #{0, 1, 4, 9, 16}
s={2**x for x in range(2,10,2)}
print(s)  #{16, 256, 64, 4}

# set objects won't support indexing and slicing:
# Eg:
s={10,20,30,40}
print(s[0]) #==>TypeError: 'set' object does not support indexing
print(s[1:3]) #==>TypeError: 'set' object is not subscriptable


# Q.Write a program to eliminate duplicates present in the list?

# Approach-1:    
l=eval(input("Enter List of values: "))
s=set(l)
print(s)

# Approach-2:
l=eval(input("Enter List of values: "))
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
    print(l1)

# Q. Write a program to print different vowels present in the given word?
w=input("Enter word to search for vowels: ")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("The different vowel present in",w,"are",d)



# =============================================================================
# Dictionary Data Structure
#  We can use List,Tuple and Set to represent a group of individual objects as a single entity.
#  If we want to represent a group of objects as key-value pairs then we should go for
# Dictionary.
#  Eg:
#  rollno----name
#  phone number--address
#  ipaddress---domain name
# Duplicate keys are not allowed but values can be duplicated.
# Hetrogeneous objects are allowed for both key and values.
# insertion order is not preserved
# Dictionaries are mutable
# Dictionaries are dynamic
# indexing and slicing concepts are not applicable
# Note: In C++ and Java Dictionaries are known as "Map" where as in Perl and Ruby it is
# known as "Hash"
# =============================================================================
# How to create Dictionary?
d={}
# or 
d=dict()

# we are creating empty dictionary. We can add entries as follows
d[100]="Timmy"
d[200]="ravi"
d[300]="shiva"
print(d) #{100: 'durga', 200: 'ravi', 300: 'shiva'}

# If we know data in advance then we can create dictionary as follows

d={100:'timmy' ,200:'ravi', 300:'shiva'}

# d={key:value, key:value}

# How to access data from the dictionary?
# We can access data by using keys.


d={100:'timmy' ,200:'ravi', 300:'shiva'}
print(d[100]) 
print(d[300]) #shiva

# If the specified key is not available then we will get KeyError
print(d[400]) # KeyError: 400

# We can prevent this by checking whether key is already available or not by using
# has_key() function or by using in operator.

d.has_key(400) #==> returns 1 if key is available otherwise returns 0

# But has_key() function is available only in Python 2 but not in Python 3. Hence
# compulsory we have to use in operator.
if 400 in d:
    print(d[400])


# Q. Write a program to enter name and percentage marks in a dictionary and
# display information on the screen
rec={}
n=int(input("Enter number of students: "))
i=1
while i<=n:
    name=input("Enter Student Name: ")
    marks=input("Enter % of Marks of Student: ")
    rec[name]=marks
    i=i+1
    print("Name of Student","\t","% of marks")

for x in rec:
    print("\t",x,"\t\t",rec[x])


# How to update dictionaries?
# d[key]=value
# If the key is not available then a new entry will be added to the dictionary with the
# specified key-value pair
# If the key is already available then old value will be replaced with new value.

# Eg:
d={100:"Timmy",200:"ravi",300:"shiva"}
print(d)
d[400]="pavan"
print(d)
d[100]="sunny"
print(d)

# How to delete elements from dictionary?
# del d[key]
#  It deletes entry associated with the specified key.
#  If the key is not available then we will get KeyError
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d)
del d[100]
print(d)
del d[400]

# d.clear()
# To remove all entries from the dictionary

# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d)
d.clear()
print(d)

# del d
# To delete total dictionary.Now we cannot access d
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d)
del d
print(d)

# Important functions of dictionary:
# 1. dict():
# To create a dictionary

d=dict() #===>It creates empty dictionary
d=dict({100:"John",200:"ravi"}) #==>It creates dictionary with specified elements
d=dict([(100,"John"),(200,"shiva"),(300,"ravi")])#==>It creates dictionary with the given
#list of tuple elements


# 2. len()
# Returns the number of items in the dictionary

# 3. clear():
# To remove all elements from the dictionary

# 4. get():
# To get the value associated with the key
# d.get(key)
#  If the key is available then returns the corresponding value otherwise returns None.It
# wont raise any error.
# d.get(key,defaultvalue)
#  If the key is available then returns the corresponding value otherwise returns default
# value.
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d[100]) 
print(d[400]) ==>KeyError:400
print(d.get(100)) 
print(d.get(400)) ==>None
print(d.get(100,"Guest")) 
print(d.get(400,"Guest")) #==>Guest

# 3. pop():
# d.pop(key)
#  It removes the entry associated with the specified key and returns the corresponding
# value
#  If the specified key is not available then we will get KeyError
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d.pop(100))
print(d)
print(d.pop(400))



# 4. popitem():
# It removes an arbitrary item(key-value) from the dictionaty and returns it.
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d)
print(d.popitem())
print(d)

# If the dictionary is empty then we will get KeyError
d={}
print(d.popitem()) #==>KeyError: 'popitem(): dictionary is empty'


# 5. keys():
# It returns all keys associated eith dictionary
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d.keys())
for k in d.keys():
    print(k)

# 6. values():
# It returns all values  associated with the dictionary
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d.values())
for v in d.values():
    print(v)

# 7. items():
# It returns list of tuples representing key-value pairs.
# [(k,v),(k,v),(k,v)]
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
for k,v in d.items():
print(k,"--",v)

# 8. copy():
# To create exactly duplicate dictionary(cloned copy)
d1=d.copy();


# 9. setdefault():
# d.setdefault(k,v)
#  If the key is already available then this function returns the corresponding value.
#  If the key is not available then the specified key-value will be added as new item to the
# dictionary.
# Eg:
d={100:"John",200:"ravi",300:"shiva"}
print(d.setdefault(400,"pavan"))
print(d)
print(d.setdefault(100,"sachin"))
print(d)


# 10. update():
# d.update(x)
# All items present in the dictionary x will be added to dictionary d


# Q. Write a program to take dictionary from the keyboard and print the sum
# of values?
d=eval(input("Enter dictionary:"))
s=sum(d.values())
print("Sum= ",s)

# Q. Write a program to find number of occurrences of each letter present in
# the given string?
word=input("Enter any word: ")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"occurred ",v," times")



# Q. Write a program to find number of occurrences of each vowel present in
# the given string?
word=input("Enter any word: ")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,"occurred ",v," times")

# Q. Write a program to accept student name and marks from the keyboard
# and creates a dictionary. Also display student marks by taking student name
# as input?
n=int(input("Enter the number of students: "))
d={}
for i in range(n):
    name=input("Enter Student Name: ")
    marks=input("Enter Student Marks: ")
    d[name]=marks
while True:
    name=input("Enter Student Name to get Marks: ")
    marks=d.get(name,-1)
    if marks== -1:
        print("Student Not Found")
    else:
        print("The Marks of",name,"are",marks)
    option=input("Do you want to find another student marks[Yes|No]")
    if option=="No":
        break
print("Thanks for using our application")


# Dictionary Comprehension:
# Comprehension concept applicable for dictionaries also.
squares={x:x*x for x in range(1,6)}
print(squares)
doubles={x:2*x for x in range(1,6)}
print(doubles)


# FUNCTIONS
# If a group of statements is repeatedly required then it is not recommended to write these
# statements everytime seperately.We have to define these statements as a single unit and
# we can call that unit any number of times based on our requirement without rewriting.
# This unit is nothing but function.
# The main advantage of functions is code Reusability.
# Note: In other languages functions are known as methods,procedures,subroutines etc
# Python supports 2 types of functions
# 1. Built in Functions
# 2. User Defined Functions

# 1. Built in Functions:
# The functions which are coming along with Python software automatically,are called built
# in functions or pre defined functions
# Eg:
id()
type()
input()
eval()
# etc..

# 2. User Defined Functions:
# The functions which are developed by programmer explicitly according to business
# requirements ,are called user defined functions.
# Syntax to create user defined functions:

def function_name(parameters) :
 """ doc string"""
 ----
 -----
  return value

# Note: While creating functions we can use 2 keywords
# 1. def (mandatory)
# 2. return (optional)
# Eg 1: Write a function to print Hello
# test.py:
def wish():
    print("Hello Good Morning")

wish()

# Parameters
# Parameters are inputs to the function. If a function contains parameters,then at the time
# of calling,compulsory we should provide values otherwise,otherwise we will get error.
# Eg: Write a function to take name of the student as input and print wish message by
# name.
def wish(name):
    print("Hello",name," Good Morning")

wish("John")
wish("Ravi")

# Eg: Write a function to take number as input and print its square value
def squareIt(number):
    print("The Square of",number,"is", number*number)

squareIt(4)
squareIt(5)

# Return Statement:
# Function can take input values as parameters and executes business logic, and returns
# output to the caller with return statement.


# Q. Write a function to accept 2 numbers as input and return sum.
def add(x,y):
    return x+y
result=add(10,20)
print("The sum is",result)
print("The sum is",add(100,200))

# If we are not writing return statement then default return value is None
# Eg:
def f1():
    print("Hello")
f1()
print(f1())

# Q. Write a function to check whether the given number is even or odd?
def even_odd(num):
    if num%2==0:
        print(num,"is Even Number")
    else:
        print(num,"is Odd Number")

even_odd(10)
even_odd(15)


# Q. Write a function to find factorial of given number?
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result

for i in range(1,5):
    print("The Factorial of",i,"is :",fact(i))


# Returning multiple values from a function:
# In other languages like C,C++ and Java, function can return atmost one value. But in
# Python, a function can return any number of values.
# Eg 1:
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub

x,y=sum_sub(100,50)
print("The Sum is :",x)
print("The Subtraction is :",y)

# Eg 2:
def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(100,50)
print("The Results are")

for i in t:
    print(i)


# Types of arguments
# def f1(a,b):
#  ------
#  ------
#  ------
f1(10,20)

# a,b are formal arguments where as 10,20 are actual arguments
# There are 4 types are actual arguments are allowed in Python.
# 1. positional arguments
# 2. keyword arguments
# 3. default arguments
# 4. Variable length arguments


# 1. positional arguments:
# These are the arguments passed to function in correct positional order.
def sub(a,b):
    print(a-b)

sub(100,200)
sub(200,100)

# The number of arguments and position of arguments must be matched. If we change the
# order then result may be changed.
# If we change the number of arguments then we will get error
    

# 2. keyword arguments:
# We can pass argument values by keyword i.e by parameter name.
# Eg:
def wish(name,msg):
    print("Hello",name,msg)

wish(name="John",msg="Good Morning")
wish(msg="Good Morning",name="John")

# Here the order of arguments is not important but number of arguments must be matched.
# Note:
# We can use both positional and keyword arguments simultaneously. But first we have to
# take positional arguments and then keyword arguments,otherwise we will get
# syntaxerror.
def wish(name,msg):
    print("Hello",name,msg)

wish("John","GoodMorning")  #==>valid
wish("John",msg="GoodMorning") #==>valid
wish(name="John","GoodMorning") #==>invalid 

# SyntaxError: positional argument follows keyword argument

# 3. Default Arguments:
# Sometimes we can provide default values for our positional arguments.
# Eg:

def wish(name="Guest"):
    print("Hello",name,"Good Morning")
 
wish("John")
wish()


    
# If we are not passing any name then only default value will be considered.
# ***Note:
# After default arguments we should not take non default arguments

def wish(name="Guest",msg="Good Morning") #===>Valid
def wish(name,msg="Good Morning") #===>Valid
def wish(name="Guest",msg)#==>Invalid

# SyntaxError: non-default argument follows default argument

# 4. Variable length arguments:
# Sometimes we can pass variable number of arguments to our function,such type of
# arguments are called variable length arguments.
# We can declare a variable length argument with * symbol as follows

def f1(*n):

# We can call this function by passing any number of arguments including zero number.
# Internally all these values represented in the form of tuple.
# Eg:
def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The Sum=",total)

# Note:
# We can mix variable length arguments with positional arguments.    
    
# Eg:
def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)

f1(10)
f1(10,20,30,40)
f1(10,"A",30,"B")

# Note: After variable length argument,if we are taking any other arguments then we
# should provide values as keyword arguments.
# Eg:
def f1(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)
 
f1("A","B",n1=10)
f1("A","B",10) #==>Invalid
# TypeError: f1() missing 1 required keyword-only argument: 'n1'

# Note: We can declare key word variable length arguments also.
# For this we have to use **.
# def f1(**n):        
# We can call this function by passing any number of keyword arguments. Internally these
# keyword arguments will be stored inside a dictionary.
# Eg:  
    
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)

display(n1=10,n2=20,n3=30)
display(rno=100,name="John",marks=70,subject="Java")

# Case Study:
def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)


f(3,2) #==> 3 2 4 8
f(10,20,30,40) #===>10 20 30 40
f(25,50,arg4=100) #==>25 50 4 100
f(arg4=2,arg1=3,arg2=4)#===>3 4 4 2
f()#===>Invalid 
#TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'

f(arg3=10,arg4=20,30,40)  #==>Invalid
# SyntaxError: positional argument follows keyword argument 
#[After keyword arguments we should not take positional arguments]

f(4,5,arg2=6)#==>Invalid
#TypeError: f() got multiple values for argument 'arg2'

f(4,5,arg3=5,arg5=6)#==>Invalid 
#TypeError: f() got an unexpected keyword argument 'arg5    
    
#   Note: Function vs Module vs Library:
# 1. A group of lines with some name is called a function
# 2. A group of functions saved to a file , is called Module
# 3. A group of Modules is nothing but Library  
# Types of Variables
# Python supports 2 types of variables.
# 1. Global Variables
# 2. Local Variables


# 1. Global Variables
# The variables which are declared outside of function are called global variables.
# These variables can be accessed in all functions of that module.
# Eg:
a=10 # global variable
def f1():
    print(a)
 
def f2():
    print(a)
 
f1()
f2()
   
    
# 2. Local Variables:
# The variables which are declared inside a function are called local variables.
# Local variables are available only for the function in which we declared it.i.e from outside
# of function we cannot access.
# Eg:
def f1():
    a=10
    print(a) # valid

def f2():
    print(a) #invalid

f1()
f2()
# NameError: name 'a' is not defined

# =============================================================================
# global keyword:
# We can use global keyword for the following 2 purposes:
# 1. To declare global variable inside function
# 2. To make global variable available to the function so that we can perform required
# modifications
# =============================================================================


# Eg 1:
a=10
def f1():
    a=777
    print(a)

def f2():
    print(a)

f1()
f2()
# 777
# 10

# Eg 2:
    
a=10
def f1():
    global a
    a=777
    print(a)

def f2():
    print(a)

f1()
f2()
# 777
# 777



# Eg 3:
    
def f1():
    a=10
    print(a)

def f2():
    print(a)
    
f1()
f2()
#NameError: name 'a' is not defined

# Eg 4:
def f1():
    global a
    a=10
    print(a)

def f2():
    print(a)

f1()
f2()
# 10
# 10   
    
# Note: If global variable and local variable having the same name then we can access
# global variable inside a function as follows

a=10 #global variable
def f1():
    a=777 #local variable
    print(a)
    print(globals()['a'])


f1()
# 777
# 10

# =============================================================================
# Recursive Functions
# A function that calls itself is known as Recursive Function.
# Eg:
# factorial(3)=3*factorial(2)
#  =3*2*factorial(1)
#  =3*2*1*factorial(0)
#  =3*2*1*1
#  =6
# factorial(n)= n*factorial(n-1) 
# The main advantages of recursive functions are:
# 1. We can reduce length of the code and improves readability
# 2. We can solve complex problems very easily.
# =============================================================================




# Q. Write a Python Function to find factorial of given number with recursion.
# Eg:
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("Factorial of 4 is :",factorial(4))
print("Factorial of 5 is :",factorial(5))

    

# =============================================================================
# Anonymous Functions:
# Sometimes we can declare a function without any name,such type of nameless functions
# are called anonymous functions or lambda functions.
# The main purpose of anonymous function is just for instant use(i.e for one time usage)
# 
# =============================================================================


# Normal Function:
# We can define by using def keyword.
# def squareIt(n):
#  return n*n

# lambda Function:
# We can define by using lambda keyword
# lambda n:n*n

# Syntax of lambda Function:
# lambda argument_list : expression

# Note: By using Lambda Functions we can write very concise code so that readability of
# the program will be improved.


# Q. Write a program to create a lambda function to find square of given
# number?
s=lambda n:n*n
print("The Square of 4 is :",s(4))
print("The Square of 5 is :",s(5)) 


# Q. Lambda function to find sum of 2 given numbers
s=lambda a,b:a+b
print("The Sum of 10,20 is:",s(10,20))
print("The Sum of 100,200 is:",s(100,200))


# Q. Lambda Function to find biggest of given values.
s=lambda a,b:a if a>b else b
print("The Biggest of 10,20 is:",s(10,20))
print("The Biggest of 100,200 is:",s(100,200))



# Note:
# Lambda Function internally returns expression value and we are not required to write
# return statement explicitly.
# Note: Sometimes we can pass function as argument to another function. In such cases
# lambda functions are best choice.
# We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z
# these functions expect function as argument.


# =============================================================================
# filter() function:     
# We can use filter() function to filter values from the given sequence based on some
# condition.
# filter(function,sequence)
#  where function argument is responsible to perform conditional check
#  sequence can be list or tuple or string. 
# =============================================================================

# Q. Program to filter only even numbers from the list by using filter()
# function?

without lambda Function:

def isEven(x):
    if x%2==0:
        return True
    else:
        return False

l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1) #[0,10,20,30]

with lambda Function:
    
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1) #[0,10,20,30]

l2=list(filter(lambda x:x%2!=0,l))
print(l2) #[5,15,25] 



# =============================================================================
# map() function:
# For every element present in the given sequence,apply some functionality and generate
# new element with the required modification. For this requirement we should go for
# map() function.
# =============================================================================


# Eg: For every element present in the list perform double and generate new list of doubles.

# Syntax:
# map(function,sequence)

# The function can be applied on each element of sequence and generates new sequence.

# Eg: Without lambda

l=[1,2,3,4,5]
def doubleIt(x):
    return 2*x
l1=list(map(doubleIt,l))
print(l1) #[2, 4, 6, 8, 10]

# with lambda
l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1) #[2, 4, 6, 8, 10] 


# Eg 2: To find square of given numbers
l=[1,2,3,4,5]
l1=list(map(lambda x:x*x,l))
print(l1) #[1, 4, 9, 16, 25]


# We can apply map() function on multiple lists also.But make sure all list should have same
# length.
# Syntax: map(lambda x,y:x*y,l1,l2))
# x is from l1 and y is from l2
# Eg:
    
l1=[1,2,3,4]
l2=[2,3,4,5]
l3=list(map(lambda x,y:x*y,l1,l2))
print(l3) #[2, 6, 12, 20]



# =============================================================================
# reduce() function:
# reduce() function reduces sequence of elements into a single element by applying the
# specified function.
# reduce(function,sequence)
# reduce() function present in functools module and hence we should write import
# statement.
# Eg:
# =============================================================================
from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result) # 150

# Eg:    
result=reduce(lambda x,y:x*y,l)
print(result) #12000000

# Eg:
from functools import *
result=reduce(lambda x,y:x+y,range(1,101))
print(result) #5050 


# Note:
#  In Python every thing is treated as object.
#  Even functions also internally treated as objects only.
# Eg:

def f1():
    print("Hello")

print(f1)
print(id(f1))

# =============================================================================
# Function Aliasing:
# For the existing function we can give another name, which is nothing but function aliasing.
# Eg:
# =============================================================================
def wish(name):
    print("Good Morning:",name)

greeting=wish

print(id(wish))

print(id(greeting))

greeting('Johnny')
wish('Johnny')

# Note: In the above example only one function is available but we can call that function by using
# either wish name or greeting name.
# If we delete one name still we can access that function by using alias name
# Eg:
def wish(name):
  print("Good Morning:",name)



greeting=wish

greeting('Johnny')
wish('Johnny')



del wish
#wish('Durga') ==>NameError: name 'wish' is not defined
greeting('Pavan')

# =============================================================================
# Nested Functions:
# We can declare a function inside another function, such type of functions are called Nested
# functions.
# Eg:
# =============================================================================
def outer():
    print("outer function started")
    def inner():
        print("inner function execution")
        print("outer function calling inner function")

inner()
outer()
#inner() ==>NameError: name 'inner' is not defined


# In the above example inner() function is local to outer() function and hence it is not possible to call
# directly from outside of outer() function.

# Note: A function can return another function.


# Eg:

    
def outer():
    print("outer function started")
    def inner():
        print("inner function execution") 
    print("outer function returning inner function")
    return inner

f1=outer()
f1()
# or
f1=outer()()
f1

# inner function execution
# Q. What is the differenece between the following lines?
#  f1 = outer
#  f1 = outer()
#  In the first case for the outer() function we are providing another name f1(function aliasing).
#  But in the second case we calling outer() function,which returns inner function.For that inner
# function() we are providing another name f1
# Note: We can pass function as argument to another function
# Eg: filter(function,sequence)
#  map(function,sequence)
#  reduce(function,sequence)




# =============================================================================
# Function Decorators:
# Decorator is a function which can take a function as argument and extend its functionality
# and returns modified function with extended functionality.
# =============================================================================


Input Function-------->Decorator --------> new(add some functionality) 
 wish()                                          inner()


Input Function-------->Decorator Function-------->  output function with extended functionality) 


# The main objective of decorator functions is we can extend the functionality of existing
# functions without modifies that function.
def wish(name):
    print("Hello",name,"Good Morning")

# This function can always print same output for any name

# Hello Ravi Good Morning
# Hello Sunny Good Morning

# But we want to modify this function to provide different message if name is Sunny.
# We can do this without touching wish() function by using decorator.


def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Hello",name,"Good Morning")

wish("John")
wish("Ravi")
wish("Sunny") 

# In the above program whenever we call wish() function automatically decor function will
# be executed.
# How to call same function with decorator and without decorator:
# We should not use @decor
def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello",name,"Good Morning")

decorfunction=decor(wish)

wish("John") #decorator wont be executed
wish("Sunny") #decorator wont be executed
# Hello John Good Morning
# Hello Sunny Good Morning

decorfunction("John") #decorator will be executed
decorfunction("Sunny") #decorator will be executed
# Hello John Good Morning
# Hello Sunny Bad Morning

# Eg 2:
def smart_division(func):
    def inner(a,b):
        print("We are dividing",a,"with",b)
        if b==0:
            print("OOPS...cannot divide")
            return
        else:
            return func(a,b) 
    return inner

@smart_division
def division(a,b):
    return a/b

print(division(20,2))
# We are dividing 20 with 2
# 10.0

print(division(20,0))
# We are dividing 20 with 0
# OOPS...cannot divide
# None


# without decorator we will get Error.In this case output is:

# with decorator we won't get any error. In this case output is:
# We are dividing 20 with 2
# 10.0
# We are dividing 20 with 0
# OOPS...cannot divide
# None


# =============================================================================
# # Decorator Chaining
# # We can define multiple decorators for the same function and all these decorators will
# # form Decorator Chaining.
# =============================================================================
# Eg:
# @decor1
# @decor
# def num():
# For num() function we are applying 2 decorator functions. First inner decorator will work
# and then outer decorator.
# Eg:
def decor1(func):
    def inner():
        x=func()
        return x*x 
    return inner

def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor
def num():
    return 10
print(num())


# Demo Program for decorator Chaining:
def decor1(func):
    def inner(name):
        print("Second Decor(decor1) Execution")
        func(name)
    return inner
    

def decor(func):
    def inner(name):
        print("First Decor(decor) Function Execution")
        func(name)
    return inner



@decor1
@decor
def wish(name):
    print("Hello",name,"Good Morning")

wish("John") 

# Second Decor(decor1) Execution
# First Decor(decor) Function Execution
# Hello John Good Morning




# =============================================================================
# Generators
# Generator is a function which is responsible to generate a sequence of values.
# We can write generator functions just like ordinary functions, but it uses yield keyword to
# return values.
# 
# 
# =============================================================================


def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g=mygen()
print(type(g))
# <class 'generator'>
print(next(g))
# A
print(next(g))
# B
print(next(g))
# B
print(next(g))
# StopIteration


def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num
        num=num-1

values=countdown(5)
for x in values: 
    print(x) 


# Eg 3: To generate first n numbers:
    
def firstn(num):
    n=1
    while n<=num:
        yield n
        n=n+1

values=firstn(5)
for x in values:
    print(x) 


# We can convert generator into list as follows:
    
values=firstn(10)
l1=list(values)
print(l1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Eg 4: To generate Fibonacci Numbers...

# The next is the sum of previous 2 numbers
# Eg: 0,1,1,2,3,5,8,13,21,...

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>100:
        break
    print(f)


# Advantages of Generator Functions:
# 1. when compared with class level iterators, generators are very easy to use
# 2. Improves memory utilization and performance.
# 3. Generators are best suitable for reading data from large number of large files
# 4. Generators work great for web scraping and crawling.



import random
import time

names = ['Sunny','Bunny','Chinny','Vinny']
subjects = ['Python','Java','Blockchain']

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {'id':i,
                  'name': random.choice(names),
                  'subject':random.choice(subjects)
                  }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person = {'id':i,
                  'name': random.choice(names),
                  'major':random.choice(subjects) 
                  }
        yield person

'''''t1 = time.clock()
people = people_list(10000000)
t2 = time.clock()'''

t1 = time.clock()
people = people_generator(10000000)
t2 = time.clock()
print('Took {}'.format(t2-t1)) 

# Note: In the above program observe the differnce wrt execution time by using list and generators
# Generators vs Normal Collections wrt Memory Utilization:
# Normal Collection:
    
l=[x*x for x in range(10000000000000000)]
print(l[0])

# We will get MemoryError in this case because all these values are required to store in the memory.
# Generators:
g=(x*x for x in range(10000000000000000))
print(next(g))
# Output: 0
# We won't get any MemoryError because the values won't be stored at the beginning



# Modules
# A group of functions, variables and classes saved to a file, which is nothing but module.
# Every Python file (.py) acts as a module.


# Eg: techmath.py
x=888
def add(a,b):
    print("The Sum:",a+b)

def product(a,b):
    print("The Product:",a*b)


# techmath module contains one variable and 2 functions.
# If we want to use members of module in our program then we should import that module.
# import modulename
# We can access members by using module name.
# modulename.variable
# modulename.function()

# test.py:
import techmath
print(techmath.x)
techmath.add(10,20)
techmath.product(10,20)


# Note:
# whenever we are using a module in our program, for that module compiled file will be
# generated and stored in the hard disk permanently.
# Renaming a module at the time of import (module aliasing):
# Eg:
    
import techmath as m
# here techmath is original module name and m is alias name.
# We can access members by using alias name m
# test.py:
import techmath as m
print(m.x)
m.add(10,20)
m.product(10,20)


# from ... import:
# We can import particular members of module by using from ... import .
# The main advantage of this is we can access members directly without using module
# name.
# Eg:
    
    
from techmath import x,add
print(x)
add(10,20)
product(10,20)#==> NameError: name 'product' is not defined

# We can import all members of a module as follows
from techmath import *
# test.py:
from techmath import *
print(x)
add(10,20)
product(10,20)


# Various possibilties of import:
# import modulename
# import module1,module2,module3
# import module1 as m
# import module1 as m1,module2 as m2,module3
# from module import member
# from module import member1,member2,memebr3
# from module import memeber1 as x
# from module import *
# member aliasing:

    
from techmath import x as y,add as sum
print(y)
sum(10,20)


# Once we defined as alias name,we should use alias name only and we should not use
# original name
# Eg:
from techmath import x as y
print(x) #==>NameError: name 'x' is not defined

# Reloading a Module:
# By default module will be loaded only once eventhough we are importing multiple
# multiple times.

# Demo Program for module reloading:
import time
from imp import reload
import module1
time.sleep(30)
reload(module1)
time.sleep(30)
reload(module1)
print("This is test file")

# Note: In the above program, everytime updated version of module1 will be available to
# our program


# module1.py:
print("This is from module1")

# test.py
import module1
import module1
import module1
import module1
print("This is test module")


# In the above program test module will be loaded only once eventhough we are importing
# multiple times.
# The problem in this approach is after loading a module if it is updated outside then
# updated version of module1 is not available to our program.
# We can solve this problem by reloading module explicitly based on our requirement.
# We can reload by using reload() function of imp module.
import imp
imp.reload(module1)

test.py:
import module1
import module1
from imp import reload
reload(module1)
reload(module1)
reload(module1)
print("This is test module")

# In the above program module1 will be loaded 4 times in that 1 time by default and 3 times
# explicitly. In this case output is
# 1) This is from module1
# 2) This is from module1
# 3) This is from module1
# 4) This is from module1
# 5) This is test module


# The main advantage of explicit module reloading is we can ensure that updated version is
# always available to our program.

# Finding members of module by using dir() function:
# Python provides inbuilt function dir() to list out all members of current module or a
# specified module.
# dir() ===>To list out all members of current module
# dir(moduleName)==>To list out all members of specified module


# Eg 1: test.py
x=10
y=20
def f1():
    print("Hello")
print(dir()) # To print all members of current module

# Eg 2: To display members of particular module:
    
# techmath.py:
x=888
def add(a,b):
    print("The Sum:",a+b)

def product(a,b):
    print("The Product:",a*b)

# test.py:    
import techmath
print(dir(techmath))

# Note: For every module at the time of execution Python interpreter will add some special
# properties automatically for internal use.

# Eg: __builtins__,__cached__,'__doc__,__file__, __loader__, __name__,__package__,
# __spec__
# Based on our requirement we can access these properties also in our program.

# Eg: test.py:
print(__builtins__ )
print(__cached__ )
print(__doc__)
print(__file__)
print(__loader__)
print(__name__)
print(__package__)
print(__spec__)

test.py
# 1) <_frozen_importlib_external.SourceFileLoader object at 0x00572170>
# 2) __main__
# 3) None
# 4) None 

# =============================================================================
# The Special variable __name__:
# For every Python program , a special variable __name__ will be added internally.
# This variable stores information regarding whether the program is executed as an
# individual program or as a module.
# If the program executed as an individual program then the value of this variable is
# __main__
# If the program executed as a module from some other program then the value of this
# variable is the name of module where it is defined.
# Hence by using this __name__ variable we can identify whether the program executed
# directly or as a module.
# 
# =============================================================================


# Demo program:    
# module1.py:
def f1():
    if __name__=='__main__':
        print("The code executed as a program")
    else:
        print("The code executed as a module from some other program")
f1()

# test.py:
import module1
module1.f1()


# =============================================================================
# Working with math module:
# Python provides inbuilt module math.
# This module defines several functions which can be used for mathematical operations.
# The main important functions are
# 1. sqrt(x)
# 2. ceil(x)
# 3. floor(x)
# 4. fabs(x)
# 5.log(x)
# 6. sin(x)
# 7. tan(x)
# =============================================================================
# Eg:
from math import *
print(sqrt(4))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6)) 


# Note:
# We can find help for any module by using help() function
# Eg:
import math
help(math)

# =============================================================================
# Working with random module:
# This module defines several functions to generate random numbers.
# We can use these functions while developing games,in cryptography and to generate
# random numbers on fly for authentication.
# =============================================================================
# 1. random() function:
#  This function always generate some float value between 0 and 1 ( not inclusive)
#  0<x<1

# Eg:
from random import *
for i in range(10):
    print(random()) 


# 2. randint() function:
# To generate random integer beween two given numbers(inclusive)
# Eg:
from random import *
for i in range(10):
    print(randint(1,100)) # generate random int value between 1 and 100(inclusive)

# 3. uniform():
#  It returns random float values between 2 given numbers(not inclusive)
# Eg:
from random import *
for i in range(10):
    print(uniform(1,10))

# random() ===>in between 0 and 1 (not inclusive)
# randint(x,y) ==>in between x and y (inclusive)
# uniform(x,y) ==> in between x and y (not inclusive)


# 4. randrange([start],stop,[step])
#  returns a random number from range
#  start<= x < stop
#  start argument is optional and default value is 0
#  step argument is optional and default value is 1
# randrange(10)-->generates a number from 0 to 9
# randrange(1,11)-->generates a number from 1 to 10
# randrange(1,11,2)-->generates a number from 1,3,5,7,9
# Eg 1:
from random import *
for i in range(10):
    print(randrange(10))

# Eg 2:    
from random import *
for i in range(10):
    print(randrange(1,11)) 



# Eg 3:
from random import *
for i in range(10):
    print(randrange(1,11,2))


# 5. choice() function:
# It wont return random number.
# It will return a random object from the given list or tuple.
# Eg:

from random import *
list=["Sunny","Bunny","Chinny","Vinny","pinny"]
for i in range(10):
    print(choice(list)) 


# =============================================================================
# 
# Packages
# It is an encapsulation mechanism to group related modules into a single unit.
# package is nothing but folder or directory which represents collection of Python modules.
# Any folder or directory contains __init__.py file,is considered as a Python package.This file
# can be empty.
# A package can contains sub packages also.
# =============================================================================
# The main advantages of package statement are
# 1. We can resolve naming conflicts
# 2. We can identify our components uniquely
# 3. It improves modularity of the application


# Eg 1:
# D:\Python_classes>
#  |-test.py
#  |-pack1
#      |-module1.py
#      |-__init__.py
     
# __init__.py:
# empty file

# module1.py:
def f1():
    print("Hello this is from module1 present in pack1")

#test.py (version-1):
import pack1.module1
pack1.module1.f1()
# test.py (version-2):
from pack1.module1 import f1
f1()



# Eg 2:
# D:\Python_classes>
#  |-test.py
#  |-com
#      |-module1.py
#      |-__init__.py
#          |-johndoe
#           |-module2.py
#           |-__init__.py

# __init__.py:
# empty file

# module1.py:
def f1():
    print("Hello this is from module1 present in com")
#module2.py:
def f2():
    print("Hello this is from module2 present in com.durgasoft")
#test.py:
from com.module1 import f1
from com.johndoe.module2 import f2
3. f1()
4. f2() 


# =============================================================================
# File Handling
# As the part of programming requirement, we have to store our data permanently for
# future purpose. For this requirement we should go for files.
# Files are very common permanent storage areas to store our data
# =============================================================================
# Types of Files:
# There are 2 types of files
# 1. Text Files:
# Usually we can use text files to store character data
# eg: abc.txt
# 2. Binary Files:
# Usually we can use binary files to store binary data like images,video files, audio files etc...

# Opening a File:
# Before performing any operation (like read or write) on the file,first we have to open that
# file.For this we should use Python's inbuilt function open()
# But at the time of open, we have to specify mode,which represents the purpose of
# opening file.
# f = open(filename, mode)
# The allowed modes in Python are

# 1. r > open an existing file for read operation. The file pointer is positioned at the
# beginning of the file.If the specified file does not exist then we will get
# FileNotFoundError.This is default mode.
# 2. w > open an existing file for write operation. If the file already contains some data
# then it will be overridden. If the specified file is not already avaialble then this mode will
# create that file.
# 3. a > open an existing file for append operation. It won't override existing data.If the
# specified file is not already avaialble then this mode will create a new file.
# 4. r+ > To read and write data into the file. The previous data in the file will not be
# deleted.The file pointer is placed at the beginning of the file.
# 5. w+ > To write and read data. It will override existing data.
# 6. a+ > To append and read data from the file.It wont override existing data.
# 7. x > To open a file in exclusive creation mode for write operation. If the file already
# exists then we will get FileExistsError.

# =============================================================================
# Note: All the above modes are applicable for text files. If the above modes suffixed with
# 'b' then these represents for binary files.
# Eg: rb,wb,ab,r+b,w+b,a+b,xb
# =============================================================================
f = open("abc.txt","w")
# We are opening abc.txt file for writing data

# Closing a File:
# After completing our operations on the file,it is highly recommended to close the file.
# For this we have to use close() function.
f.close()

# Various properties of File Object:
# Once we opend a file and we got file object,we can get various details related to that file
# by using its properties.
# name > Name of opened file
# mode > Mode in which the file is opened
# closed > Returns boolean value indicates that file is closed or not
# readable()> Retruns boolean value indicates that whether file is readable or not
# writable()>Returns boolean value indicates that whether file is writable or not.

f=open("abc.txt",'w')
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Is File Readable: ",f.readable())
print("Is File Writable: ",f.writable())
print("Is File Closed : ",f.closed)
f.close()
print("Is File Closed : ",f.closed) 



# =============================================================================
# Writing data to text files:
# We can write character data to the text files by using the following 2 methods.
# write(str)
# writelines(list of lines)
# =============================================================================

f=open("abcd.txt",'w')
f.write("John\n")
f.write("Doe\n")
f.write("Techniques\n")
print("Data written to the file successfully")
f.close()


# Note: In the above program, data present in the file will be overridden everytime if we
# run the program. Instead of overriding if we want append operation then we should open
# the file as follows. 
f = open("abcd.txt","a")

f=open("abcd.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close() 

# Note: while writing data by using write() methods, compulsory we have to provide line
# seperator(\n),otherwise total data should be written to a single line


# Reading Character Data from text files:
# We can read character data from text file by using the following read methods.
# read()> To read total data from the file
# read(n) > To read 'n' characters from the file
# readline()> To read only one line
# readlines()> To read all lines into a list

# Eg 1: To read total data from the file
f=open("abc.txt",'r')
data=f.read()
print(data)
f.close() 

# Eg 2: To read only first 10 characters:
f=open("abc.txt",'r')
data=f.read(10)
print(data)
f.close()


# Eg 3: To read data line by line:
f=open("abc.txt",'r')
line1=f.readline()
print(line1,end='')
line2=f.readline()
print(line2,end='')
line3=f.readline()
print(line3,end='')
f.close() 


# Eg 4: To read all lines into list:
f=open("abc.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end='')
f.close()

# Eg 5:
f=open("abc.txt","r")
print(f.read(3))
print(f.readline())
print(f.read(4))
print("Remaining data")
print(f.read()) 


# =============================================================================
# The with statement:
# The with statement can be used while opening a file.We can use this to group file
# operation statements within a block.
# The advantage of with statement is it will take care closing of file,after completing all
# operations automatically even in the case of exceptions also, and we are not required to
# close explicitly.
# =============================================================================

with open("abc.txt","w") as f:
    f.write("Durga\n")
    f.write("Software\n")
    f.write("Solutions\n")
    print("Is File Closed: ",f.closed)
print("Is File Closed: ",f.closed) 



# =============================================================================
# # The seek() and tell() methods:
# # tell():
# # ==>We can use tell() method to return current position of the cursor(file pointer) from
# # beginning of the file. [ can you plese telll current cursor position]
# # The position(index) of first character in files is zero just like string index.
# 
# =============================================================================
f=open("abc.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())


# =============================================================================
# seek():
# We can use seek() method to move cursor(file pointer) to specified location.
# [Can you please seek the cursor to a particular location]
# f.seek(offset, fromwhere)
# offset represents the number of positions
# The allowed values for second attribute(from where) are
# 0---->From beginning of file(default value)
# 1---->From current position
# 2--->From end of the file
# Note: Python 2 supports all 3 values but Python 3 supports only zero.
# Eg:
# =============================================================================
data="All Students are STUPIDS"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+") as f:
    text=f.read()
    print(text)
    print("The Current Cursor Position: ",f.tell())
    f.seek(17)
    print("The Current Cursor Position: ",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("Data After Modification:")
    print(text) 


# =============================================================================
# os module
# How to check a particular file exists or not?
# We can use os library to get information about files in our computer.
# os module has path sub module,which contains isFile() function to check whether a
# particular file exists or not?
# os.path.isfile(fname)
# =============================================================================

# Q. Write a program to check whether the given file exists or not. If it is
# available then print its content?

import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)

print("The content of file is:")
data=f.read()
print(data) 

# Note:
# sys.exit(0) ===>To exit system without executing rest of the program.
# argument represents status code . 0 means normal termination and it is the default value.


# Q. Program to print the number of lines,words and characters present in the
# given file?
import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)

lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    count=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
    
print("The number of Lines:",lcount)
print("The number of Words:",wcount)
print("The number of Characters:",ccount)


# Handling Binary Data:
# It is very common requirement to read or write binary data like images,video files,audio
# files etc.

# Q. Program to read image file and write to a new image file?
f1=open("rossum.jpg","rb")
f2=open("newpic.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print("New Image is available with the name: newpic.jpg") 


# Handling csv files:
# CSV==>Comma seperated values
# As the part of programming,it is very common requirement to write and read data wrt csv
# files. Python provides csv module to handle csv files.


# Writing data to csv file:
import csv
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f) # returns csv writer object
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
print("Total Employees data written to csv file successfully") 


# Note: Observe the difference with newline attribute and without
with open("emp.csv","w",newline='') as f:
with open("emp.csv","w") as f:
# Note: If we are not using newline attribute then in the csv file blank lines will be included
# between data. To prevent these blank lines, newline attribute is required in Python-3,but
# in Python-2 just we can specify mode as 'wb' and we are not required to use newline
# attribute.

# Reading Data from csv file:
import csv
f=open("emp.csv",'r')
r=csv.reader(f) #returns csv reader object
data=list(r)
#print(data)
for line in data:
    for word in line:
        print(word,"\t",end='')
    print() 


# =============================================================================
# Zipping and Unzipping Files:
# It is very common requirement to zip and unzip files.
# The main advantages are:
# 1. To improve memory utilization
# 2. We can reduce transport time
# 3. We can improve performance.
# To perform zip and unzip operations, Python contains one in-bulit module zip file.
# This module contains a class : ZipFile# 
# =============================================================================
# To create Zip file:
# We have to create ZipFile class object with name of the zip file,mode and constant
# ZIP_DEFLATED. This constant represents we are creating zip file.
f = ZipFile("files.zip","w","ZIP_DEFLATED")
# Once we create ZipFile object,we can add files by using write() method.
f.write(filename)


# Eg:
from zipfile import *
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")
f.close()
print("files.zip file created successfully") 


# To perform unzip operation:
# We have to create ZipFile object as follows

f = ZipFile("files.zip","r",ZIP_STORED)

# ZIP_STORED represents unzip operation. This is default value and hence we are not
# required to specify.
# Once we created ZipFile object for unzip operation,we can get all file names present in
# that zip file by using namelist() method.
names = f.namelist()
# Eg:
from zipfile import *
f=ZipFile("archive.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print( "File Name: ",name)
    print("The Content of this file is:")
    f1=open(name,'r')
    print(f1.read())
    print()



# =============================================================================
# _______OS MODULE------------------------- 
# # Working with Directories:
# # It is very common requirement to perform operations for directories like
# # 1. To know current working directory
# # 2. To create a new directory
# # 3. To remove an existing directory
# # 4. To rename a directory
# # 5. To list contents of the directory# 
# 
# To perform these operations,Python provides inbuilt module os,which contains several
# functions to perform directory related operations.
# =============================================================================

# Q1. To Know Current Working Directory:  
import os
cwd=os.getcwd()
print("Current Working Directory:",cwd)



# Q2. To create a sub directory in the current working directory:  
import os
os.mkdir("mysub")
print("mysub directory created in cwd")

# Q3. To create a sub directory in mysub directory:
#  cwd
#  |-mysub
#  |-mysub2 
import os
os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")

# Note: Assume mysub already present in cwd.

# Q4. To create multiple directories like sub1 in that sub2 in that sub3:
import os
os.makedirs("sub1/sub2/sub3")
print("sub1 and in that sub2 and in that sub3 directories created")

# Q5. To remove a directory:
import os
os.rmdir("mysub/mysub2")
print("mysub2 directory deleted")

# Q6. To remove multiple directories in the path:
import os
os.removedirs("sub1/sub2/sub3")
print("All 3 directories sub1,sub2 and sub3 removed")


# Q7. To rename a directory:
import os
os.rename("mysub","newdir")
print("mysub directory renamed to newdir")

# Q8. To know contents of directory:
# os module provides listdir() to list out the contents of the specified directory. It won't
# display the contents of sub directory.
# Eg:
    
import os
print(os.listdir("."))

# The above program display contents of current working directory but not contents of sub
# directories.
# If we want the contents of a directory including sub directories then we should go for
# walk() function.

# Q9. To know contents of directory including sub directories:
# We have to use walk() function
# [Can you please walk in the directory so that we can aware all contents of that directory]
# os.walk(path,topdown=True,onerror=None,followlinks=False)

# It returns an Iterator object whose contents can be displayed by using for loop
# path-->Directory path. cwd means .
# topdown=True --->Travel from top to bottom
# onerror=None --->on error detected which function has to execute.
# followlinks=True -->To visit directories pointed by symbolic links

# Eg: To display all contents of Current working directory including sub directories:
import os
for dirpath,dirnames,filenames in os.walk('.'):
    print("Current Directory Path:",dirpath)
    print("Directories:",dirnames)
    print("Files:",filenames)
    print()

# Note: To display contents of particular directory,we have to provide that directory name
# as argument to walk() function.
os.walk("directoryname")

# Q. What is the difference between listdir() and walk() functions?
# In the case of listdir(), we will get contents of specified directory but not sub directory
# contents. But in the case of walk() function we will get contents of specified directory and
# its sub directories also.



# Running Other programs from Python program:
# os module contains system() function to run programs and commands.
# It is exactly same as system() function in C language.


os.system("commad string")
# The argument is any command which is executing from DOS.

# Eg:
import os
os.system("dir *.py")
os.system("py abc.py")


# How to get information about a File:
# We can get statistics of a file like size, last accessed time,last modified time etc by using
# stat() function of os module.

stats = os.stat("abc.txt")


# The statistics of a file includes the following parameters:
# st_mode==>Protection Bits
# st_ino==>Inode number
# st_dev===>device
# st_nlink===>no of hard links
# st_uid===>userid of owner
# st_gid==>group id of owner
# st_size===>size of file in bytes
# st_atime==>Time of most recent access
# st_mtime==>Time of Most recent modification
# st_ctime==> Time of Most recent meta data change


# Note:
# st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st
# 1970 ,12:00AM. By using datetime module fromtimestamp() function,we can get exact
# date and time.

# Q. To print all statistics of file abc.txt:
import os
stats=os.stat("abc.txt")
print(stats)

# Q. To print specified properties:
import os
from datetime import *
stats=os.stat("abc.txt")
print("File Size in Bytes:",stats.st_size)
print("File Last Accessed Time:",datetime.fromtimestamp(stats.st_atime))
print("File Last Modified Time:",datetime.fromtimestamp(stats.st_mtime)) 


# =============================================================================
# Pickling and Unpickling of Objects:
#     
# Sometimes we have to write total state of object to the file and we have to read total
# object from the file.
# 
# The process of writing state of object to the file is called pickling and the process of
# reading state of an object from the file is called unpickling.
# 
# We can implement pickling and unpickling by using pickle module of Python.
# pickle module contains dump() function to perform pickling.
# 
# pickle.dump(object,file)
# 
# pickle module contains load() function to perform unpickling
# 
# obj=pickle.load(file)
# =============================================================================

# Writing and Reading State of object by using pickle Module:
import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno;
        self.ename=ename;
        self.esal=esal;
        self.eaddr=eaddr;
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
    
with open("emp.dat","wb") as f:
    e=Employee(100,"John",1000,"Delhi")
    pickle.dump(e,f)
    print("Pickling of Employee Object completed...")

with open("emp.dat","rb") as f:
    obj=pickle.load(f)
    print("Printing Employee Information after unpickling")
    obj.display()




# Writing Multiple Employee Objects to the file:
# emp.py:
import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno;
        self.ename=ename;
        self.esal=esal;
        self.eaddr=eaddr;
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
# pick.py:
import emp,pickle
f=open("emp.dat","wb")
n=int(input("Enter The number of Employees:"))
for i in range(n):
    eno=int(input("Enter Employee Number:"))
    ename=input("Enter Employee Name:")
    esal=float(input("Enter Employee Salary:"))
    eaddr=input("Enter Employee Address:")
    e=emp.Employee(eno,ename,esal,eaddr)
    pickle.dump(e,f)
print("Employee Objects pickled successfully")

# unpick.py:
import emp,pickle
f=open("emp.dat","rb")
print("Employee Details:")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("All employees Completed")
        break
f.close()


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

