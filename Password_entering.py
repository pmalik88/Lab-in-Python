# -*- coding: utf-8 -*-
"""Enter the password three times
"""

n=0
while n<3:
    n=n+1
    password = input('Enter the password')
    
    if password=='secret':
        print("Welcome...........")
        n=4
    else:
        if n==3:
            print('You have exhausted all attempts')
        else:
            print(f'You have left {3-n} attempts')        
       
        