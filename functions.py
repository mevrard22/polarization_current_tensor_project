import sympy as sp  # Symbolic mathematics package


def enter_matrix():
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
                threeBySix[i][j] = sp.exp(temp)

    # Convert the 3x6 array to a 3x3 array
    # Loop through each row of the 3x6 matrix
    for i in range(0, 3):
        # Loop through each column of the 3x6 matrix
        for j in range(0, 6):
            # Function to change the values accordingly
            adjust_value(i, j, threeByThree, threeBySix)

    # Returning the properly formatted array
    return threeByThree


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


def calculate_dc_current_vector(matrix):
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
                vector_component_list[i] += sp.simplify(en[j] * en[k] * matrix[i][j][k])

    print(vector_component_list.__str__())


def graph_dc_current_vector():
    # Make a function which can graph the dc current vector components
    print()
