# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:19:46 2024

@author: SOEE
"""

import random
import string

# Function to generate a random name
def generate_name():
    names = ["John", "Alice", "Michael", "Emily", "Daniel", "Sophia", "William", "Olivia", "James", "Emma"]
    return random.choice(names)

# Function to generate a random age between 18 and 70
def generate_age():
    return random.randint(18, 70)

# Function to generate a random weight between 40 and 120
def generate_weight():
    return random.randint(40, 120)

# Function to generate a random height between 120 and 200
def generate_height():
    return random.randint(120, 200)

# Function to generate a random email
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"])
    return f"{username}@{domain}"

# Generate 100 lines and write to the file
with open("random_people.txt", "w") as file:
    for _ in range(100):
        name = generate_name()
        age = generate_age()
        weight = generate_weight()
        height = generate_height()
        email = generate_email()
        line = f"Name: {name} Age: {age} Weight: {weight} Height: {height} Email: {email}\n"
        file.write(line)
