#Analytical Mechanics 0070 Lab 2 Code
#@author: NicoDiLullo
import numpy as np
import matplotlib.pyplot as plt
#Data and errors
#acceleration
x = np.array([0.738, 0.790, 0.901, 1.064])
#f=msubhg
y = np.array([0.137, 0.147, 0.167, 0.196])
x_errors = np.array([0.003, 0.003, 0.003, 0.004])
# Line of best fit
coefficients = np.polyfit(x, y, 1)
line_of_best_fit = np.poly1d(coefficients)
# Create a scatter plot with y-errors
plt.errorbar(x, y, xerr=x_errors, fmt='o', label='Data with Errors')
# Plot it
x_range = np.linspace(min(x), max(x), 100)
plt.plot(x_range, line_of_best_fit(x_range), label='Line of Best Fit', color='red')
# L & L, show
plt.xlabel('F=mg')
plt.ylabel('Acceleration')
plt.legend()
plt.grid(True) 
plt.show()
