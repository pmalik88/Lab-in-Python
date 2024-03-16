# -*- coding: utf-8 -*-
"""
Python Logging
"""

# =============================================================================
# Logging the Exceptions:
# It is highly recommended to store complete application flow and exceptions information
# to a file. This process is called logging.
# =============================================================================

# The main advantages of logging are:
# 1. We can use log files while performing debugging
# 2. We can provide statistics like number of requests per day etc

# To implement logging, Python provides one inbuilt module logging.
# =============================================================================
# # logging levels:
# # Depending on type of information, logging data is divided according to the following 6
# # levels in Python.
# #  table
# # 1. CRITICAL==>50==>Represents a very serious problem that needs high attention
# # 2. ERROR===>40===>Represents a serious error
# # 3. WARNING==>30==>Represents a warning message, some caution needed. It is alert to
# # the programmer
# # 4. INFO===>20===>Represents a message with some important information
# # 5. DEBUG===>10==>Represents a message with debugging information
# # 6. NOTSET==>0==>Rrepresents that the level is not set.
# # By default while executing Python program only WARNING and higher level messages will
# # be displayed.
# =============================================================================


# =============================================================================
# # How to implement logging:
# # To perform logging, first we required to create a file to store messages and we have to
# # specify which level messages we have to store.
# # We can do this by using basicConfig() function of logging module.
import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
# =============================================================================
# The above line will create a file log.txt and we can store either WARNING level or higher
# level messages to that file.
# After creating log file, we can write messages to that file by using the following methods.
# import logging
# logging.debug(message)
# logging.info(message)
# logging.warning(message)
# logging.error(message)
# logging.critical(message)


# =============================================================================
# Q.Write a Python program to create a log file and write WARNING and higher
# level messages?
# =============================================================================
import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print("Logging Module Demo")
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message") 


# Note:
# In the above program only WARNING and higher level messages will be written to log file.
# If we set level as DEBUG then all messages will be written to log file.

import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print("Logging Module Demo")
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message") 


# Note: We can format log messages to include date and time, ip address of the client etc
# at advanced level.


# How to write Python program exceptions to the log file:
# By using the following function we can write exceptions information to the log file.
# logging.exception(msg)


# Q. Python Program to write exception information to the log file
import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A New request Came:")
try:
    x=int(input("Enter First Number: "))
    y=int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError as msg:
    print("cannot divide with zero")
    logging.exception(msg)
except ValueError as msg:
    print("Enter only int values")
    logging.exception(msg)
logging.info("Request Processing Completed") 














