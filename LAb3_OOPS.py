# -*- coding: utf-8 -*-
"""
Excersise 3_1
"""

class Movie:
    
    def __init__(self,title,actor,actress):
        self.title =title
        self.actor = actor
        self.actress = actress
        
        
    def info(self):
        print("Movie name:",self.title)
        print("Actor name:",self.actor)
        print("Actress name:",self.actress)
        
        
list_of_movies = []

while True:
      title=input('Enter Movie Name:')
      actor=input('Enter actor Name:')
      actress=input('Enter actress Name:')
     
      m = Movie(title,actor,actress)
      list_of_movies.append(m)
      print("Movie added Successfully")
      
      option= input(" Do you want to add more movies: [Y|N]") 
      
      if option.lower()=='n':
           break
      

print('All Movies information')
print('#'*40)


for movie in list_of_movies:
    movie.info()
    
    
"""Exercise 3.2:
    
Bank Application
Multiple customers

customer name
balance
deposit
withdraw

"""
import sys

class Customer:
    """Customer class to describe bank operations"""
    
    bankname="SBI"
    
    def __init__(self,name,balance=0.0):
        
        self.name=name
        self.balance=balance
        
        
    def deposit(self,amt):
        self.balance+=amt        
        print("Balance after deposit:",self.balance) 
        
        
    def withdraw(self,amt):        
        if amt>self.balance:            
            print("Insufficient Funds.........")            
            sys.exit()
        else:
            self.balance-=amt            
            print("Balance after withdraw.",self.balance)
    

print(f'Welcome to {Customer.bankname} Bank')

name =input('Enter your name: ')
c = Customer(name)

while True:
    
    print('d-Deposit\nw -Withdraw \ne - Exit')
    
    option=input("Choose your option:")
    
    #if option=='d' or option=='D':
    if option.lower()=='d':
        
        amount =float(input("Enter Amount to deposit:"))
                  
        c.deposit(amount)

    elif option=='w' or option=='W':        
        amount=float(input("Enter amount to withdraw:"))        
        c.withdraw(amount)

    elif option.lower()=='e':
        print(f"Thanks for visiting {Customer.bankname} Bank")        
        sys.exit()
    else:        
        print("Invalid Option")



# ATM has only 500 rs notes, modify the code

import sys

class Customer:
    """Customer class to describe bank operations"""
    
    bankname="SBI"
    
    def __init__(self,name,balance=0.0):
        
        self.name=name
        self.balance=balance
        
        
    def deposit(self,amt):
        self.balance+=amt        
        print("Balance after deposit:",self.balance) 
        
        
    def withdraw(self,amt): 

        
        if amt>self.balance:            
            print("Insufficient Funds.........")            
            sys.exit()
        else:
            self.balance-=amt            
            print("Balance after withdraw.",self.balance)
    

print(f'Welcome to {Customer.bankname} Bank')

name =input('Enter your name: ')
c = Customer(name)

while True:
    
    print('d-Deposit\nw -Withdraw \ne - Exit')    
    option=input("Choose your option:")    
    #if option=='d' or option=='D':
    if option.lower()=='d':        
        amount =float(input("Enter Amount to deposit:"))                  
        c.deposit(amount)

    elif option=='w' or option=='W':
        while amount%500!=0:
            print('Amount should be multiple of 500')
            amount=float(input("Enter amount to withdraw:"))
        c.withdraw(amount)

    elif option.lower()=='e':
        print(f"Thanks for visiting {Customer.bankname} Bank")        
        sys.exit()
    else:        
        print("Invalid Option")


# Q 3_3

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
count =0
while(count<n):
    name=input("Enter student name")
    marks=int(input("Enter student marks"))
    s.display()
    s.grade()
    print("*"*20)
    count+=1




