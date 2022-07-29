import sympy as sp  # Symbolic mathematics package
import numpy as np

'''
Allows the user to enter a matrix via the console, in a 3x6 format, then converts it to a 3x3x3 tensor using the 
adjust_value function, returns the final 3x3x3 matrix
'''


def enter_tensor():
    # Make a placeholder list with arbitrary elements so it's already formatted
    threeBySix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    threeByThree = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0],
                                                        [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    print("Enter each value of the 3x6 matrix representation of your tensor, from "
          "right to left, top to bottom")
    # Go through each element in the 3x6 matrix, as decribed above
    for i in range(0, 3):
        for j in range(0, 6):
            # Getting input from the user while telling them which row / column they should enter
            temp = input("Enter input for Column " + str(i + 1) + ", Row " + str(j + 1) + ":")
            # Adding the input to list
            if temp == "0":
                threeBySix[i][j] = 0
            else:
                threeBySix[i][j] = 1

    # Convert the 3x6 array to a 3x3 array
    # Loop through each row of the 3x6 matrix
    for i in range(0, 3):
        # Loop through each column of the 3x6 matrix
        for j in range(0, 6):
            # Function to change the values accordingly
            adjust_value(i, j, threeByThree, threeBySix)

    # Returning the properly formatted array
    return threeByThree


''' 
Adjust value will take in two indices (for the column and row of the 3x6 matrix)
, as well as a placeholder 3x3x3 matrix the 3x6 matrix which is to be converted
NOTE: these calculations currently only works for point groups where
jk → j if j=k, jk → 9-(j+k) if j≠k in the 3x6 matrix
'''


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

'''
Take in a rank 3 tensor, execute tensor contraction and return the 
vector that results from the contraction.
'''


def calculate_dc_current_vector(tensor):
    # Defining expressions before I can use them
    x = sp.symbols('x');
    cosine = sp.cos(x);
    sine = sp.sin(x)
    # Defining the components of the magnetic field and final vector, respectively
    en = [cosine, sine, 0]
    vector_component_list = [0, 0, 0]
    # Perform a triple sum with i, j and k of the tensor
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                vector_component_list[i] += sp.simplify(en[j] * en[k] * tensor[i][j][k])
    return vector_component_list

# TODO 3: Graph the DC current vectors using this function
def graph_dc_current_vector():
    # Make a function which can graph the dc current vector components
    return 0

# Change angles of the rotation of the x, y, and z matrices here.
'''
Take in a tensor, 
'''


def overall_rotation_matrix():
    xrot = float(input("Input the rotation angle about the x axis (in degrees):"))
    yrot = float(input("Input the rotation angle about the y axis (in degrees):"))
    zrot = float(input("Input the rotation angle about the z axis (in degrees):"))
    return np.matmul(mat("y", yrot), np.matmul(mat("x", xrot), mat("z", zrot)))


"""
Takes in a string which represents which rotation matrix (x, y or z) and a
float which represents the angle the user would like to input into that rotation matrix
"""


def mat(xyz, angle):
    angle = np.radians(angle)
    cosine = float(np.cos(angle))
    sine = float(np.sin(angle))
    if xyz == "x":
        return np.array([[1, 0, 0], [0, cosine, -sine], [0, sine, cosine]])
    elif xyz == "y":
        return np.array([[cosine, 0, sine], [0, 1., 0], [-sine, 0, cosine]])
    elif xyz == "z":
        return sp.Matrix([[cosine, -sine, 0], [sine, cosine, 0], [0, 0, 1]])
    else:
        return "You didn't input a valid xyz value!"


"""
Takes in a tensor which the user should have inputted through the enter_tensor method, 
rotates it and returns the rotated tensor
"""


def calculate_rotated_tensor(user_tensor, rm):
    temp = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0],
                                                [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                if abs(temp_tensor_contraction_fn(i, j, k, user_tensor, rm)) > 10 ** (-15):
                    temp[i][j][k] = temp_tensor_contraction_fn(i, j, k, user_tensor, rm)
                else:
                    temp[i][j][k] = 0
    return [mathematica_format(temp.__str__()), temp]


def temp_tensor_contraction_fn(i, j, k, tensor, rm):
    sum = 0.
    for l in range(0, 3):
        for m in range(0, 3):
            for n in range(0, 3):
                sum += rm[l][i] * rm[m][j] * rm[n][k] * tensor[l][m][n]
    return sum


def mathematica_format(user_string):
    templist = list(user_string)
    for i in range(0, len(templist)):
        if templist[i] == "[":
            templist[i] = "{"
        elif templist[i] == "]":
            templist[i] = "}"
    tempstr = ""
    for j in range(0, len(templist)):
        tempstr += templist[j]
    return tempstr

