import numpy as np
import sympy as sp  # Symbolic mathematics package

# Adjust value will take in two indices (for the column and row of the 3x6 matrix)
# , as well as a placeholder 3x3x3 matrix the 3x6 matrix which is to be converted
# NOTE: these calculations currently only works for point groups where
# jk → j if j=k, jk → 9-(j+k) if j≠k in the 3x6 matrix


def adjust_value(i_index, j_index, three_by_three, three_by_six):
    # Handle cases where looking at first, second or third index of 3x6 matrix
    if j_index <= 2:
        three_by_three[i_index][j_index][j_index] = three_by_six[i_index][j_index]
    # Individually handle cases for when index (j) is 4, 5 or 6
    # Change rules as necessary
    elif j_index == 3:
        three_by_three[i_index][1][2] = three_by_six[i_index][j_index]
        three_by_three[i_index][2][1] = three_by_six[i_index][j_index]
    elif j_index == 4:
        three_by_three[i_index][0][2] = three_by_six[i_index][j_index]
        three_by_three[i_index][2][0] = three_by_six[i_index][j_index]
    elif j_index == 5:
        three_by_three[i_index][1][0] = three_by_six[i_index][j_index]
        three_by_three[i_index][0][1] = three_by_six[i_index][j_index]

# Get the matrix which has been converted
# Define the list En
# Perform double sum


def calculate_dccurrent_vector(matrix):
    # Defining expressions before I can use them
    x = sp.symbols('x'); cosine = sp.cos(x); sine = sp.sin(x)
    # Defining the components of the magnetic field and final vector, respectively
    en = [cosine, sine, 1]
    vector_component_list = [0, 0, 0]
    # Working out what the final expression for the DC current vector should be
    temp_i = 0
    for j in range(0, 3):
        for k in range(0, 3): #
            vector_component_list[j] += sp.simplify(en[j] * en[k] * matrix[temp_i][j][k])
            # Allows me to navigate
            if j == 2:
                temp_i += 1
    print(vector_component_list)