# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:28:47 2024

@author: SOEE
"""

import numpy as np
import matplotlib.pyplot as plt

# Create a normalized random variable of size 20
np.random.seed(42)  # for reproducibility
data = np.random.randn(20)

# Calculate quartiles
quartiles = np.percentile(data, [25, 50, 75])

# Find counts for each quartile
count_quartile_1 = np.sum(data <= quartiles[0])
count_quartile_2 = np.sum((data > quartiles[0]) & (data <= quartiles[1]))
count_quartile_3 = np.sum((data > quartiles[1]) & (data <= quartiles[2]))
count_quartile_4 = np.sum(data > quartiles[2])

# Display quartiles and their counts
print("Quartiles:")
print("Q1:", quartiles[0])
print("Q2 (Median):", quartiles[1])
print("Q3:", quartiles[2])
print()
print("Counts in each quartile:")
print("Q1 count:", count_quartile_1)
print("Q2 count:", count_quartile_2)
print("Q3 count:", count_quartile_3)
print("Q4 count:", count_quartile_4)

# Draw box plot
plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=False)
plt.title('Box Plot of Normalized Random Variable')
plt.xlabel('Values')
plt.show()
