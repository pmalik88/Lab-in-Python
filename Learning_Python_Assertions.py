# -*- coding: utf-8 -*-
"""
PYTHON DEBUGGING BY USING ASSERTIONS
"""
# =============================================================================
# # Debugging Python Program by using assert keyword:
# # The process of identifying and fixing the bug is called debugging.
# =============================================================================
# Very common way of debugging is to use print() statement. But the problem with the
# print() statement is after fixing the bug,compulsory we have to delete the extra added
# print() statments,otherwise these will be executed at runtime which creates performance
# problems and disturbs console output.

# To overcome this problem we should go for assert statement. The main advantage of
# assert statement over print() statement is after fixing bug we are not required to delete
# assert statements. Based on our requirement we can enable or disable assert statements.
# Hence the main purpose of assertions is to perform debugging. Usully we can perform
# debugging either in development or in test environments but not in production
# environment. Hence assertions concept is applicable only for dev and test environments
# but not for production environment.

# Types of assert statements:
# =============================================================================
# # There are 2 types of assert statements
# # 1. Simple Version
# # 2. Augmented Version
# =============================================================================
# 1. Simple Version:
assert conditional_expression
# 2. Augmented Version:
assert conditional_expression,message
# conditional_expression will be evaluated and if it is true then the program will be
# continued.
# If it is false then the program will be terminated by raising AssertionError.
# By seeing AssertionError, programmer can analyze the code and can fix the problem.
# Eg:
def squareIt(x):
    return x**x

assert squareIt(2)==4,"The square of 2 should be 4"
assert squareIt(3)==9,"The square of 3 should be 9"
assert squareIt(4)==16,"The square of 4 should be 16"
print(squareIt(2))
print(squareIt(3))
print(squareIt(4)) 
    
    
def squareIt(x):
    return x*x

assert squareIt(2)==4,"The square of 2 should be 4"
assert squareIt(3)==9,"The square of 3 should be 9"
assert squareIt(4)==16,"The square of 4 should be 16"
print(squareIt(2))
print(squareIt(3))
print(squareIt(4)) 

# Exception Handling vs Assertions:
# Assertions concept can be used to alert programmer to resolve development time errors.
# # Exception Handling can be used to handle runtime errors.





























