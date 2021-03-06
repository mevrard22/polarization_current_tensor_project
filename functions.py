import sympy as sp  # Symbolic mathematics package
import numpy as np  # Allow me to do math package

'''
Allows the user to enter a matrix via the console, in a 3x6 format, then converts it to a 3x3x3 tensor using the 
adjust_value function, returns the final 3x3x3 matrix
'''


def enter_tensor():
    # Make a placeholder list with arbitrary elements, so it's already formatted
    threeBySix = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    threeByThree = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0],
                                                        [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

    print("Enter each value of the 3x6 matrix representation of your tensor, from "
          "right to left, top to bottom")
    # Go through each element in the 3x6 matrix, as described above
    for i in range(0, 3):
        for j in range(0, 6):
            # Getting input from the user while telling them which row / column they should enter
            temp = input("Enter input for Column " + str(i + 1) + ", Row " + str(j + 1) + ":")
            # Adding the input to list
            if temp == "0":
                threeBySix[i][j] = 0
            else:
                threeBySix[i][j] = sp.exp(temp)

    # Convert the 3x6 array to a 3x3 array
    # Loop through each row of the 3x6 matrix
    for i in range(0, 3):
        # Loop through each column of the 3x6 matrix
        for j in range(0, 6):
            # Function to change the values accordingly
            adjust_value(i, j, threeByThree, threeBySix)
    print("\n 3x6 as 3x3x3 Tensor: \n" + threeByThree.__str__())
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
    x = sp.symbols('x')
    cosine = sp.cos(x); sine = sp.sin(x)
    # Defining the components of the magnetic field and final vector, respectively
    en = [cosine, sine, 0.]; vector_component_list = [0., 0., 0.]
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


'''
Take in 3 values of x, y and z rotation in console, use function mat to get the correct 
rotation matrix for xyz and calculate the rotation matrix at the given angle for xyz, 
then multiply them together and return the overall rotation matrix.
'''


def calculate_overall_rotation_matrix():
    xrot = float(input("Input the rotation angle about the x axis (in degrees):"))
    yrot = float(input("Input the rotation angle about the y axis (in degrees):"))
    zrot = float(input("Input the rotation angle about the z axis (in degrees):"))
    return np.matmul(return_rotation_matrix("y", yrot), np.matmul(return_rotation_matrix("x", xrot), return_rotation_matrix("z", zrot)))


"""
Takes in a string which represents which rotation matrix (x, y or z) and a
float which represents the angle the user would like to input into that rotation matrix
"""


def return_rotation_matrix(axes, angle):
    angle = np.radians(angle)
    cosine = float(np.cos(angle))
    sine = float(np.sin(angle))
    if axes == "x":
        return np.array([[1, 0, 0], [0, cosine, -sine], [0, sine, cosine]])
    elif axes == "y":
        return np.array([[cosine, 0, sine], [0, 1, 0], [-sine, 0, cosine]])
    elif axes == "z":
        return sp.Matrix([[cosine, -sine, 0], [sine, cosine, 0], [0, 0, 1]])
    else:
        return "You didn't input a valid xyz value!"


"""
Takes in a tensor which the user should have inputted through the enter_tensor method, 
rotates it and returns the rotated tensor
"""


def calculate_rotated_tensor(user_tensor, rm):
    tempTensor = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0],
                                                [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(0, 3):
        for j in range(0, 3):
            for k in range(0, 3):
                tempTensor[i][j][k] = tensor_contraction_fn(i, j, k, user_tensor, rm)
    return [mathematica_format(tempTensor.__str__()), tempTensor]


"""
This function is used to do a tensor contraction; otherwise it would be 6 different loops
and it would be too messy.
"""


def tensor_contraction_fn(i, j, k, tensor, rm):
    tempSum = 0.
    for l in range(0, 3):
        for m in range(0, 3):
            for n in range(0, 3):
                numberPart = round(rm[i][l] * rm[j][m] * rm[k][n], 10)
                bothTogether = numberPart * tensor[l][m][n]
                tempSum += bothTogether
    return tempSum


"""
Convert a string (usually, tensor or matrix) to be in a format suitable for use as a 
matrix/tensor with mathematica (how it works is self explanatory)
"""


def mathematica_format(string):
    tempList = list(string)
    for i in range(0, len(tempList)):
        if tempList[i] == "[":
            tempList[i] = "{"
        elif tempList[i] == "]":
            tempList[i] = "}"
        elif tempList[i] == "e":
            tempList[i + 5] = ""
            tempList[i + 3] = ""
            tempList[i + 2] = ""
            tempList[i + 1] = ""
            tempList[i] = ""
        elif tempList[i] == "s" and tempList[i + 1] == "i":
            tempList[i] = "S"
        elif tempList[i] == "c" and tempList[i + 1] == "o":
            tempList[i] = "C"
        elif tempList[i] == "*" and tempList[i + 1] == "*":
            tempList[i] = "^"
            tempList[i + 1] = ""
        # TODO: Figure out how to change () to [] and also not make S of cos capitalized and also turn ** into power
    tempStr = ""
    for j in range(0, len(tempList)):
        tempStr += tempList[j]
    return tempStr
