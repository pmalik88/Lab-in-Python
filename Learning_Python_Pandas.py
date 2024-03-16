# -*- coding: utf-8 -*-
"""
Pandas
"""

# Creation of Pandas
import pandas as pd

# Series
# From List
s=pd.Series([1,2,3,4])
print(s)
type(S)
dir(S)
# Back to list
s.to_list()



# from Tuple
s=pd.Series((1,2,3,4))
print(s)




# From Dictionary
s=pd.Series({0:1,1:2,2:3,3:4})
print(s)
# Back to dictionary
s.to_dict()



# from set
s=pd.Series({1,2,3,4}) #TypeError: 'set' type is unordered

# by functions
s=pd.Series(range(10))
print(s)

# From Numpy array
s=pd.Series(np.array(range(10)))
s=pd.Series(np.arange(10))
s=pd.Series(np.random.randint(1,10))
#back to numpy array
s.values
s.to_numpy()



# Operations on a Series 
# checking size,shape,datatype,element and length of series
s.shape
s.size
len(s)
s.ndim
s.dtype

# change data type
s=pd.Series([1,2,3,4])
s.dtype

s1=pd.Series([1.,2.,3.,4.])
s1.dtype


s=pd.Series([1,2,3,4])
print(s.dtype)

s=pd.Series([1,2,3,4],dtype=float)
print(s.dtype)


p=s.astype('float')
print(p.dtype)


# checking whether element is in series or not
1 in s
# iterate over series
for i in s:
    print(i)

for i,j in enumerate(s):
    print(f"{i} - {j}")
    
    
# Mutability
s=pd.Series([1,2,3,4])    
s[0]=4  
print(s)    
    
# Operation association
s*2
s**2
s+2
s-2
s.sum()
s.mean()
s.var()
s.std()
s.describe()
s.head()
s.tail()

# Plotting
s.hist()
s.plot()
# Changing Index
S=pd.Series([1.,2.,3.,5.],index=['a','b','c','d'])
S.index
# Index(['a', 'b', 'c', 'd'], dtype='object')


# Accessing the series
S[0]
S['a']
S.iloc[0]
# or
S[1]
S.iloc[1]
S['b']
S.loc['b']

# Manipulation over two series
S1=pd.Series([1,2,3,4])
S2=pd.Series([1,2,3,4])

S1*S2
S1>5
S1[S1<3]


# Finding elements
S1>5


# Finding NA elements
S1=pd.Series([1,None,3,4])
S1.isna()
pd.isna(S1)


#
S1=pd.Series([1,None,3,4])
P=S1.dropna()
print(p)
# or 
s=pd.Series([1,None,3,4])
s.drop(s[s == None].index)
s


s.drop(2)


print(s)
s.drop([2,3])

s = pd.Series([1, 2, 3, 4, 5])
# Drop the element at index 2 from the Series
s_dropped = s.drop(index=2)

# Checking for missing values
missing_values = df.isnull().sum()

# Dropping rows with missing values
df.dropna(inplace=True)

# Filling missing values with a specified value
df.fillna(0, inplace=True)


s=pd.Series(range(2,23))
s = s.drop(s[s == 5].index)


S=pd.Series([1,2,3,5],dtype='float64')

S.dtype
S.index
S=pd.Series([1,2,3,5],dtype='float64')
S.index
S.values
S[3]
S[1:3].values




S=pd.Series(range(10))

A={'p':1,'t':2,'c':3}
S=pd.Series(A)
S.index

import numpy as np
S=pd.Series(np.array([1,2,3,4]))
print(S)








# Manipulation over Panda Series

S1=pd.Series([1,2,3,4,5])
S2=pd.Series([5,6,7,8,5])

S1*S2

S1.multiply(S2)

S1.sum()
S1.std()
S1.to_numpy()
type(S1.values)


S1.describe()
S1.unique

S1.plot()
S1.quantile()
S1.cumsum()
S1.argmin()
S1.hist()

S1.to_timestamp()
S1.equals(S2)
S1.cov(S2)
S1.add(S2)
df = pd.read_csv("nba.csv") 




# Module 1: Introduction to Pandas
# Creating DataFrames

import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Creating a DataFrame from a list of lists
data = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
df = pd.DataFrame(data, columns=['Name', 'Age'])


# Reading and Writing into Semi-Structured Data
# Reading CSV file
df = pd.read_csv('data.csv')

# Writing DataFrame to CSV file
df.to_csv('data.csv', index=False)

# Reading Excel file
df = pd.read_excel('data.xlsx')

# Writing DataFrame to Excel file
df.to_excel('data.xlsx', index=False)

# Reading JSON file
df = pd.read_json('data.json')

# Writing DataFrame to JSON file
df.to_json('data.json', orient='records')

# Reading and Writing into Semi-Structured Data
# Reading XML file
import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()
data = []
for child in root:
    data.append({elem.tag: elem.text for elem in child})
df = pd.DataFrame(data)

# Writing DataFrame to XML file
with open('data.xml', 'w') as f:
    f.write(df.to_xml())
    
    
    
# Module 2: Data Manipulation with Pandas
# Selection in DataFrames

# Selecting a column
column = df['Name']
column 
# Selecting multiple columns
columns = df[['Name', 'Age']]
columns
# Selecting rows using boolean indexing
young_people = df[df['Age'] < 30]
young_people



# Conditional Selection
# Using boolean indexing with multiple conditions
young_and_charlie = df[(df['Age'] < 30) & (df['Name'] == 'Charlie')]
young_and_charlie


# Groupby Operations
# Grouping data by a column and calculating mean
average_age = df.groupby('Name')['Age'].mean()
average_age


# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'],
        'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)

# Group by 'Name'
grouped = df.groupby('Name')

# Apply aggregate functions (e.g., mean, sum) on the groups
print(grouped.mean())  # Calculate mean salary for each group
print(grouped.sum())   # Calculate total salary for each group


# Applying Aggregate Functions:
# You can apply various aggregate functions like mean, sum, count, max, min, etc., on the grouped data.
# Calculate mean age for each group
print(grouped['Age'].mean())

# Calculate total salary for each group
print(grouped['Salary'].sum())

# Get the count of records for each group
print(grouped.size())

# Get the maximum age for each group
print(grouped['Age'].max())

# Grouping by Multiple Columns:
# You can group by multiple columns by passing a list of column names to the groupby() function.
# Group by 'Name' and 'Age'
grouped = df.groupby(['Name', 'Age'])
# Apply aggregate functions on the groups
print(grouped.mean())  # Calculate mean salary for each (Name, Age) combination



# Iterating over Groups:
# You can iterate over the groups and perform custom operations on each group.
# Iterate over groups
for name, group in grouped:
    print("Group:", name)
    print(group)

# Sorting values in DataFrames
# Sorting DataFrame by a column
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# Pivot Tables for data summarization
# Creating a pivot table
pivot_table = df.pivot_table(index='Name', values='Age', aggfunc='mean')
pivot_table

# =============================================================================
# # USe of inplace
# =============================================================================
# Without inplace=True:
import pandas as pd
# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Applying an operation without inplace=True
A=df.drop(columns='B')  # Drop column 'B', but the original DataFrame 'df' remains unchanged
print(df)
print(A)


# With inplace=True:
import pandas as pd
# Creating a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Applying an operation with inplace=True
A=df.drop(columns='B', inplace=True)  # Drop column 'B', and modify the original DataFrame 'df' in place
print(df)
print(A)




# =============================================================================
# Data Integration:
#     
# Data integration involves combining data from different sources or datasets into 
# a unified format. This process may include merging, joining, concatenating, or 
# appending datasets. In Pandas, you can perform data integration using the following functions: 
# 1. Merging (pd.merge()): 
 # Merging combines datasets based on one or more common columns, 
# similar to SQL joins. You can specify the type of join (inner, outer, left, right) 
# and the columns to join on.
# 
# 2.Joining (DataFrame.join()): 
#Joining is a convenient method for combining datasets 
# horizontally based on the DataFrame index or column values.
# 
# 3.Concatenating (pd.concat()): 
    #Concatenating combines datasets along a particular 
# axis (row or column). It is useful for vertically stacking or horizontally 
# concatenating multiple DataFrames.
# =============================================================================

import pandas as pd

# Data Integration
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 35]})

merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Merge based on 'ID'
merged_df
# Data Transformation
cleaned_df = merged_df.dropna()  # Drop rows with missing values
cleaned_df['Age'] = cleaned_df['Age'].astype(int)  # Convert 'Age' column to integer

# Feature Engineering
cleaned_df['Age_Group'] = pd.cut(cleaned_df['Age'], bins=[0, 30, 40, float('inf')], labels=['<30', '30-40', '>=40'])
print(cleaned_df)


 # =============================================================================
# Data Transformation:
# Data transformation involves modifying the structure or content of datasets to 
# make them suitable for analysis. This may include tasks such as filtering rows, 
# transforming columns, handling missing values, and creating new features. 
# In Pandas, you can perform various data transformation tasks using the following 
# methods and functions:
# =============================================================================

# Data Cleaning:

# 1. Removing Duplicate Rows (DataFrame.drop_duplicates()): Removes duplicate rows 
# based on specified columns.

# 2. Handling Missing Values (DataFrame.dropna(), DataFrame.fillna()): Drops rows or 
# fills missing values with specified values or methods.

# 3. Replacing Values (Series.replace()): Replaces specified values with other values.

# Data Manipulation:

# 1. Selecting Rows and Columns (DataFrame.loc[], DataFrame.iloc[]): Selects specific
#  rows and columns based on labels or integer indices.
# 2. Applying Functions (Series.apply(), DataFrame.applymap()): Applies custom functions
#  element-wise or column-wise.
# 3. Grouping and Aggregation (DataFrame.groupby(), GroupBy.agg()): Groups data based
#  on specified criteria and applies aggregate functions.


# Feature Engineering:
# 1. Creating New Columns: Generates new columns based on existing columns or custom
#  functions. 
# 2.  Extracting Information (Series.str.extract(), Series.dt): Extracts information 
# from text or datetime columns.

# Data Conversion:

# 1. Changing Data Types (DataFrame.astype()): Converts the data type of columns to 
# a specified type.
# 3. Reshaping Data (DataFrame.pivot(), DataFrame.melt()): Transforms data between 
# wide and long formats.



# Module 3: Data Integration and Transformation
# Merging DataFrames
# Merging two DataFrames on a common column


# Renaming and dropping values in DataFrames
# Renaming columns
df.rename(columns={'Name': 'Full Name', 'Age': 'Years'}, inplace=True)

# Dropping columns
df.drop(columns=['Name'], inplace=True)






# Working with datetime data

# Converting a string column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Extracting month and year from datetime column
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year


# Advanced data manipulation techniques
# Applying a custom function to a DataFrame
df['Name_Length'] = df['Name'].apply(lambda x: len(x))
# Replacing values in a column
df['Gender'].replace({'M': 'Male', 'F': 'Female'}, inplace=True)
# Creating dummy variables for categorical data
dummy_df = pd.get_dummies(df['Gender'])


import numpy as np
# Sample data
data = np.array([[4, 11], [8, 4], [13,5],[7,14]])
# Compute covariance matrix
cov_matrix = np.cov(data, rowvar=False)
print("Covariance Matrix:")
print(cov_matrix)

import numpy as np
# Sample data
data = np.array([[4, 11], [8, 4], [13,5],[7,14]])
# Compute covariance matrix
cov_matrix = np.cov(data, rowvar=False)
# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)









