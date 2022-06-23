def adjust_value(i_index, j_index, threeByThree, threeBySix):
    # Handle cases where looking at first, second or third index of 3x6 matrix
    if j_index <= 2:
        threeByThree[i_index][j_index][j_index] = threeBySix[i_index][j_index]
    # Individually handle cases for when index (j) is 4, 5 or 6
    # Change rules as necessary
    elif j_index == 3:
        threeByThree[i_index][1][2] = threeBySix[i_index][j_index]
        threeByThree[i_index][2][1] = threeBySix[i_index][j_index]
    elif j_index == 4:
        threeByThree[i_index][0][2] = threeBySix[i_index][j_index]
        threeByThree[i_index][2][0] = threeBySix[i_index][j_index]
    elif j_index == 5:
        threeByThree[i_index][1][0] = threeBySix[i_index][j_index]
        threeByThree[i_index][0][1] = threeBySix[i_index][j_index]