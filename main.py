import pyperclip as pc  # To copy and paste the final matrix when it has been processed

import functions
import sympy as sp

# Define a list to put each tensor into
l = []

# Find the number of tensors the user would like to enter
number = int(input("How many tensors would you like to enter?"))

# Loop through whatever that number so user can enter all tensors they need calculations for
for number in range(0, number):
    l += [functions.enter_matrix()]
