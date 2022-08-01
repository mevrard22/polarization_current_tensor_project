import functions as fns
import pyperclip as pc  # To copy and paste the final matrix when it has been processed
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# TODO: Get the a and b and stuff to work on the calculate dc current vector

# Get the overall rotation matrix given the transformation the user wants
rotation_matrix = fns.calculate_overall_rotation_matrix()
print("\n Rotation Matrix: \n" + rotation_matrix.__str__() + "\n")

# Get the user to input the structure of the tensor
user_tensor = fns.enter_tensor()

temp = fns.calculate_rotated_tensor(user_tensor, rotation_matrix)
print("\n Rotated tensor (Mathematica format): " + temp[0].__str__() + "\n")
pc.copy(temp[0])
print('The above has been copied to clipboard')

print("\n DC Current Vector (Mathematica format): " + fns.mathematica_format(fns.calculate_dc_current_vector(temp[1]).__str__()))
# TODO 1: Graph the components of A tensors on a graph, with labels and a key

# TODO 2: Graph both graphs as a subplot
# x = np.arange(-4 * np.pi, 4 * np.pi, 0.1)
# y = l[0][0][0]
# plt.plot(x, y)
# plt.show()

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html#sphx-glr-gallery-subplots-axes-and-figures-subplot-py
# TODO 2: Graph the components of BOTH tensors on two seperate graphs, with labels and a key

# Copy the new matrix to clipboard using pyperclip package

