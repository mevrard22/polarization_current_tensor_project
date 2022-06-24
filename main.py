import pyperclip as pc  # To copy and paste the final matrix when it has been processed
import functions as fns  # Functions file to keep it more organised
import sympy as sp

"""
* Check if the function made yesterday actually works by doing algebra to 
compare values to dan's mathematica file (try to do this by doing the math to 
untransformed tensor to see if it is the same)
"""

# Change values and of the 3x6 here
a = sp.exp('a'); b = sp.exp('b'); c = sp.exp('c')
threeBySix = [[1, 1, 1, 1, a, 1], [1, 1, 1, b, 1, 1], [b, b, c, 1, 1, 1]]

# Placeholder values before changing them
threeByThree = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0],
                                                    [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

# Loop through each row of the 3x6 matrix
for i in range(0, 3):
    # Loop through each column of the 3x6 matrix
    for j in range(0, 6):
        # Function to change the values accordingly
        fns.adjust_value(i, j, threeByThree, threeBySix)

fns.calculate_dc_current_vector(threeByThree)
print(".")

# Printing the original and final matrix
print('Original Matrix: ' + threeBySix.__str__())
print('Matrix as 3x3x3: ' + threeByThree.__str__())

# Copy the new matrix to clipboard using pyperclip package
# pc.copy(threeByThree.__str__())
# print('3x3 Matrix Copied to Clipboard')
